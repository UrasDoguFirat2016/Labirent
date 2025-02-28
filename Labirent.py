import turtle
import time

screen = turtle.Screen()
screen.title("Labirent Oyunu")
screen.setup(700, 700)

başla = turtle.Turtle()
başla.shape("square")
başla.shapesize(27, 58)
başla.color("green")
başla.penup()
başla.goto(0, 0)
başla.pendown()

kaplumbik = turtle.Turtle()
kaplumbik.shape("turtle")
kaplumbik.color("green")
kaplumbik.penup()
kaplumbik.goto(-270, 260)

kalem = turtle.Turtle()
kalem.speed(0)
kalem.color("black")

def labirent_çiz(x, y):
    başla.speed(0)
    başla.goto(10000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000)
    başla.shapesize(1, 1)
    kalem.penup()
    kalem.goto(-300, 300)
    kalem.pendown()
    kalem.forward(600)
    kalem.right(90)
    kalem.forward(600)
    kalem.right(90)
    kalem.forward(600)
    kalem.right(90)
    kalem.forward(600)
    kalem.right(90)
    kalem.penup()
    kalem.goto(-300, 300)
    kalem.pendown()
    kalem.color("black")
    kalem.penup()
    kalem.goto(-300, 200)
    kalem.pendown()
    kalem.forward(100)
    kalem.penup()
    kalem.goto(-320, 200)
    kalem.pendown()
    kalem.forward(100)
    kalem.right(90)
    kalem.forward(500)
    kalem.penup()
    kalem.goto(-150, 0)
    kalem.pendown()
    kalem.left(180)
    kalem.forward(300)
    kalem.left(180)
    kalem.penup()
    kalem.goto(-150, 0)
    kalem.pendown()
    kalem.forward(235)
    kalem.left(90)
    kalem.forward(375)
    kalem.left(90)
    kalem.forward(475)
    kalem.left(90)
    kalem.forward(300)
    kalem.left(90)
    kalem.forward(400)
    kalem.left(90)
    kalem.forward(300)

def yukarı():
    kaplumbik.setheading(90)
    y = kaplumbik.ycor()
    y += 25
    if y > 275:
        y = 275
    kaplumbik.sety(y)
    kontrol_et()

def aşağı():
    kaplumbik.setheading(270)
    y = kaplumbik.ycor()
    y -= 25
    if y < -275:
        y = -275
    kaplumbik.sety(y)
    kontrol_et()

def sağa():
    kaplumbik.setheading(0)
    x = kaplumbik.xcor()
    x += 25
    if x > 275:
        x = 275
    kaplumbik.setx(x)
    kontrol_et()

def sola():
    kaplumbik.setheading(180)
    x = kaplumbik.xcor()
    x -= 25
    if x < -275:
        x = -275
    kaplumbik.setx(x)
    kontrol_et()

def kontrol_et():
    if kaplumbik.distance(kalem) < 10:
        kalem.hideturtle()
        kaplumbik.hideturtle()
        time.sleep(1)
        screen.bye()
    # Labirent çizgilerine değip değmediğini kontrol et
    if kalem.distance(kaplumbik) < 10:
        kalem.hideturtle()
        kaplumbik.hideturtle()
        time.sleep(1)
        screen.bye()

screen.listen()
screen.onkey(yukarı, "Up")
screen.onkey(aşağı, "Down")
screen.onkey(sağa, "Right")
screen.onkey(sola, "Left")
screen.onkey(screen.bye, ".")

kalem.hideturtle()
başla.onclick(labirent_çiz)

screen.mainloop()
