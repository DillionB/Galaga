import turtle
import time
import os

turtle.delay(0)

SHIP = "ship.gif"
BAD_GUY_1 = "bad_guy_red.gif"
BAD_GUY_RED = "bad_guy_red.gif"
BAD_GUY_BLUE = "bad_guy_blue.gif"
EXPLOSION_1 = "explosion_1.gif"
EXPLOSION_2 = "explosion_2.gif"
EXPLOSION_3 = "explosion_3.gif"

BLACK = "black"
WHITE = "white"
RED = "red"
LEFT = "Left"
RIGHT = "Right"
SPACE = "space"
CIRCLE = "circle"
CENTER = "center"
SCORE = "SCORE"
HIGH_SCORE = "HIGH SCORE"
COURIER = "courier"
BOLD = "bold"

width = 960
height = 540

screen = turtle.Screen()
screen.setup(width, height)
screen.bgcolor(BLACK)

screen.addshape(SHIP)
screen.addshape(BAD_GUY_1)
screen.addshape(BAD_GUY_RED)
screen.addshape(BAD_GUY_BLUE)
screen.addshape(EXPLOSION_1)
screen.addshape(EXPLOSION_2)
screen.addshape(EXPLOSION_3)

ship = turtle.Turtle()
ship.shape(SHIP)
ship.up()
ship.goto(0, -200)

pos_x = -400
enemies = []
score = 0
high_score = 0

for i in range(3):
    life = turtle.Turtle()
    life.shape(SHIP)
    life.up()
    life.goto(pos_x, -230)
    pos_x += 50

style = (COURIER, 20, BOLD)
score_title = turtle.Turtle()
score_title.hideturtle()
score_title.up()
score_title.goto(-200, 200)
score_title.color(WHITE)
score_title.write(SCORE, font=style, align=CENTER)

high_score_title = turtle.Turtle()
high_score_title.hideturtle()
high_score_title.up()
high_score_title.color(WHITE)
high_score_title.goto(200, 200)
high_score_title.write(HIGH_SCORE, font=style, align=CENTER)

score_text = turtle.Turtle()
score_text.hideturtle()
score_text.up()
score_text.color(RED)
score_text.goto(-200, 170)
score_text.write(str(0), font=style, align=CENTER)

high_score_text = turtle.Turtle()
high_score_text.hideturtle()
high_score_text.up()
high_score_text.color(RED)
high_score_text.goto(200, 170)
high_score_text.write(str(0), font=style, align=CENTER)


def add_enemy(enemy):
    global enemies
    enemies.append(enemy)


pos_x = -100
pos_y = 100
for i in range(4):
    bad_guy = turtle.Turtle()
    bad_guy.up()
    bad_guy.goto(pos_x, pos_y)
    bad_guy.shape(BAD_GUY_1)
    add_enemy(bad_guy)
    pos_x += 50

pos_x = -200
pos_y = 50
for i in range(8):
    bad_guy_red = turtle.Turtle()
    bad_guy_red.up()
    bad_guy_red.goto(pos_x, pos_y)
    bad_guy_red.shape(BAD_GUY_RED)
    add_enemy(bad_guy_red)
    pos_x += 50

pos_x = -200
pos_y = 20
for i in range(8):
    bad_guy_red = turtle.Turtle()
    bad_guy_red.up()
    bad_guy_red.goto(pos_x, pos_y)
    bad_guy_red.shape(BAD_GUY_RED)
    add_enemy(bad_guy_red)
    pos_x += 50

pos_x = -250
pos_y = -10
for i in range(10):
    bad_guy_blue = turtle.Turtle()
    bad_guy_blue.up()
    bad_guy_blue.goto(pos_x, pos_y)
    bad_guy_blue.shape(BAD_GUY_BLUE)
    add_enemy(bad_guy_blue)
    pos_x += 50

pos_x = -250
pos_y = -40
for i in range(10):
    bad_guy_blue = turtle.Turtle()
    bad_guy_blue.up()
    bad_guy_blue.goto(pos_x, pos_y)
    bad_guy_blue.shape(BAD_GUY_BLUE)
    add_enemy(bad_guy_blue)
    pos_x += 50


def left():
    ship.backward(50)


def right():
    ship.forward(50)


def shoot():
    shot = turtle.Turtle()
    shot.up()
    shot.goto(ship.pos())
    shot.color(WHITE)
    shot.shape(CIRCLE)
    shot.turtlesize(0.5)
    turtle.delay(10)
    shot.speed(1.5)
    shot.left(90)
    for i in range(60):
        shot.forward(12)
        for j in range(len(enemies)):
            if is_collided_with(shot, enemies[j]):
                show_explosion(enemies[j].position())
                enemies[j].hideturtle()
                shot.hideturtle()
                increase_score(j)
                del enemies[j]
                return


def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10


def show_explosion(position):
    explosion = turtle.Turtle()
    explosion.goto(position)
    explosion.up()
    explosion.shape(EXPLOSION_1)
    time.sleep(0.1)
    explosion.shape(EXPLOSION_2)
    time.sleep(0.1)
    explosion.shape(EXPLOSION_3)
    time.sleep(0.1)
    explosion.hideturtle()
    del explosion


def increase_score(index):
    global score
    if index < 4:
        score += 150
    elif index < 16:
        score += 80
    elif index < 40:
        score += 50
    score_text.clear()
    score_text.color(RED)
    score_text.goto(-200, 170)
    score_text.write(str(score), font=style, align=CENTER)
    increase_high_score()


def increase_high_score():
    global score
    global high_score
    if(not os.path.exists("highscore.txt")):
        f = open("highscore.txt", "w")
        f.close()
    f = open("highscore.txt", "r+")
    current = f.read()
    if current == "":
        current = 0
    else:
        current = int(current)

    if current > score:
        high_score = current
    else:
        high_score = score
        f.seek(0)
        f.truncate()
        f.write(str(score))
    f.close()
    high_score_text.clear()
    high_score_text.color(RED)
    high_score_text.goto(200, 170)
    high_score_text.write(str(high_score), font=style, align=CENTER)


screen.onkey(left, LEFT)
screen.onkey(right, RIGHT)
screen.onkey(shoot, SPACE)

increase_high_score()
screen.listen()
turtle.mainloop()
