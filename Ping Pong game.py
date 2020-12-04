import turtle

# window
wind = turtle.Screen()
wind.title('Ping Pong game')
wind.bgcolor('black')
wind.setup(width=800, height=600)
wind.tracer(0)

# first square
square1 = turtle.Turtle()
square1.speed(0)
square1.shape("square")
square1.color('blue')
square1.shapesize(stretch_wid=5, stretch_len=1)
square1.penup()
square1.goto(-350, 0)

# second square
square2 = turtle.Turtle()
square2.speed(0)
square2.shape("square")
square2.color('red')
square2.shapesize(stretch_wid=5, stretch_len=1)
square2.penup()
square2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write('Player1: 0 Player2: 0', align='center', font=('Courier',24,'normal'))

#functions
def square1_up():
    y = square1.ycor()
    y += 20
    square1.sety(y)

def square1_down():
    y = square1.ycor()
    y -= 20
    square1.sety(y)

def square2_up():
    y = square2.ycor()
    y += 20
    square2.sety(y)

def square2_down():
    y = square2.ycor()
    y -= 20
    square2.sety(y)

#Keybord bindings
wind.listen()
wind.onkeypress(square1_up, 'w')
wind.onkeypress(square1_down, 's')
wind.onkeypress(square2_up, 'Up')
wind.onkeypress(square2_down, 'Down')
#main game loop
while True:
    wind.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write('Player1: {} Player2: {}'.format(score1, score2), align='center', font=('Courier',24,'normal'))
    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write('Player1: {} Player2: {}'.format(score1, score2), align='center', font=('Courier',24,'normal'))

    # ball and square collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < square2.ycor() + 40 and ball.ycor() > square2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < square1.ycor() + 40 and ball.ycor() > square1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
