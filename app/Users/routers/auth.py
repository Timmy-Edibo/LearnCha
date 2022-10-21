from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from ... import models

from .. import utils, oauth2
from ... import schemas

from ... import database

from .. import oauth2

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), 
            db: Session = Depends(database.get_db)):

    user = db.query(models.Users).filter(
        models.Users.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")


    if not utils.verify(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")


    # create a token
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}  



# @router.get("/logout")
# def logout(db: Session= Depends(database.get_db),
#             token: str = Depends(oauth2.get_token_user),
#             current_user: users_schema.UserBase = Depends(oauth2.get_current_user)):

#             auth_cruds.blacklist_token(db, token=token, current_user=current_user)
#             return {"status_code": status.HTTP_200_OK,
#                     "detail": "User logged out successfully",
#                    }   


# @router.post('/forget_password')
# async def forget_password(email_form: auth_schema.ForgetPassword, 
#                             db:Session= Depends(database.get_db)):

#     # If user exist
#     user = db.query(models.Users).filter(
#         models.Users.email == email_form.email).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#     # return auth_cruds.create_rest_code(db=db, form=email_form)     
#     token = oauth2.create_access_token(data={"user_id": user.id})
#     reset_link = f"http://localhost:8000/reset?token={token}"

#     # Send the email to the user
#     await EmailUtils.password_reset(
#                 subject="Password Reset", 
#                 email=user.email,
#                 body={"title": "Password Reset",   
#                     "name":  user.username,
#                     "reset_link":reset_link,
                    
#         })


# @router.put("/reset_password", description="Reset Password Here", )
# async def check_reset_password(token:str,  
#                                 request: auth_schema.ResetPassword, 
#                                 db: Session= Depends(database.get_db)):
#     # Fetch current user
#     user__ = oauth2.get_current_user(token, db=db)

#     if request.new_password != request.confirm_password:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
#                             detail="Password does not match, input correct password")
    
#     # Hashing of new password
#     hashed_password = utils.hash(request.new_password)  
#     # user.update = hashed_password

#     user_id = user__.id
#     user = db.query(models.Users).filter(models.Users.id==user_id)
#     # user = db.query(models.Users).filter(models.Users.id==user_id).first()

#     user.update({'password': hashed_password})
#     db.commit()
#     return "password successfully updated"




@router.get('/me')
def get_current_user(token: str = Depends(oauth2.get_token_user),
                        current_user: schemas.UsersForm = Depends(oauth2.get_current_user),
                        db: Session= Depends(database.get_db)):

        user__ = oauth2.get_current_user(token, db=db)
        return db.query(models.Users).filter(models.Users.id == user__.id).first()


