from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.upload_pdf import router as UploadRouter
from routes.summarize import router as SummarizeRouter
from routes.question_answer import router as QARouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(UploadRouter)
app.include_router(SummarizeRouter)
app.include_router(QARouter)

@app.get("/")
def read_root():
    return {"message": "LegalLens AI backend is running 🚀"}
