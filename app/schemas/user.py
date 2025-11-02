"""User schemas."""
from typing import Optional

# EmailStr: спеціальний тип з pydantic, який автоматично перевіряє, що значення є валідною email-адресою. Використовується для валідації email у моделях.
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base user schema."""
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """User creation schema."""
    password: str


class UserResponse(UserBase):
    """User response schema."""
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    """User update schema."""
    full_name: Optional[str] = None
    is_active: Optional[bool] = None