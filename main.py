from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from src.routes.flashcard_routes import router as flashcard_router
from src.config.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Flashcards Generator API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(flashcard_router)

@app.get("/health")
async def health_check():
    return Response(status_code=status.HTTP_200_OK)
