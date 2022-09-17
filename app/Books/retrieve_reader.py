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



@router.get("/retrieve/grade_one")
async def drive_():
  return cloudinary.Search().expression("folder=LearnCha/grade_one").execute()

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

@router.get("/retrieve/grade_two")
async def drive_():
  return cloudinary.Search().expression("folder=LearnCha/grade_two").execute()

res = []
response = set(res)
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

@router.get("/retreive/grade_three")
async def drive_():
  return cloudinary.Search().expression("folder=LearnCha/grade_three").execute()

res = []
response = set(res)
@router.post("/retreive/grade_three/search_book")
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

@router.get("/retreive/grade_four")
async def drive_():
  return cloudinary.Search().expression("folder=LearnCha/grade_four").execute()

res = []
response = set(res)
@router.post("/retreive/grade_four/search_book")
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

@router.get("/retreive/grade_five")
async def drive_():
  return cloudinary.Search().expression("folder=LearnCha/grade_five").execute()

res = []
response = set(res)
@router.post("/retreive/grade_five/search_book")
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

@router.get("/retreive/grade_six")
async def drive_():
  return cloudinary.Search().expression("folder=LearnCha/grade_six").execute()

res = []
response = set(res)
@router.post("/retreive/grade_six/search_book")
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
  
        


# @router.post("/book/find_book")
# async def drive_(item: Optional[str] = Form(...)):
#     # return cloudinary.api.subfolders("samples",)
#     # return cloudinary.api.resources(max_results = 30)
#     return cloudinary.Search().expression(f"{item}").execute()


res = []
@router.get("/retrieve/all_books")
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
 