from operator import or_
from fastapi import Depends, APIRouter, HTTPException, status, File, UploadFile, Form, Body
# from fastapi. import 
from sqlalchemy.orm import Session
from sqlalchemy import or_, func



from typing import List

from .import  models
from .schemas import (ChallangeViewResponse, 
                        ChallangeProgressViewResponse,
                        ChallengeTrending, 
                        CreateChallengeForm, 
                        UsersForm, ChallengeFormResponse)

from .database import SessionLocal, engine
from sqlalchemy.exc import IntegrityError
from .Users.oauth2 import get_current_user

import cloudinary.uploader
import cloudinary.api
import cloudinary

cloudinary.config( 
  cloud_name = "learncha", 
  api_key = "635799119624934", 
  api_secret = "hXsnfE0_ajAYij_KUOOUuKME4c4" 
)


router = APIRouter(tags=['Challenge'])


models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/challenge", response_model=List[ChallengeFormResponse])
def get_all_challenge(db: Session = Depends(get_db)):
    return db.query(models.Challenge).all()


@router.get("/challenge/{id}", response_model=ChallangeViewResponse)
def view_challenge(id: int, db: Session = Depends(get_db)):
    if query := db.query(models.Challenge).filter(models.Challenge.id == id).first():
        return query
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"challenge with id {id} not found")

@router.get("/challenge/progress/{id}", response_model=ChallangeProgressViewResponse)
def view_challenge_with_progress(id: int, db: Session = Depends(get_db)):
    if query := db.query(models.Challenge).filter(models.Challenge.id == id).first():
        return query
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"challenge with id {id} not found")


@router.get("/challenge/search/{name}", response_model=List[ChallangeProgressViewResponse])
def search_challenge(name: str, db: Session = Depends(get_db)):
    if query := db.query(models.Challenge).filter(
        or_(models.Challenge.name.contains(name.lower()), 
                            models.Challenge.description.contains(name.lower()))).all():

        return query
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"challenge with name {name} not found")        


@router.get("/challenge/{id}")
def challenge_by_id(id: int, db: Session = Depends(get_db)):

    if query := db.query(models.Challenge).filter(models.Challenge.id == id).first():
        return query
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"challenge with id {id} not found")


@router.post("/challenge")
def create_challenge(
                    form: CreateChallengeForm, db: Session = Depends(get_db), 
                    current_user: UsersForm = Depends(get_current_user),
                ):
    try:

        form.name = form.name.lower()
        query = models.Challenge(user_id=current_user.__dict__["id"], **form.__dict__)
        if check_challenge := db.query(models.Challenge).filter(models.Challenge.user_id==current_user.__dict__["id"]).filter(
            models.Challenge.name == query.name ).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                detail="You have an active challenge with the same name")


        notify = models.ChallengeNotification(user_id=current_user.__dict__["id"], challenge_name=form.name.lower(), message=f"You have created a new challenge: {form.name.lower()}")
        db.add(query)
        db.add(notify)

        db.commit()

        db.refresh(query)
        db.refresh(notify)
    except IntegrityError as e:
        print(e)


    link = f"https://learncha.mybluemix.net/challenge/{query.id}"
    return {"query": query,
            "challenge_link": link
    }


@router.post("/challenge/{id}/join")
def challenge(id: int, db: Session = Depends(get_db),  
                current_user: UsersForm = Depends(get_current_user)):
    user_id = current_user.__dict__["id"]

    self_created =db.query(models.Challenge).filter(
        models.Challenge.user_id==user_id).filter(models.Challenge.id == id).first()

    check_if_added = db.query(models.ChallengeMembers).filter(models.ChallengeMembers.user_id==user_id).filter(
        models.ChallengeMembers.challenge_id==id).first()


    get_challenge_name = db.query(models.Challenge).filter(models.Challenge.id ==id).first()
    if not get_challenge_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Challenge with id {id} does not exist")    

    if not check_if_added and not self_created:
        add_members = models.ChallengeMembers(user_id=user_id, challenge_id=id)

        notify_to_creator = models.ChallengeNotification(user_id=get_challenge_name.__dict__["user_id"], challenge_name=get_challenge_name.__dict__["name"], message=f"{current_user.__dict__['name']} have joined your challenge: {get_challenge_name.__dict__['name']}")
        notify_for_joining = models.JoinChallengeNotification(user_id=current_user.__dict__["id"], challenge_id=id, message=f"You have joined a new challenge: {get_challenge_name.__dict__['name']}")


        db.add(add_members)
        db.add(notify_to_creator)
        db.add(notify_for_joining)

        db.commit()

        db.refresh(add_members)
        db.refresh(notify_to_creator)
        db.refresh(notify_for_joining)

        return "You have successfully joined the challenge"
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already part of the challenge")    



@router.post("/challenge/{id}/progress")
async def challenge_progress(id: int,  image: UploadFile= File(...), 
             db: Session = Depends(get_db), 
                current_user: UsersForm = Depends(get_current_user)):
    
    user = current_user.__dict__["id"]

    self_created =db.query(models.Challenge).filter(
        models.Challenge.user_id==user).filter(models.Challenge.id == id).first()

    joined = db.query(models.ChallengeMembers).filter(
        models.ChallengeMembers.user_id==user).filter(models.ChallengeMembers.challenge_id == id).first()

    if not self_created and not joined:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"You have not created or joined any challenge with specified id {id}")
    file_format = ["png", "jpg", "jpeg"]
    if [x for x in file_format if image.filename.split(".")[1]]:
        
        results = cloudinary.uploader.upload(image.file, public_id=image.filename, folder="/Learncha_photos/")
        image_url = results.get("url")
        query = models.ChallengeProgress(user_id=user, challenge_id=id, image =image_url)
        db.add(query)
        db.commit()
        db.refresh(query)
        return query
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Accepted File type png, jpg or jpeg.")


@router.get("/trending/all", response_model=List[ChallengeTrending])
def trending_challenge(db: Session = Depends(get_db)):
    return db.query(models.Challenge).all()