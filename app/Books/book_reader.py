from dataclasses import field
import json
from unittest import result
from fastapi import APIRouter, Form, File, UploadFile, Body


router = APIRouter(prefix="/books", tags=["Books"])


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

@router.post("/book/upload_book")
async def drive(file: UploadFile = File(...)):
    print(file.filename)

    results = cloudinary.uploader.upload(file.file, public_id=file.filename)
    url = results.get("url")
    print(url)


@router.post("/book/find_book")
async def drive_(item: str = Form(...)):
    # return cloudinary.api.subfolders("samples",)
    # return cloudinary.api.resources(max_results = 30)
    return cloudinary.Search().expression(f"{item}").execute()

from pydantic import BaseModel

res = []
@router.get("/book/all_books")
def drive_():
  results =  cloudinary.api.resources(max_results=30)

  for result in results["resources"]:
    response = {"filename": result["public_id"], 
                "asset_id": result["asset_id"],
                "format": result["format"],
                "created_at": result["created_at"],
                "url": result["url"]}

    res.append(response)
  return res
 