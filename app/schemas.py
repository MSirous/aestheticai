from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Optional[str] = "artist"  # پیش‌فرض

class UserLogin(BaseModel):
    email: EmailStr
    password: str