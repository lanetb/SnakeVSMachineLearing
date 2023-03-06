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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      snake.steer(Direction.LEFT)
    elif keys[pygame.K_RIGHT]:
      snake.steer(Direction.RIGHT)
    elif keys[pygame.K_UP]:
      snake.steer(Direction.UP)
    elif keys[pygame.K_DOWN]:
      snake.steer(Direction.DOWN)