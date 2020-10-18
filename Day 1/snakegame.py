#snake game with python



import turtle    #consider it is as drawing board
import time
import random

delay=0.1
#score
score=0
high_score=0



#setting up the screen

wn=turtle.Screen()
wn.title("Snake game\n")
wn.bgcolor('pink')  #background color
wn.setup(width=600,height=600)  #setting the dimensions
wn.tracer(0)    #turning off the animation

# snake head

head=turtle.Turtle()   #lets you command a turtle to draw all over it
head=turtle.Turtle()   
head.speed(0)
head.shape('square')
head.color('blue')
head.penup()    # so it doesn't draw anything
head.goto(0,0)
head.direction='stop'

#snake food

food=turtle.Turtle()   #lets you command a turtle to draw all over it
food=turtle.Turtle()   
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()    # so it doesn't draw anything
food.goto(0,100)

segments=[]

#pen

pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)

pen.write("Score: 0  High Score: 0",align='center',font=("Courier",24,'normal'))

#functions

def go_up():
    if head.direction !='down':
        head.direction='up'

def go_down():
    if head.direction !='up':
        head.direction='down'

def go_left():
    if head.direction !='right':
        head.direction='left'

def go_right():
    if head.direction !='left':
        head.direction='right'

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)

    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)

    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)

    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)

#keyboards blinding

wn.listen()
wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_left,'a')
wn.onkeypress(go_right,'d')


#main game loop

while True:
    wn.update()

    #check for collison with the boundry
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'

        #hide the segment
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segment list
        segments.clear()

        #reset the delay
        delay=0.1

        #update score
        score=0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align='center',font=("Courier",24,"normal"))

    #for collision with food

    if head.distance(food)<20:        
        #move the food to a random point

        x= random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)

        #add a segment

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        #in turtle module as the snake get longer the writing time will also be longer
        delay-=0.001
        #increase thr score
        score+=10

        if score>high_score:
            high_score=score

        #update score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align='center',font=("Courier",24,"normal"))



    #move the end segments in reverse order

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to head

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


    move()

    #check for head collision

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'

            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            
            #clear the segments
            segments.clear()

            #reset the delay
            delay=0.1

            #update score
            score=0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score),align='center',font=("Courier",24,"normal"))

    time.sleep(delay)  #for delaying

wn.mainloop() # keep the window open for us
