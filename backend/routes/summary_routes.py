
# backend/routes/summary_routes.py

from fastapi import APIRouter, Body
from backend.services.text_summarizer import summarize_text

router = APIRouter()

@router.post("/generate")
async def generate_summary(text: str = Body(..., embed=True)):
    """
    Generates a summary for the provided text.
    """
    summary = summarize_text(text)
    return {"summary": summary}
