#this is a clock
import time
import turtle
wn = turtle.Screen()
wn.bgcolor('white')
wn.setup(width=500, height=500)
wn.title("Clock")
wn.tracer(0)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):
    
    #clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color('black')
    pen.pendown()
    pen.circle(210)


    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    #hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color("black")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    #minute hand
    pen.penup()
    pen.goto(0,0)
    pen.color("grey")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)
    
    #second hand
    pen.penup()
    pen.goto(0,0)
    pen.color("gold")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)


while True: 
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%s"))


    draw_clock(h, m, s, pen)
    wn.update()
    time.sleep(1)

    pen.clear()


wn.mainloop()