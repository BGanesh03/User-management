from pydantic import BaseModel, field_validator
import re

class Register(BaseModel):
    name: str
    email: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$', v):
            raise ValueError("Password must have 1 uppercase, 1 number, 1 symbol, min 8 chars")
        return v

class Login(BaseModel):
    email: str
    password: str

class UpdateProfile(BaseModel):
    name: str