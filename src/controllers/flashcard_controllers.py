from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from src.models.flashcard_models import FlashcardModel, FlashcardSchema, TextInputSchema
from src.helpers.ai_model import ai_flashcard

def get_all_flashcards(db:Session):
    try:
        flashcards = db.query(FlashcardModel).all()
        return flashcards
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to get all flashcards: {e}')
    
def get_flashcard(flashcard_id:int, db:Session):
    try:
        flashcard = db.query(FlashcardModel).get(flashcard_id)
        if not flashcard:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Flashcard with id {flashcard_id} not found')
            
        return flashcard
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to get flashcard: {e}')
    
def generate_flashcard(request:TextInputSchema, db:Session):
    try:
        ai_result = ai_flashcard(text=request.text)
        new_flashcard = FlashcardModel(
            question=ai_result.question,
            answer=ai_result.answer,
            tag=ai_result.tag,
            difficulty=ai_result.difficulty
        )

        db.add(new_flashcard)
        db.commit()
        db.refresh(new_flashcard)

        return new_flashcard

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to generate flashcard: {e}')
    
def edit_flashcard(flashcard_id:int, request:FlashcardSchema, db:Session):
    try:
        flashcard = db.query(FlashcardModel).get(flashcard_id)
        if not flashcard:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Flashcard with id {flashcard_id} not found')
        
        flashcard.question = request.question
        flashcard.answer = request.answer
        flashcard.tag = request.tag
        flashcard.difficulty = request.difficulty

        db.commit()
        db.refresh(flashcard)

        return flashcard
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to edit flashcard: {e}')
    
def delete_flashcard(flashcard_id:int, db:Session):
    try:
        flashcard = db.query(FlashcardModel).get(flashcard_id)
        if not flashcard:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Flashcard with id {flashcard_id} not found')
        db.delete(flashcard)
        db.commit()
        return None
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to delete flashcard: {e}')