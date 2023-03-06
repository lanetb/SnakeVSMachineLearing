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

    def __init__(self, block_size, bounds, body, color, direction):
        self.block_size = block_size
        self.bounds = bounds
        self.body = body
        self.color = color
        self.respawn(body, direction)

    def respawn(self, body, direction):
        self.length = 1
        self.direction = direction
        self.body = body

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

    def eat(self):
        self.length += 1

    def check_for_food(self, food):
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.eat()
            food.respawn()

    def check_tail_collision(self):
        head = self.body[-1]
        has_eaten_tail = False

        for i in range(len(self.body) - 1):
          segment = self.body[i]
          if head[0] == segment[0] and head[1] == segment[1]:
            has_eaten_tail = True

        return has_eaten_tail
    
    def check_bounds(self):
        head = self.body[-1]
        if head[0] >= self.bounds[0]:
          return True
        if head[1] >= self.bounds[1]:
          return True

        if head[0] < 0:
            return True
        if head[1] < 0:
            return True

        return False
