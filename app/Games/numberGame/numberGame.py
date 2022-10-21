from asyncore import write
from distutils.file_util import write_file
from textwrap import indent
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/games", tags=["Number Game"])
import random



@router.get("/level_one")
def level_one():
    """ Level: Level one \n
    Difficulty level: Easy \n
    It Generates random numbers from 1 to 99
    """
    return random.randrange(1, 99)


@router.get("/level_two")
def level_two():
    """ Level: Level two \n
    Difficulty level: Easy \n
    It Generates random numbers from 100 to 999
    """
    return random.randrange(100, 999)


@router.get("/level_three")
def level_three():
    """ Level: Level three \n
    Difficulty level: Easy \n
    It Generates random numbers from 1000 to 9999
    """
    return random.randrange(1000, 9999)

@router.get("/level_four")
def level_four():
    """ Level: Level four \n
    Difficulty level: Intermediate \n
    It Generates random numbers from 10000 to 99999
    """
    return random.randrange(10000, 99999) 
   

@router.get("/level_five")
def level_five():
    """ Level: Level five \n
    Difficulty level: Intermediate \n
    It Generates random numbers from 100000 to 999999
    """
    return random.randrange(100000, 999999) 
   

@router.get("/level_six")
def level_six():
    """ Level: Level six \n
    Difficulty level: Intermediate \n
    It Generates random numbers from 1000000 to 9999999
    """
    return random.randrange(1000000, 9999999)  
  

@router.get("/level_seven")
def level_seven():
    """ Level: Level Seven \n
    Difficulty level: Hard \n
    It Generates random numbers from 10000000 to 99999999
    """
    return random.randrange(10000000, 99999999)  


@router.get("/level_eight")
def level_eight():
    """ Level: Level eight \n
    Difficulty level: Hard \n
    It Generates random numbers from 100000000 to 999999999
    """
    return random.randrange(100000000, 999999999)   

@router.get("/level_nine")
def level_nine():
    """ Level: Level nine \n
    Difficulty level: Hard \n
    It Generates random numbers from 1000000000 to 9999999999
    """
    return random.randrange(1000000000, 9999999999)
   

@router.get("/level_ten")
def level_ten():
    """ Level: Level ten \n
    Difficulty level: Hard \n
    It Generates random numbers from 10000000000 to 99999999999
    """
    return random.randrange(10000000000, 99999999999)   

@router.get("/level_eleven")
def level_eleven():
    """ Level: Level Eleven \n
    Difficulty level: Hard \n
    It Generates random numbers from 10000000000 to 99999999999
    """
    return random.randrange(100000000000, 999999999999)  


@router.get("/level_twelve")
def level_twelve():
    """ Level: Level twelve \n
    Difficulty level: Hard \n
    It Generates random numbers from 10000000000 to 99999999999
    """
    return random.randrange(1000000000000, 9999999999999)  


@router.get("/level_thirteen")
def level_thirteen():
    """ Level: Level Thirteen \n
    Difficulty level: Hard \n
    It Generates random numbers from 10000000000 to 99999999999
    """
    return random.randrange(10000000000000, 99999999999999)  



@router.get("/level_Fourteen")
def level_fourteen():
    """ Level: Level Fourteen \n
    Difficulty level: Hard \n
    It Generates random numbers from 10000000000 to 99999999999
    """
    return random.randrange(10000000000000, 99999999999999)  


@router.get("/level_Fifteen")
def level_fifteen():
    """ Level: Level Fifteen \n
    Difficulty level: Hard \n
    It Generates random numbers from 10000000000 to 99999999999
    """
    return random.randrange(10000000000000, 99999999999999)  


@router.get("/level_Sixteen")
def level_sixteen():
    """ Level: Level Sixteen \n
    Difficulty level: Hard \n
    It Generates random numbers from 10000000000 to 99999999999
    """
    return  random.randrange(100000000000000, 999999999999999)  


@router.get("/level_Seventeen")
def level_seventeen():
    """ Level: Level Seventeen \n
    Difficulty level: Hard \n
    It Generates random numbers from 1000000000000000 to 9999999999999999
    """
    return random.randrange(1000000000000000, 9999999999999999)  







