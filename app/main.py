from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn


from .Transcriber import transcriber
from .Games import games
from .Dictionary import dictionary
from .Do_it_yourself import do_it_yourself
from .Books import book_reader
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="LearnCha", 
            description="""Welcome to learnCha. An online gaming platform developed for kids as an attempt to
                            provide equitable sustainability via educational resource and games, making learning
                             fun and interesting at the same time.""",
            version="1.0.0")


app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["set-cookie"],
)

@app.get("/", tags=["Home"])
def home():
    return "Welcome to learnCha. An online gaming platform developed for kids as an attempt to provide equitable sustainability via educational resource and games, making learning fun and interesting at the same time."

app.include_router(games.router)
app.include_router(transcriber.router)
app.include_router(dictionary.router)
app.include_router(do_it_yourself.router)
app.include_router(book_reader.router)




if __name__=="__main__":
    uvicorn.run(app.main, port=8000, host="localhost")

