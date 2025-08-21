from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    name: str
    email: str
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None