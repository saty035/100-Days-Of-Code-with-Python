#Simple Analog Clock
#By saty035

import turtle
import time
wn=turtle.Screen()
wn.bgcolor('black')
wn.setup(width=600,height=600)
wn.title('Simple Analog Clock By @saty_035')
wn.tracer(0)

#creating drawing pen
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


#Brand
Pen=turtle.Turtle()
Pen.hideturtle()
Pen.speed(0)
Pen.color('cyan')
Pen.shape('square')
Pen.penup()
Pen.goto(0,85)
Pen.write("Meri Moony",align='center',font=("Courier",20,'italic'))




def draw_clock(h,m,s,pen):

    #clock face
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color('red')
    pen.pendown()
    pen.circle(210)

    #draw the line for hours
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(200)
        pen.pendown()
        pen.fd(-10)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    #draw hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color('blue')
    pen.setheading(90)
    angle=(h /12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(90)

    #draw minute hand
    pen.penup()
    pen.goto(0,0)
    pen.color('silver')
    pen.setheading(90)
    angle=(m /60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    #draw second hand
    pen.penup()
    pen.goto(0,0)
    pen.color('gold')
    pen.setheading(90)
    angle=(s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)


while True:
    h=int(time.strftime('%I'))
    m=int(time.strftime('%M'))
    s=int(time.strftime('%S'))


    draw_clock(h,m,s,pen)
    wn.update()

    time.sleep(1)

    pen.clear()

wn.mainloop()