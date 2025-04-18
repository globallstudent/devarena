# app/models/question.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from app.core.database import Base

class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    question_text: Mapped[str] = mapped_column(String, nullable=False)
    time_limit: Mapped[int] = mapped_column(default=30)
    order: Mapped[int] = mapped_column()

    game = relationship("Game", back_populates="questions")
    options = relationship("Option", back_populates="question")
    answers = relationship("Answer", back_populates="question")
