# app/models/game_participant.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, DateTime
from datetime import datetime
from app.core.database import Base

class GameParticipant(Base):
    __tablename__ = "game_participants"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    score: Mapped[int] = mapped_column(default=0)
    joined_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    user = relationship("User", back_populates="participations")
    game = relationship("Game", back_populates="participants")
