from abc import ABC, abstractmethod
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2

class Entities(Enum):
    HERO = 1
    ENEMY = 2

class GameState(Enum):
    PAUSE = 1
    RESUME = 2 
    QUIT = 3
