from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    phone_number =Column(String(20))
    address = Column(String(50))
    is_active = Column(Boolean, default=True)

    challenge_table = relationship("Challenge", back_populates = "users_table")
    challenges_joined =  relationship("ChallengeMembers", back_populates = "user")

    progress = relationship("ChallengeProgress", back_populates = "user")

    notifier = relationship("ChallengeNotification", back_populates = "user")
    notifier_join = relationship("JoinChallengeNotification", back_populates = "user_join_notification")




class Challenge(Base):
    __tablename__ = "challenge"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    name = Column(String)
    challenge_type = Column(String)
    description = Column(String)
    # image = Column(String)
    status = Column(String, default="active")

    users_table =  relationship("Users", back_populates = "challenge_table")
    challenge_members =  relationship("ChallengeMembers", back_populates = "challenge")

    progress = relationship("ChallengeProgress", back_populates = "challenge")
    # notifier = relationship("ChallengeNotification", back_populates = "challenge")
    notifier_join = relationship("JoinChallengeNotification", back_populates = "challenge_join_notification")



class ChallengeMembers(Base):
    __tablename__ = "challenge_members"

    id =  Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    challenge_id = Column(Integer,  ForeignKey("challenge.id", ondelete="CASCADE"))

    user =  relationship("Users", back_populates = "challenges_joined")
    challenge = relationship("Challenge", back_populates = "challenge_members")



class ChallengeProgress(Base):
    __tablename__ = "challenge_progress"
     
    id =  Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    challenge_id = Column(Integer,  ForeignKey("challenge.id", ondelete="CASCADE"))
    image = Column(String)

    user =  relationship("Users", back_populates = "progress")
    challenge = relationship("Challenge", back_populates = "progress")


class ChallengeNotification(Base):
    __tablename__="challenge_notification"

    id =  Column(Integer, primary_key=True, index=True)
    message = Column(String)
    challenge_name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    user =  relationship("Users", back_populates = "notifier")

class JoinChallengeNotification(Base):
    __tablename__="join_challenge_notification"

    id =  Column(Integer, primary_key=True, index=True)
    message = Column(String)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    challenge_id = Column(Integer,  ForeignKey("challenge.id", ondelete="CASCADE"))

    user_join_notification =  relationship("Users", back_populates = "notifier_join")
    challenge_join_notification = relationship("Challenge", back_populates = "notifier_join")        
