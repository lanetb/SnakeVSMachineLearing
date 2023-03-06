import pygame as pg
from snake import *
from food import Food

pg.init()
bounds = (600,600)
window = pg.display.set_mode(bounds)
pg.display.set_caption("Snake")
block_size = 20
snake = Snake(block_size, bounds)
food = Food(block_size,bounds)
font = pg.font.SysFont('comicsans',60, True)

run = True
while run:
    pg.time.delay(100)

    for event in  pg.event.get():
        if event.type == pg.QUIT:
            run = False

    snake.move()
    snake.check_for_food(food)
    window.fill((0,0,0))
    snake.draw(pg, window)
    food.draw(pg, window)
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

    if snake.check_bounds() == True or snake.check_tail_collision() == True:
        text = font.render('Game Over', True, (255,255,255))
        window.blit(text, (150,150))
        pg.display.update()
        pg.time.delay(1000)
        snake.respawn()
        food.respawn()