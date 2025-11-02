"""API routes."""
from typing import List

from fastapi import APIRouter, HTTPException, status

from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

# Тимчасове сховище (в реальному проекті використовуйте базу даних)
fake_users_db: List[dict] = []


@router.get("/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy", "message": "API is running"}


@router.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> UserResponse:
    """Create a new user."""
    # Перевірка чи користувач вже існує
    for existing_user in fake_users_db:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists"
            )
    
    # Створення нового користувача
    new_user = {
        "id": len(fake_users_db) + 1,
        "email": user.email,
        "full_name": user.full_name,
        "is_active": True
    }
    fake_users_db.append(new_user)
    
    return UserResponse(**new_user)


@router.get("/users/", response_model=List[UserResponse])
async def get_users() -> List[UserResponse]:
    """Get all users."""
    return [UserResponse(**user) for user in fake_users_db]


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> UserResponse:
    """Get user by ID."""
    for user in fake_users_db:
        if user["id"] == user_id:
            return UserResponse(**user)
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )