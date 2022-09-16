from fastapi import APIRouter, Form

from wonderwords import RandomSentence
from random_words import RandomWords

from random import randint
import requests
import os

router = APIRouter(prefix="/transcribe", tags=["Transcriber"])


def num_generator():
    return randint(1000056, 9999999)

@router.get("/transcribe_numbers")
def transcribe_numbers():
    """"Endpoint that generate random numbers\n
     It should then convert the number to speech"""

    return num_generator()


@router.get("/transcribe_words")
async def transcribe_words():
    """"Endpoint that generate random words\n
     It should then convert the word to speech"""

    r =  RandomWords()
    return r.random_word()



@router.post("/transcribe_alphabet")
async def transcribe_alphabet(alphabet: str = Form(..., max_length=1)):
    """"Enter an Alphabet to get a word converted to speech"""

    r =  RandomWords()
    return r.random_word(alphabet)    

@router.get("/transcribe_sentence")
async def transcribe_sentence():
    """"Endpoint that generate random sentences\n
     And then convert the word to speech"""
    r = RandomSentence()
    return r.sentence()

