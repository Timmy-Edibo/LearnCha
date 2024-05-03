from fastapi import APIRouter, File, UploadFile, status, Depends, Form, status, HTTPException, BackgroundTasks
from app.Books.utils import delete_existing_thumbail, thumbnail_to_cloud
router = APIRouter(prefix="/books", tags=["Upload Books"])
import secrets
import os

from dotenv import load_dotenv
load_dotenv()

import cloudinary.uploader
import cloudinary.api
import cloudinary

cloudinary.config( 
  cloud_name = "globalgist", 
  api_key =os.getenv("CLOUDINARY_API_KEY"), 
  api_secret = os.getenv("CLOUDINARY_SECRET")
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
async def upload_thumbnail(background_task: BackgroundTasks, id: int, 
            image: UploadFile = File(...), 
            db: Session =Depends(get_db)):

    query = models.BookThumbnail(book_id =id , thumbnail_url="test_url")
    db.add(query)
    db.commit()
    db.refresh(query)

    delete_existing_thumbail(query.book_id, query.id, db)    
    background_task.add_task(thumbnail_to_cloud, query.id, query.book_id, db, image)

    return {"response": query,
            "status": status.HTTP_201_CREATED,
            "message": "Uploaded Successfully"}


@router.get("/get_all_thumbnails/all")
async def get_all_thumbnails(db: Session =Depends(get_db)):

    query = db.query(models.BookThumbnail).all()
    return {"response": query,
            "status": status.HTTP_200_OK}

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



