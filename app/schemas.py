from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional, List


class UsersForm(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str
    phone_number: str
    address: str

    class Config:
        orm_mode = True    


class UsersFormOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: str
    address: str
    is_active: bool

    class Config:
        orm_mode = True   

class ChallengeProgressResponse(BaseModel):
    user: UsersFormOut
    image: str


    class Config:
        orm_mode = True


class CreateChallengeForm(BaseModel):
    name: str
    description: str
    challenge_type: str

    class Config:
        orm_mode = True

class ChallengeFormResponse(CreateChallengeForm):
    id: int
    # progress: List[ChallengeProgressResponse]

    class Config:
        orm_mode = True
        


# class ChallengeFormResponse(CreateChallengeForm):
#     progress: List[ChallengeProgressResponse]

#     class Config:
#         orm_mode = True
        

class JoinChallenge(BaseModel):
    user_id: int
    Challenge_id: str


class AddChallengeMembers(BaseModel):
    Challenge_id: int

    class Config:
        orm_mode = True


class JoinedChallenge(BaseModel):
    challenge: CreateChallengeForm

    class Config:
        orm_mode = True

class ChallengeListResponse(UsersFormOut):
    id:int
    challenge_table: List[ChallengeFormResponse]
    challenges_joined: List[JoinedChallenge]

    class Config:
        orm_mode = True
    

class ChallengeMembers(BaseModel):
    challenge_id:int
    user_id: int
    user: UsersFormOut

    class Config:
        orm_mode = True    

class ChallangeViewResponse(CreateChallengeForm, BaseModel):
    id: int
    users_table: UsersFormOut
    challenge_members: List[ChallengeMembers]    
    # progress: List[ChallengeProgressResponse]

    class Config:
        orm_mode = True

class ChallangeProgressViewResponse(CreateChallengeForm, BaseModel):
    id: int
    users_table: UsersFormOut
    challenge_members: List[ChallengeMembers]    
    progress: List[ChallengeProgressResponse]

    class Config:
        orm_mode = True


class ChallengeNotification(BaseModel):
    # id: int
    message: str

    class Config:
        orm_mode = True

class JoinChallengeNotification(BaseModel):
    # id: int
    message: str  

    class Config:
        orm_mode = True


class ChallengeNotificationResponse(BaseModel):
    id: int
    is_active: bool
    notifier: List[ChallengeNotification]
    notifier_join: List[JoinChallengeNotification]


    class Config:
        orm_mode = True


class ChallengeprogressRes(BaseModel):
    id:int
    user_id: int
    challenge_id: int
    image: str

    class Config:
        orm_mode = True

class ChallengeTrending(ChallangeViewResponse):
    progress: List[ChallengeprogressRes]
    # progress: List[ChallengeprogressRes]

    class Config:
        orm_mode = True

class BookThumbnail(BaseModel):
    book_id: int
    thumbnail_url: str

    class Config:
        orm_mode = True
class Book(BaseModel):
    id: int
    name: str
    category: str
    book_isbn: str
    url: str
    created_at: datetime
    thumbnail: List[BookThumbnail]

    class Config:
        orm_mode = True
###########################################################################################



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

class ForgetPassword(BaseModel):
    email: str



class BlacklistToken(BaseModel):
    email: EmailStr
    token: str

class ResetPassword(BaseModel):
    new_password: str
    confirm_password: str
