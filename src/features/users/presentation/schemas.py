
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
   
    name: str = Field(..., min_length=2, max_length=100, description="Nombre del usuario")
    email: EmailStr = Field(..., description="Correo electrónico del usuario")

class UserCreate(UserBase):
    """Esquema para crear usuarios"""
    pass
   

class UserResponse(UserBase):
    """Esquema para respuestas con información de usuario"""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True  
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Juan Pérez",
                "email": "juan@example.com",
                "created_at": "2025-08-21T10:00:00",
                "updated_at": "2025-08-21T10:00:00"
            }
        }