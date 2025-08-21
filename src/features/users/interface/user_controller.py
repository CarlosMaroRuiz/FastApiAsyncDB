from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.di import get_db_session
from ..infrastructure import UserRepositoryImplement
from ..aplication import UserService, UserUseCases


async def get_user_repository(session: AsyncSession = Depends(get_db_session)):
    
    return UserRepositoryImplement(session=session)

async def get_user_service(repository = Depends(get_user_repository)):
 
    return UserService(user_repository=repository)

async def user_controller(service = Depends(get_user_service)):

    return UserUseCases(user_service=service)