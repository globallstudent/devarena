# app/schemas/question.py
from pydantic import BaseModel
from typing import List

class OptionCreate(BaseModel):
    text: str
    is_correct: bool

class QuestionCreate(BaseModel):
    question_text: str
    time_limit: int = 30
    order: int
    options: List[OptionCreate]

class QuestionOut(BaseModel):
    id: int
    question_text: str
    time_limit: int
    order: int
    options: List[OptionCreate]

    class Config:
        from_attributes = True
