import pygame as pg
from snake import *
from food import Food

pg.init()
bounds = (1200,600)
window = pg.display.set_mode(bounds)
pg.display.set_caption("Snake")
block_size = 20
snake = Snake(block_size, bounds, [(20,300)], (0,255,0), Directions.RIGHT)
snake2 = Snake(block_size, bounds, [(1160,300)], (0,0,255), Directions.LEFT)
food = Food(block_size, bounds)

font = pg.font.SysFont('comicsans',60, True)

run = True
while run:
    pg.time.delay(100)

    for event in  pg.event.get():
        if event.type == pg.QUIT:
            run = False

    snake.move()
    snake2.move()
    print(snake2.body[-1])
    snake.check_for_food(food)
    snake2.check_for_food(food)
    window.fill((0,0,0))
    snake.draw(pg, window)
    snake2.draw(pg, window)
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
    
    keys2 = pg.key.get_pressed()
    if keys2[pg.K_a]:
      snake2.steer(Directions.LEFT)
    elif keys2[pg.K_d]:
      snake2.steer(Directions.RIGHT)
    elif keys2[pg.K_w]:
      snake2.steer(Directions.UP)
    elif keys2[pg.K_s]:
      snake2.steer(Directions.DOWN)

    if snake.check_bounds() == True or snake.check_tail_collision() == True:
        text = font.render('Player 1 Wins', True, (255,255,255))
        window.blit(text, (400,200))
        pg.display.update()
        pg.time.delay(1000)
        snake.respawn((20,300), Directions.RIGHT)
        snake2.respawn((1180,300), Directions.LEFT)
        food.respawn()

    if snake2.check_bounds() == True or snake2.check_tail_collision() == True:
        text = font.render('Player 2 Wins', True, (255,255,255))
        window.blit(text, (400, 200))
        pg.display.update()
        pg.time.delay(1000)
        snake.respawn((20,300), Directions.RIGHT)
        snake2.respawn((1180,300), Directions.LEFT)
        food.respawn()