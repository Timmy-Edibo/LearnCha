from fastapi import APIRouter
from fastapi import Form
from app.Dictionary.cruds import dictionary

router = APIRouter(prefix="/dictionary", tags=["Dictionary"])

@router.post("/dictionary")
def dictionaryy(word: str = Form(Ellipsis)):
    """ Post request \n
    Dictionary Endpoint
    """
    return dictionary(word=word)
