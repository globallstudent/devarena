# app/schemas/answer.py
from pydantic import BaseModel
from datetime import datetime

class AnswerSubmit(BaseModel):
    question_id: int
    selected_option_id: int

class AnswerOut(BaseModel):
    question_id: int
    is_correct: bool
    answered_at: datetime

    class Config:
        from_attributes = True
