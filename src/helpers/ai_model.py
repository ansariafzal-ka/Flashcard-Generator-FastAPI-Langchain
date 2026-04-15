from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from src.models.flashcard_models import FlashcardSchema
from dotenv import load_dotenv

load_dotenv()
model = init_chat_model(model='gpt-4o')
prompt = ChatPromptTemplate([
    ('system', 'You generate Q&A flashcards from text. Create ONE flashcard with question, answer, tag, and difficulty (Easy/Medium/Hard).'),
    ('human', 'Generate a flashcard from this text: {text}')
])

def ai_flashcard(text:str):
    structured_model = model.with_structured_output(FlashcardSchema)
    chain = prompt | structured_model
    response = chain.invoke({'text': text})
    return response