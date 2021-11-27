import config

highscore = 0
scr = 0

def show():
    fill(255)
    textSize(24)
    text("Highscore: " + str(highscore), 20, 70)
    text("Score: " + str(scr), 20, 40)

def update_highscore():
    if scr > highscore:
        with open(config.HIGHSCORE_FILE, "w") as file:
            file.write(str(scr))
