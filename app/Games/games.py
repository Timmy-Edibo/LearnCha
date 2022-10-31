from fastapi import APIRouter
from fastapi.responses import RedirectResponse

import os
from dotenv import load_dotenv


load_dotenv()

router = APIRouter(prefix="/games", tags=["Games"])

word_game = os.getenv("WORD_GAME")
alphabet_game = os.getenv("ALPHABET_GAME")
game_room = os.getenv("GAMES_ROOM")
blockly_games =os.getenv("BLOCKLY_GAMES")
game_room_two = os.getenv("GAMES_ROOM_TWO")
swap_game = os.getenv("SWAP_GAME")
Floppy_bird = os.getenv("FLOPPY_BIRD")
forest_game = os.getenv("FOREST_GAME")


@router.get("/wordle_game")
def game_one():    
    return RedirectResponse(word_game)

@router.get("/alphabet_game")
def game_two():    
    return RedirectResponse(alphabet_game)

@router.get("/game_room")
def game_three():    
    return RedirectResponse(game_room)

@router.get("/blockly_games")
def game_three():    
    return RedirectResponse(blockly_games)

@router.get("/bounce")
def game_four():    
    return RedirectResponse(game_room_two)

@router.get("/swap")
def game_five():    
    return RedirectResponse(swap_game)

@router.get("/floppy_bird")
def game_six():    
    return RedirectResponse(Floppy_bird)

@router.get("/forest_game")
def game_seven():    
    return RedirectResponse(forest_game)