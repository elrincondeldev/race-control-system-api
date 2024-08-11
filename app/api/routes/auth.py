from fastapi import FastAPI, Request, HTTPException, Depends, APIRouter
from authx import AuthX, AuthXConfig, RequestToken
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY="SECRET_KEY",
    JWT_TOKEN_LOCATION=["headers"],
)

auth = AuthX(config=config)

@router.get('/login')
async def login(username: str, password: str):
    if username == os.getenv("username") and password == os.getenv("password"):
        token = auth.create_access_token(uid=username)
        return {"access_token": token}
    raise HTTPException(401, detail={"message": "Invalid credentials"})

# Define an async dependency function to get the token
async def get_token(request: Request) -> RequestToken:
    return await auth.get_access_token_from_request(request)

@router.get("/protected")
async def get_protected(
    request: Request,
    token: RequestToken = Depends(get_token)  # Use the async dependency function
):
    try:
        # Call verify_token without `await` if it's not async
        auth.verify_token(token=token)
        return {"message": "Hello world !"}
    except Exception as e:
        raise HTTPException(401, detail={"message": str(e)}) from e
