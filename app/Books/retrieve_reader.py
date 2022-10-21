from fastapi import APIRouter, Form, HTTPException, status


router = APIRouter(prefix="/books", tags=["Retrieve Books"])


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


res = []
@router.get("/retrieve/grade_one")
async def drive_():
  results = cloudinary.Search().expression("folder=LearnCha/grade_one").execute()
  return [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]


res = []
response = set(res)
@router.post("/retrieve/grade_one/search_book")
async def drive_(filename: str = Form(Ellipsis)):
  results = cloudinary.Search().expression(f"folder=LearnCha/grade_one AND filename:{filename}").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Not item with {filename} is found in the database")
 
#############################################################################################
res = []
@router.get("/retrieve/grade_two")
async def drive_():
  results = cloudinary.Search().expression("folder=LearnCha/grade_two").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Not item found")





@router.post("/retrieve/grade_two/search_book")
async def drive_(filename: str = Form(Ellipsis)):
  results = cloudinary.Search().expression(f"folder=LearnCha/grade_two AND filename:{filename}").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Not item with {filename} is found in the database")
 
########################################################################################################
res = []
@router.get("/retrieve/grade_three")
async def drive_():
  results = cloudinary.Search().expression("folder=LearnCha/grade_three").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not item found")

res = []
@router.post("/retrieve/grade_three/search_book")
async def drive_(filename: str = Form(Ellipsis)):
  results = cloudinary.Search().expression(f"folder=LearnCha/grade_three AND filename:{filename}").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Not item with {filename} is found in the database")
 
        
###################################################################################################
res = []
@router.get("/retrieve/grade_four")
async def drive_():
  results = cloudinary.Search().expression("folder=LearnCha/grade_four").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not item found")


@router.post("/retrieve/grade_four/search_book")
async def drive_(filename: str = Form(Ellipsis)):
  results = cloudinary.Search().expression(f"folder=LearnCha/grade_four AND filename:{filename}").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Not item with {filename} is found in the database")
 

###########################################################################################
res = []
@router.get("/retrieve/grade_five")
async def drive_():
  results = cloudinary.Search().expression("folder=LearnCha/grade_five").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not item found")


res = []
@router.post("/retrieve/grade_five/search_book")
async def drive_(filename: str = Form(Ellipsis)):
  results = cloudinary.Search().expression(f"folder=LearnCha/grade_five AND filename:{filename}").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Not item with {filename} is found in the database")
 

##########################################################################################################
res = []
@router.get("/retrieve/grade_six")
async def drive_():
  results =  cloudinary.Search().expression("folder=LearnCha/grade_six").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not item found")


res = []
response = set(res)
@router.post("/retrieve/grade_six/search_book")
async def drive_(filename: str = Form(Ellipsis)):
  results = cloudinary.Search().expression(f"folder=LearnCha/grade_six AND filename:{filename}").execute()
  if res := [{
      "filename": result["filename"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Not item with {filename} is found in the database")
  
#############################################################################################

res = []
@router.get("/retrieve/all_books")
def drive_():
  results = cloudinary.api.resources(max_results=30)
  if res := [{ 
      "filename": result["public_id"],
      "asset_id": result["asset_id"],
      "format": result["format"],
      "created": result["created_at"],
      "url": result["url"]
  } for result in results["resources"]]:
    return res
  else:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Not item found")
 