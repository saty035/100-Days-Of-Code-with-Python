# Simple Ping Pong 
#By saty035


import turtle
import winsound     #for windows  'os' for macs

wn=turtle.Screen()
wn.title("Ping Pong By saty035")
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#score
score_a=0
score_b=0


#paddle A
paddle_a=turtle.Turtle()    #turtle object
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('red')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()  #stop the drawing
paddle_a.goto(-350,0)


#paddle B
paddle_b=turtle.Turtle()    #turtle object
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()  #stop the drawing
paddle_b.goto(350,0)


#Ball
ball=turtle.Turtle()    #turtle object
ball.speed(0)
ball.shape('circle')
ball.color('gold')
ball.penup()  #stop the drawing
ball.goto(0,0)

ball.dx=.2  #our ball move by 2 pixel everytime
ball.dy=-.2  #set the value according to your system

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('blue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier",24,"italic"))

#function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_dowm():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_dowm():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_dowm,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_dowm,'Down')


#main loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1  #reverse the direction the ball
       
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1  #reverse the direction the ball

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a+=1
        winsound.PlaySound('yummy.wav',winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"italic"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b+=1
        winsound.PlaySound('yummy.wav',winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"italic"))

    #paddle and all collisions
    if (ball.xcor()>340 and ball.xcor()<350) and ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40:
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()<-340 and ball.xcor()>-350) and ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_b.ycor()-40:
        ball.setx(-340)
        ball.dx *= -1



