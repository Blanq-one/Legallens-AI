from fastapi import APIRouter, Body
from transformers import pipeline

router = APIRouter()

# Load summarization pipeline (you can switch to a legal-specific model later)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@router.post("/summarize")
def summarize_text(text: str = Body(..., embed=True)):
    if len(text) < 50:
        return {"summary": "Text too short to summarize."}
    
    # Hugging Face summarization
    summary = summarizer(text[:1000], max_length=150, min_length=30, do_sample=False)

    return {"summary": summary[0]['summary_text']}
