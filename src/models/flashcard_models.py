from sqlalchemy import Column, String, Text, Integer, Enum, Date
from pydantic import BaseModel
from datetime import date
from src.config.db import Base

class FlashcardModel(Base):
    __tablename__='flashcard'
    id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)
    tag = Column(String(255))
    difficulty = Column(Enum('Easy', 'Medium', 'Hard'))
    created_at = Column(Date, default=date.today)
    updated_at = Column(Date, default=date.today, onupdate=date.today)

class TextInputSchema(BaseModel):
    text: str

class FlashcardSchema(BaseModel):
    question: str
    answer: str
    tag: str
    difficulty: str

class FlashcardOutSchema(BaseModel):
    id: int
    question: str
    answer: str
    tag: str
    difficulty: str
    created_at: date
    updated_at: date