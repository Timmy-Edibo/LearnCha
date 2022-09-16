from fastapi import HTTPException, status
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()


dictionary_url = os.getenv("DICTIONARY_URL")

def dictionary(word: str):
    try:
        res = requests.get(f"{dictionary_url}{word}").json()

        word = res[0]["word"]
        audio = res[0]["phonetics"][0]["audio"]
        definitions = []

        meaning_ = [x["definitions"] for x in res[0]["meanings"]]
        for x in meaning_:
            ans = [x["definition"] for x in x]
            definitions.append(ans)

        res = { "word":word, "sound" :audio, "definitions": definitions}
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Word not found in the dictionary" ) from e 
    return res





















# meaning_all =  res[0]["meanings"][0]["definitions"]
# meaning_noun = [x["definition"] for x in meaning_all]