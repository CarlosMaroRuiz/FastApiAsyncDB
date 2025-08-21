from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..aplication import UserUseCases
from .user_controller import user_controller
from .schemas import UserResponse, UserCreate

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.get("/", response_model=List[UserResponse])
async def get_all_users(usecases: UserUseCases = Depends(user_controller)):
    return await usecases.get_all_users()

@user_router.get("/{id}", response_model=UserResponse)
async def get_user_by_id(id: int, usecases: UserUseCases = Depends(user_controller)):
    user = await usecases.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@user_router.post("/", response_model=UserResponse, status_code=201)
async def create_user(user_data: UserCreate, usecases: UserUseCases = Depends(user_controller)):
    return await usecases.create_user(user_data.dict())