# app/models/answer.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base

class Answer(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    selected_option_id: Mapped[int] = mapped_column(ForeignKey("options.id"))
    is_correct: Mapped[bool]
    answered_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    user = relationship("User", back_populates="answers")
    game = relationship("Game", back_populates="answers")
    question = relationship("Question", back_populates="answers")
