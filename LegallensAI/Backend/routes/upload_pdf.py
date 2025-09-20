from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter(prefix="/upload-pdf", tags=["Upload PDF"])

UPLOAD_FOLDER = "Data/Uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "File uploaded successfully", "filename": file.filename, "path": file_path}
