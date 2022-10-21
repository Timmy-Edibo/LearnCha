from fastapi import APIRouter, Form, status, HTTPException
from fastapi.responses import JSONResponse

from wonderwords import RandomSentence
from random_words import RandomWords

from ..Dictionary import cruds as dictionary_cruds
from random import randint

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

    generated_word =  RandomWords().random_word()
    response = dictionary_cruds.dictionary_text_to_speech(generated_word.lower())
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status_code":200,"response": response})


@router.post("/transcribe_alphabet")
async def transcribe_alphabet(alphabet: str = Form(..., max_length=1)):
    """"Enter an Alphabet to get a word converted to speech"""
    try:
        result =  RandomWords().random_word(alphabet.lower())
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Input an alphabet") from e
    return  result.capitalize()


@router.get("/transcribe_sentence")
async def transcribe_sentence():
    """"Endpoint that generate random sentences\n
     And then convert the word to speech"""
    return RandomSentence().sentence()
