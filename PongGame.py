import turtle
import winsound

# setting game window
wn = turtle.Screen()
wn.title("Pong By Gyanendra")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scores
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.color("white")
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.color("white")
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.color("white")
ball.speed(0)
ball.shape('circle')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 260)
pen.write(f"Player A : {score_a}  Player B : {score_b}", align="center",
          font=("Courier", 24, "normal"))

# Functions for different operations


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "l")

# Main game loop


while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border Chacking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a += 1
        pen.clear()
        pen.write(f"Player A : {score_a}  Player B : {score_b}", align="center",
                  font=("Courier", 24, "normal"))
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        score_b += 1
        pen.clear()
        pen.write(f"Player A : {score_a}  Player B : {score_b}", align="center",
                  font=("Courier", 24, "normal"))
        ball.dx *= -1

    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_b.ycor()-50 < ball.ycor() and ball.ycor() < paddle_b.ycor()+50):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < - 340 and ball.xcor() > - 350) and (paddle_a.ycor()-50 < ball.ycor() and ball.ycor() < paddle_a.ycor()+50):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1
