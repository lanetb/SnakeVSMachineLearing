import pygame as pg
from enum import Enum

pg.init()
bounds = (300,300)
window = pg.display.set_mode(bounds)
pg.display.set_caption("Snake")

class Directions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Snake:
    length = None
    direction = None
    body = None
    block_size = None
    color = (0,255,0)
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.respawn()

    def respawn(self):
        self.length = 1
        self.direction = Directions.RIGHT
        self.body = [(20,20)]

