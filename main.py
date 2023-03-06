import pygame as pg
from snake import *

pg.init()
bounds = (300,300)
window = pg.display.set_mode(bounds)
pg.display.set_caption("Snake")
block_size = 20
snake = Snake(block_size, bounds)

run = True
while run:
    pg.time.delay(100)

    for event in  pg.event.get():
        if event.type == pg.QUIT:
            run = False

    snake.move()
    window.fill((0,0,0))
    snake.draw(pg, window)
    pg.display.flip()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
      snake.steer(Directions.LEFT)
    elif keys[pg.K_RIGHT]:
      snake.steer(Directions.RIGHT)
    elif keys[pg.K_UP]:
      snake.steer(Directions.UP)
    elif keys[pg.K_DOWN]:
      snake.steer(Directions.DOWN)