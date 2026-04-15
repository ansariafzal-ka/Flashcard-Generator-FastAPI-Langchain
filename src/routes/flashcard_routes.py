from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.models.flashcard_models import FlashcardSchema, FlashcardOutSchema, TextInputSchema
from src.controllers import flashcard_controllers
from typing import List

router = APIRouter(prefix='/api/v1/flashcards', tags=['flashcards'])

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[FlashcardOutSchema])
def get_all_flashcards(db:Session=Depends(get_db)):
    return flashcard_controllers.get_all_flashcards(db)

@router.get('/{flashcard_id}', status_code=status.HTTP_200_OK, response_model=FlashcardOutSchema)
def get_flashcard(flashcard_id:int, db:Session=Depends(get_db)):
    return flashcard_controllers.get_flashcard(flashcard_id, db)

@router.post('/generate', status_code=status.HTTP_201_CREATED, response_model=FlashcardOutSchema)
def generate_flashcard(request: TextInputSchema, db=Depends(get_db)):
    return flashcard_controllers.generate_flashcard(request, db)

@router.put('/edit/{flashcard_id}', status_code=status.HTTP_201_CREATED, response_model=FlashcardOutSchema)
def edit_flashcard(flashcard_id:int, request:FlashcardSchema, db:Session=Depends(get_db)):
    return flashcard_controllers.edit_flashcard(flashcard_id, request, db)

@router.delete('/delete/{flashcard_id}', status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def delete_flashcard(flashcard_id:int, db:Session=Depends(get_db)):
    return flashcard_controllers.delete_flashcard(flashcard_id, db)
