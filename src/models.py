from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

@dataclass
class User:
    id: UUID
    name: str
    email: str
    role: str
    created_at: datetime

@dataclass
class Project:
    id: UUID
    title: str
    description: str
    owner_id: UUID
    status: str
    created_at: datetime