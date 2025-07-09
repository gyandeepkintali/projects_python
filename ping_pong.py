from turtle import Screen, Turtle
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")

screen.tracer(0)

r_paddle = Turtle()
r_paddle.shape("square")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5, stretch_len=1)
r_paddle.penup()
r_paddle.goto(350, 0)

l_paddle = Turtle()
l_paddle.shape("square")
l_paddle.color("white")
l_paddle.shapesize(stretch_wid=5, stretch_len=1)
l_paddle.penup()
l_paddle.goto(-350, 0)

ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

score_a = 0
score_b = 0
scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)

def update_score():
    scoreboard.clear()
    scoreboard.write(f"{score_a} : {score_b}", align="center", font=("Courier", 24, "normal"))

def reset_ball():
    ball.goto(0, 0)
    ball.dx *= -1

def r_paddle_up():
    new_y = r_paddle.ycor() + 20
    r_paddle.goto(r_paddle.xcor(), new_y)

def r_paddle_down():
    new_y = r_paddle.ycor() - 20
    r_paddle.goto(r_paddle.xcor(), new_y)

def l_paddle_up():
    new_y = l_paddle.ycor() + 20
    l_paddle.goto(l_paddle.xcor(), new_y)

def l_paddle_down():
    new_y = l_paddle.ycor() - 20
    l_paddle.goto(l_paddle.xcor(), new_y)

screen.listen()
screen.onkey(r_paddle_up, "Up")
screen.onkey(r_paddle_down, "Down")
screen.onkey(l_paddle_up, "w")
screen.onkey(l_paddle_down, "s")

game_is_on = True
update_score()  
while game_is_on:
    screen.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    
    if ball.xcor() > 390:  
        score_a += 1
        update_score()
        reset_ball()
    
    if ball.xcor() < -390:  
        score_b += 1
        update_score()
        reset_ball()
    
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (r_paddle.ycor() + 50 > ball.ycor() > r_paddle.ycor() - 50):
        ball.dx *= -1
    
    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (l_paddle.ycor() + 50 > ball.ycor() > l_paddle.ycor() - 50):
        ball.dx *= -1

screen.exitonclick()

