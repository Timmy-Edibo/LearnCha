from fastapi import APIRouter, File, UploadFile, status, Depends, Form, status, HTTPException

router = APIRouter(prefix="/books", tags=["Upload Books"])
from pdf2image import convert_from_path


import os
import shutil

from dotenv import load_dotenv
load_dotenv()

import cloudinary.uploader
import cloudinary.api
import cloudinary

cloudinary.config( 
  cloud_name = "globalgist", 
  api_key =os.getenv("CLOUDINARY_SECRET"), 
  api_secret = os.getenv("CLOUDINARY_API_KEY")
)


from ..database import SessionLocal
from sqlalchemy.orm import Session
from ..import models


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


import secrets
import pypdfium2 as pdfium
import os


@router.get("/retrieve_video/all")
async def retrieve_video(db: Session = Depends(get_db)):
    return db.query(models.Video).all()


@router.post("/upload_book")
async def drive(name: str = Form(), category: str = Form(), file: UploadFile = File(...), db: Session =Depends(get_db)):
    
    results = cloudinary.uploader.upload(file.file, public_id=file.filename, folder="/learncha/books")
    image_url = results.get("url")

    file_extension = file.filename.split(".")[1].lower()

    generated_num = secrets.token_hex(16)
    isbn = f"{generated_num}.{file_extension}"
    isbn = generated_num
    query = models.Books(name=name.lower(), book_isbn =isbn , url=image_url, category=category.lower())

    db.add(query)
    db.commit()
    db.refresh(query)
    return {"data": query, "status_code": status.HTTP_201_CREATED, "message": "Uploaded Successfully"}




@router.post("/upload_thumbnail")
async def upload_thumbnail(id: int, image: UploadFile = File(...), db: Session =Depends(get_db)):

    with open(image.filename, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
        pdf = pdfium.PdfDocument(f"{image.filename}")
        n_pages = len(pdf)
        
        for page_number in range(n_pages):
            page = pdf.get_page(page_number)
            pil_image = page.render_topil(
                scale=1,
                rotation=0,
                crop=(0, 0, 0, 0),
            )
            pil_image.save(f"image_{page_number}.png")

            if page_number == 0:
                break

    with open("image_0.png", "rb") as file:
        byte_im = file.read()
        results = cloudinary.uploader.upload(byte_im, public_id=image.filename, folder="/learncha_photos/thumbnails/")
        image_url = results.get("url")

    os.remove(f"{image.filename}")
    os.remove("image_0.png")
    query = models.BookThumbnail(book_id =id , thumbnail_url=image_url)
    db.add(query)
    db.commit()
    db.refresh(query)
    return {"respnse": query,
            "status": status.HTTP_201_CREATED,
            "message": "Uploaded Successfully"}



@router.post("/upload_video")
async def upload_video(video_title: str = Form(), 
                        subject: str = Form(),
                        topic: str = Form(),
                        video: UploadFile = File(...), db: Session =Depends(get_db)):
    if query := db.query(models.Video).filter(models.Video.video_title == video_title).first():
        raise HTTPException(status_code=401, detail="video uploaded already, video title is unique")

    results = cloudinary.uploader.upload_large(video.file, public_id=video.filename, folder="/learncha/videos/", resource_type = "video")
    video_url = results.get("url")
    query = models.Video(video_url=video_url, video_title=video_title, subject=subject, topic=topic)
    db.add(query)
    db.commit()
    db.refresh(query)
    return query



