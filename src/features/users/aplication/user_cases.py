from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from ..domain import User
from .user_services import UserService

@dataclass
class UserUseCases:
    
    user_service: UserService

    async def get_all_users(self) -> List[Dict[str, Any]]:
        users = await self.user_service.get_all_users()
        return [self._to_dict(user) for user in users]

    async def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        user = await self.user_service.get_user_by_id(user_id)
        if user:
            return self._to_dict(user)
        return None

    async def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        user = User(
            name=user_data.get("name"),
            email=user_data.get("email")
        )
        created_user = await self.user_service.create_user(user)
        return self._to_dict(created_user)

    def _to_dict(self, user: User) -> Dict[str, Any]:
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
        }
