from fastapi import APIRouter, Body
from transformers import pipeline

router = APIRouter()

# Load QA pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

@router.post("/question-answer")
def question_answer(context: str = Body(...), question: str = Body(...)):
    if not context or not question:
        return {"answer": "Missing context or question."}

    try:
        result = qa_pipeline(question=question, context=context)
        return {"answer": result["answer"], "score": result["score"]}
    except Exception as e:
        return {"error": str(e)}
