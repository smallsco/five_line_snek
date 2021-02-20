from enum import Enum
from pydantic import BaseModel
from typing import List, Optional


class Point(BaseModel):
    x: int
    y: int


class RuleSet(BaseModel):
    name: str
    version: str


class Game(BaseModel):
    id: str
    ruleset: RuleSet
    timeout: int


class Snake(BaseModel):
    id: str
    name: str
    health: int
    body: List[Point]
    latency: str
    head: Point
    length: int
    shout: str
    squad: Optional[str]
    masked: Optional[bool]


class Board(BaseModel):
    height: int
    width: int
    food: List[Point]
    hazards: List[Point]
    snakes: List[Snake]


class Request(BaseModel):
    game: Game
    turn: int
    board: Board
    you: Snake


class Direction(str, Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"


class MoveResponse(BaseModel):
    move: Direction
    shout: Optional[str] = None


class RootResponse(BaseModel):
    apiversion: str
    author: str
    color: str
    head: str
    tail: str
    version: str
