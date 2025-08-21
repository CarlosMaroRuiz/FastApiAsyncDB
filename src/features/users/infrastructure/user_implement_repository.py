from dataclasses import dataclass
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..domain import UserRepository, User
from .user_schema import UserSchema

@dataclass
class UserRepositoryImplement(UserRepository):
    
    session: AsyncSession

    async def get_all(self) -> List[User]:
        query = select(UserSchema)
        result = await self.session.execute(query)
        user_models = result.scalars().all()
        return [self._to_entity(user_model) for user_model in user_models]

    async def get_by_id(self, user_id: int) -> Optional[User]:
        query = select(UserSchema).where(UserSchema.id == user_id)
        result = await self.session.execute(query)
        user_model = result.scalar_one_or_none()
        if user_model:
            return self._to_entity(user_model)
        return None

    async def create(self, user: User) -> User:
        user_model = UserSchema(
            name=user.name,
            email=user.email
        )
        self.session.add(user_model)
        await self.session.commit()
        await self.session.refresh(user_model)

        user.id = user_model.id
        return user

    def _to_entity(self, user_model: UserSchema) -> User:
        return User(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email
        )