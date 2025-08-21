from dataclasses import dataclass
from typing import List, Optional
from ..domain import UserRepository,User

@dataclass
class UserService:
    #recibe un interface de repository
    user_repository: UserRepository

    async def get_all_users(self) -> List[User]:
        """Retorna todos los usuarios."""
        return await self.user_repository.get_all()

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Retorna un usuario por su ID, o None si no existe."""
        return await self.user_repository.get_by_id(user_id)

    async def create_user(self, user: User) -> User:
        """Crea un nuevo usuario y lo retorna."""
        return await self.user_repository.create(user)
