# app/models/game.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base

class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="waiting")  # waiting, started, ended
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    creator = relationship("User", back_populates="games_created")

    participants = relationship("GameParticipant", back_populates="game")
    questions = relationship("Question", back_populates="game")
    answers = relationship("Answer", back_populates="game")
