import turtle
import time

wn = turtle.Screen()
wn.title("")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue") 
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# Ball 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("blue") 
ball2.penup()
ball2.goto(10, 20)
ball2.dx = -5
ball2.dy = 5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y) 

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y) 
 
def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# Main game loop
while True:
    wn.update()

    # Move the ball   
    ball.setx(ball.xcor() + ball.dx)   
    ball.sety(ball.ycor() + ball.dy)
    ball2.setx(ball2.xcor() + ball2.dx)   
    ball2.sety(ball2.ycor() + ball2.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0) 
        ball.dx *= -1 
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier",  24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0) 
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

 # Border checking
    if ball2.ycor() > 290:
        ball2.sety(290)
        ball2.dy *= -1

    if ball2.ycor() < -290:
        ball2.sety(-290)
        ball2.dy *= -1

    if ball2.xcor() > 390:
        ball2.goto(0, 0) 
        ball2.dx *= -1 
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier",  24, "normal"))


    if ball2.xcor() < -390:
        ball2.goto(0, 0) 
        ball2.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



    # paddle and ball collisions
    if (ball2.xcor() > 340 and ball2.xcor() < 350) and (ball2.ycor() < paddle_b.ycor() + 40 and ball2.ycor() > paddle_b.ycor() -40):
        ball2.setx(340)
        ball2.dx *= -1

    if (ball2.xcor() < -340 and ball2.xcor() > -350) and (ball2.ycor() < paddle_a.ycor() + 40 and ball2.ycor() > paddle_a.ycor() -40):
        ball2.setx(-340)
        ball2.dx *= -1

    if (score_a == 10):
        pen.clear()
        pen.goto(0, 50)
        wn.clear()
        wn.bgcolor("black")

        pen.write("Player A: WINS!".format(score_a), align="center", font=("Courier", 50, "normal"))
        while True:
            time.sleep(5)
            exit(0)
        
    if (score_b == 10):
        pen.clear()
        pen.goto(0, 50)
        wn.clear()
        wn.bgcolor("black")

        pen.write("Player B: WINS!".format(score_b), align="center", font=("Courier", 50, "normal"))
        while True:
            time.sleep(5)
            exit(0)







