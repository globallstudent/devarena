# app/schemas/game.py
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from .user import UserOut

class GameCreate(BaseModel):
    title: str

class GameOut(BaseModel):
    id: int
    title: str
    status: str
    creator: UserOut
    created_at: datetime

    class Config:
        from_attributes = True
