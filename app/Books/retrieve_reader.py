from fastapi import APIRouter, Form, HTTPException, status, Depends


router = APIRouter(prefix="/books", tags=["Retrieve Books"])

from ..database import SessionLocal
from sqlalchemy.orm import Session
from ..import models


from dotenv import load_dotenv
load_dotenv()

import cloudinary.uploader
import cloudinary.api
import cloudinary


import os

cloudinary.config( 
  cloud_name = "learncha", 
  api_key =os.getenv("CLOUDINARY_SECRET"), 
  api_secret = os.getenv("CLOUDINARY_API_KEY")
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from ..schemas import Book
from typing import List, Union
from sqlalchemy import or_


@router.get("/", response_model=List[Book])
async def drive_(db:Session = Depends(get_db)):
  return db.query(models.Books).all()
  
@router.get("/{id}", response_model=Book)
async def drive_(id: int, db:Session = Depends(get_db)):
  if query :=  db.query(models.Books).filter(models.Books.id==id).first():
    return query
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
   detail=f"Book with id {id} not found")


@router.get("/search", response_model=List[Book])
async def drive_(category: Union[str, None]=None, name: Union[str, None]=None, db:Session = Depends(get_db)):
    if query :=  db.query(models.Books).filter(or_(
              models.Books.category.contains(str(category).lower()),
              models.Books.name.contains(str(name).lower())
              )).all():
      return query
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")