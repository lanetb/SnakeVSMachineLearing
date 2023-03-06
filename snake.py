from enum import Enum

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

    def draw(self, game, window):
        for segment in self.body:
            game.draw.rect(window, self.color, (segment[0],segment[1],self.block_size, self.block_size))
    
    def move(self):
        curr_head = self.body[-1]
        if self.direction == Directions.DOWN:
            next_head = (curr_head[0], curr_head[1] + self.block_size)
            self.body.append(next_head)
        elif self.direction == Directions.UP:
            next_head = (curr_head[0], curr_head[1] - self.block_size)
            self.body.append(next_head)
        elif self.direction == Directions.RIGHT:
            next_head = (curr_head[0] + self.block_size, curr_head[1])
            self.body.append(next_head)
        elif self.direction == Directions.LEFT:
            next_head = (curr_head[0] - self.block_size, curr_head[1])
        self.body.append(next_head)

        if self.length < len(self.body):
            self.body.pop(0)

    def steer(self, direction):
        if self.direction == Directions.DOWN and direction != Directions.UP:
          self.direction = direction
        elif self.direction == Directions.UP and direction != Directions.DOWN:
          self.direction = direction
        elif self.direction == Directions.LEFT and direction != Directions.RIGHT:
          self.direction = direction
        elif self.direction == Directions.RIGHT and direction != Directions.LEFT:
          self.direction = direction