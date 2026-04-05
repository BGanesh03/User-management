import jwt
from fastapi import Header, HTTPException
from database import redis_client
from dotenv import load_dotenv
import os

load_dotenv()

SECRET = os.getenv("SECRET_KEY")

def get_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(401, "Token missing")

    token = authorization.split(" ")[1]

    try:
        data = jwt.decode(token, SECRET, algorithms=["HS256"])
        email = data["email"]

        stored = redis_client.get(email)
        if stored != token:
            raise HTTPException(401, "Session expired")

        return email
    except:
        raise HTTPException(401, "Invalid token")