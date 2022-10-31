from fastapi import Depends, APIRouter, HTTPException, status
# from fastapi. import 
from sqlalchemy.orm import Session
from typing import List

from ... import  models
from ...schemas import ChallengeNotificationResponse, UsersForm, ChallengeListResponse, UsersFormOut
from ...database import SessionLocal, engine
from sqlalchemy.exc import IntegrityError

from app.Users.oauth2 import get_current_user

router = APIRouter(tags=['Users'])

from ..utils import hash

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @router.get("/users")
# def users(db: Session = Depends(get_db)):
#     return db.query(models.Users).all()


@router.post("/users", response_model=UsersFormOut)
def users(user_form: UsersForm, db: Session = Depends(get_db)):
    try:
        hashed_password = hash(user_form.hashed_password)
        user_form.hashed_password = hashed_password

        query = models.Users(is_active=True, **user_form.__dict__)
        db.add(query)
        db.commit()
        db.refresh(query)
    except IntegrityError as e:

        db.rollback()
        if "UNIQUE constraint failed: users.email" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="email address already exisy in database") from e

        elif " UNIQUE constraint failed: users.username" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="username address already exisy in database") from e

        else: raise e    

    return query


@router.get("/users/notification", response_model=ChallengeNotificationResponse)
def challenge_progress(
                 db: Session = Depends(get_db), 
                current_user: UsersForm = Depends(get_current_user)):
    user = current_user.__dict__["id"]

    query = db.query(models.Users).filter(models.Users.id==user).first()
    return query


@router.get("/users/{id}/challenge", response_model=List[ChallengeListResponse])
def users_(id:int, db: Session = Depends(get_db)):
    return db.query(models.Users).filter(models.Users.id ==id).all()

