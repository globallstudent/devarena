# app/models/answer.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, DateTime, Boolean
from datetime import datetime
from app.core.database import Base

class Answer(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    selected_option_id: Mapped[int] = mapped_column(ForeignKey("options.id"))
    is_correct: Mapped[bool] = mapped_column()
    answered_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    game = relationship("Game", back_populates="answers")
    question = relationship("Question", back_populates="answers")
    user = relationship("User", back_populates="answers")
