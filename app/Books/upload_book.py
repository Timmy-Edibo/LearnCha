from fastapi import APIRouter, File, UploadFile, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/books", tags=["Upload Books"])


from dotenv import load_dotenv
load_dotenv()

import cloudinary.uploader
import cloudinary.api
import cloudinary

cloudinary.config( 
  cloud_name = "learncha", 
  api_key = "635799119624934", 
  api_secret = "hXsnfE0_ajAYij_KUOOUuKME4c4" 
)

@router.post("/upload_book/grade_one")
async def drive(file: UploadFile = File(...)):

    results = cloudinary.uploader.upload(file.file, public_id=file.filename, folder="/LearnCha/grade_one")
    url = results.get("url")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": 200, "message": "Uploaded Successfully", "filename":file.filename, "url": url}) 


@router.post("/upload_book/grade_two",)
async def drive(file: UploadFile = File(...)):

    results = cloudinary.uploader.upload(file.file, public_id=file.filename, folder="/LearnCha/grade_two")
    url = results.get("url")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": 200, "message": "Uploaded Successfully","filename":file.filename, "url": url}) 



@router.post("/upload_book/grade_three")
async def drive(file: UploadFile = File(...)):

    results = cloudinary.uploader.upload(file.file, public_id=file.filename, folder="/LearnCha/grade_three")
    url = results.get("url")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": 200, "message": "Uploaded Successfully", "filename":file.filename, "url": url}) 


@router.post("/upload_book/grade_four")
async def drive(file: UploadFile = File(...)):

    results = cloudinary.uploader.upload(file.file, public_id=file.filename, folder="/LearnCha/grade_four")
    url = results.get("url")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": 200, "message": "Uploaded Successfully", "filename":file.filename, "url": url}) 


@router.post("/upload_book/grade_five")
async def drive(file: UploadFile = File(...)):

    results = cloudinary.uploader.upload(file.file, public_id=file.filename, folder="/LearnCha/grade_five")
    url = results.get("url")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": 200, "message": "Uploaded Successfully", "filename":file.filename, "url": url}) 


@router.post("/upload_book/grade_six")
async def drive(file: UploadFile = File(...)):
    results = cloudinary.uploader.upload(file.file, public_id=file.filename, folder="/LearnCha/grade_six")
    url = results.get("url")

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": 200, "message": "Uploaded Successfully", "filename":file.filename, "url": url}) 


