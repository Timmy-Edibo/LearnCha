from fastapi import APIRouter, File, UploadFile, Depends, HTTPException

router = APIRouter(prefix="/books", tags=["Upload Books"])
import pypdfium2 as pdfium
import os
import shutil

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



def thumbnail_to_cloud(thumbnail_id: int, book_id:int, db: Session = Depends(get_db), image: UploadFile = File(...)):
    try:
        # Save the uploaded file
        with open(image.filename, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        # Process the PDF
        with pdfium.PdfDocument(image.filename) as pdf:
            n_pages = len(pdf)
            for page_number in range(min(n_pages, 1)):  # Process only the first page
                page = pdf.get_page(page_number)
                pil_image = page.render_topil(scale=1, rotation=0, crop=(0, 0, 0, 0))
                pil_image.save(f"image_{page_number}.png")


        # Upload the first page image to cloudinary
        with open("image_0.png", "rb") as file:
            byte_im = file.read()
            results = cloudinary.uploader.upload(byte_im, public_id=image.filename, folder="/learncha/thumbnails/")
            image_url = results.get("url")

        # Remove temporary files
        os.remove(f"{image.filename}")
        os.remove("image_0.png")

        # Update the thumbnail record in the database
        query = db.query(models.BookThumbnail).filter(models.BookThumbnail.id==thumbnail_id)
        if not query:
            raise HTTPException(status_code=404, detail=f"Thumbnail with id {thumbnail_id} not found")
        

        query.update({"thumbnail_url": image_url})
        db.commit()
        db.refresh(query)

        return {"message": "Thumbnail updated successfully"}
    except Exception as e:
        # Handle exceptions (e.g., file operations, PDF processing, cloudinary upload)
        return {"error": str(e)}


def delete_existing_thumbail(book_id, thumbnail_id, db:Session = Depends(get_db)):
    deleted_count = db.query(models.BookThumbnail).filter(
        models.BookThumbnail.book_id == book_id,
        models.BookThumbnail.id != thumbnail_id
            ).delete(synchronize_session=False)
