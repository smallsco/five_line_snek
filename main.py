import random
import uvicorn
from fastapi import FastAPI
from models import MoveResponse, Request, RootResponse

app = FastAPI(
    title="Challenge Snek",
    description="Five Line Challenge Snek",
    version="1.0.0",
    redoc_url=None
)


@app.get("/", response_model=RootResponse)
async def root():
    return {
        "apiversion": "1",
        "author": "smallsco",
        "color": "#36688D",
        "head": "snowman",
        "tail": "bonhomme",
        "version": app.version
    }


@app.post("/start")
async def start(r: Request):
    return


@app.post("/move", response_model=MoveResponse)
async def move(r: Request):
    # Line 1: find enemy
    s=r.board.snakes; e=0 if len(s)==1 else s[0] if s[0].id!=r.you.id else s[1]
    # Line 2: decide if we want to go for enemy or food
    m=[]; a=r.you.head; h=r.you.health; g='s' if h>40 and len(s)>1 else 'f'
    # Line 3: store target position
    t=e.head if g=='s' else r.board.food[0]; dx=t.x-a.x; dy=t.y-a.y
    # Line 4: get direction to target
    m.append('right') if dx>0 else m.append('left')
    # Line 5: return move
    m.append('up') if dy>0 else m.append('down');return{"move":random.choice(m)}


@app.post("/end")
async def end(r: Request):
    return


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
