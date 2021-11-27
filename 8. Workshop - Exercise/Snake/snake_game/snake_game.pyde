import config
import snake
import food
import score
import os


def setup():
    size(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    frameRate(10)
    if os.path.exists(config.HIGHSCORE_FILE):
        with open(config.HIGHSCORE_FILE, "r") as file:
            score.highscore = int(file.read())
    else:
        highscore = 0
    
    food.pear_image = loadImage("pear.png")
    
def draw():
    background(0)
    snake.show()
    snake.move()
    food.show()
    score.show()
    
    if snake.touches_food():
        print("Mm, Yummy!")
        snake.eat_food()
        food.reset()
        score.scr +=1
        
    if snake.eats_self():
        print("Ouch! Game Over!")
        score.update_highscore()
        noLoop()
    

def keyPressed():
    if keyCode == UP and config.CURRENT_DIR != "down":
        config.CURRENT_DIR = "up"
    elif keyCode == DOWN and config.CURRENT_DIR != "up":
        config.CURRENT_DIR = "down"
    elif keyCode == LEFT and config.CURRENT_DIR != "right":
        config.CURRENT_DIR = "left"
    elif keyCode == RIGHT and config.CURRENT_DIR != "left":
        config.CURRENT_DIR = "right"
    
    
