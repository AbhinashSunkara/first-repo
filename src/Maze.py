import turtle
import time
import random
from tkinter import *

# Player color control window
root = Tk()
root.title("Control")
root.config(background="black")
root.geometry("250x250")

life = 2
sc = 0
hs = 0

# Players Gifs registering (fixed backslashes)
turtle.register_shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\pink.gif")
turtle.register_shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\pink1.gif")
turtle.register_shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\blue.gif")
turtle.register_shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\blue1.gif")
turtle.register_shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\red.gif")
turtle.register_shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\red1.gif")

# Game play window
s = turtle.Screen()
s.bgcolor("black")
s.bgpic(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\bgpic.gif")
s.title("Maize Stealer")
s.tracer(0)
s.setup(width=700, height=700)

k = turtle.Turtle()
k.color("white")
k.width(3)

# Player object
a = turtle.Turtle()
a.pensize(0)
a.color("orange")
a.shapesize(0.9, 0.9, 0.9)
a.shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\blue.gif")
a.direction = "stop"
a.goto(0, 0)
a.speed(0)  # Set initial speed to 0 for consistent movement
a.penup()

# Control the movement speed
move_step = 5  # Define the step size for each movement
delay = 0.1  # Delay between each frame update to control overall game speed

def red():
    a.shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\red.gif")

def blue():
    a.shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\blue.gif")

def pink():
    a.shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\pink.gif")

def exit():
    turtle.Screen().bye()
    root.destroy()

def lock():
    a.goto(0, 0)
    x = random.randint(-235, 235)
    y = random.randint(-235, 235)
    food.goto(x, y)

# Buttons for player color
Label(root, text="Select Player Color : ", bg="black", fg="white", font="verdana 12 bold italic").place(relx=0.5, rely=0.3, anchor=CENTER)

Button(root, text="red", command=red, bg="red", fg="black", font="verdana 12 bold").place(relx=0.2, rely=0.5, anchor=CENTER)

Button(root, text="blue", command=blue, bg="light blue", fg="black", font="verdana 12 bold").place(relx=0.5, rely=0.5, anchor=CENTER)

Button(root, text="pink", command=pink, bg="pink", fg="black", font="verdana 12 bold").place(relx=0.8, rely=0.5, anchor=CENTER)

Button(root, text="Exit", command=exit, bg="gold", fg="black", font="verdana 12 bold").place(relx=0.7, rely=0.7, anchor=CENTER)

Button(root, text="Lock!", command=lock, bg="white", fg="black", font="verdana 12 bold").place(relx=0.35, rely=0.7, anchor=CENTER)

# Food object
food = turtle.Turtle()
food.penup()
food.width(1)
shap = random.choice(["circle", "square"])
food.pensize(0)
food.shape("circle")
food.shapesize(0.7, 0.7, 0.7)
food.color("gold")
food.penup()
food.goto(50, 0)
food.penup()

# Score-Board object
score = turtle.Turtle()
score.penup()
score.speed(50)
score.color("gold")
score.pensize(0)
score.goto(0, 300)
score.write("Score : 0 High Score : {} Life : {}".format(hs, life), align="center", font=("candra", 16, "bold"))
score.hideturtle()
score.penup()

# Player direction control
def goup():
    a.direction = "up"

def godown():
    a.direction = "down"

def goright():
    a.direction = "right"

def goleft():
    a.direction = "left"

def stop():
    a.direction = "stop"

def move():
    if a.direction == "down":
        y = a.ycor()
        a.sety(y - move_step)
    if a.direction == "up":
        y = a.ycor()
        a.sety(y + move_step)
    if a.direction == "stop":
        y = a.ycor()
        a.sety(y)

    if a.direction == "right":
        x = a.xcor()
        a.setx(x + move_step)

    if a.direction == "left":
        x = a.xcor()
        a.setx(x - move_step)

    if a.direction == "right":
        x = a.xcor()
        if a.shape() == r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\red1.gif":
            a.shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\red.gif")
        if a.shape() == r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\blue1.gif":
            a.shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\blue.gif")
        if a.shape() == r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\pink1.gif":
            a.shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\pink.gif")
        a.setx(x + move_step)

    if a.direction == "left":
        x = a.xcor()
        if a.shape() == r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\red.gif":
            a.shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\red1.gif")
        if a.shape() == r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\pink.gif":
            a.shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\pink1.gif")
        if a.shape() == r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\blue.gif":
            a.shape(r"C:\Users\abhis\OneDrive\Desktop\MazeStealer\src\blue1.gif")
        a.setx(x - move_step)

s.listen()

# Keys using for player direction
s.onkeypress(goup, "Up")
s.onkeypress(godown, "Down")
s.onkeypress(goleft, "Left")
s.onkeypress(goright, "Right")
s.onkeypress(stop, "p")

# Outline for game space and blocks in game
k.speed(500)
k.penup()
k.goto(-248, 250)
k.penup()
k.width(5)
k.color("antiquewhite1")
for i in range(4):
    k.pendown()
    k.forward(493)
    k.right(90)
    k.penup()
k.penup()
k.goto(-210, 210)
k.pendown()
k.forward(420)
k.penup()

k.goto(-210, -210)
k.pendown()
k.forward(420)
k.penup()

k.goto(-100, 170)
k.pendown()
k.width(7)
k.color("red")
k.forward(210)
k.penup()

k.goto(-200, -120)
h = turtle.Turtle()
h.speed(100)
h.penup()
h.shapesize(3, 3, 3)
h.color("light blue")
h.shape("square")
h.goto(-160, -150)
h.penup()

l = turtle.Turtle()
l.speed(100)
l.penup()
l.shapesize(3, 3, 3)
l.color("light blue")
l.shape("square")
l.goto(180, -150)

p = turtle.Turtle()
p.speed(100)
p.penup()
p.shapesize(3, 3, 3)
p.color("light blue")
p.shape("square")
p.goto(180, 140)

s.update()
o = turtle.Turtle()
o.speed(100)
o.penup()
o.color("light blue")
o.shape("square")
o.shapesize(3, 3, 3)
o.goto(-170, 140)

s.update()

k.goto(-100, -180)
k.pendown()
k.color("red")
k.width(7)
k.forward(210)
k.penup()

k.goto(-160, 60)
k.pendown()
k.width(7)
k.color("red")
k.right(90)
k.forward(140)
k.penup()

k.goto(160, 60)
k.pendown()
k.width(7)
k.color("red")
k.forward(140)
k.penup()

k.hideturtle()
a.speed(0.5)

# Entire game logic
while True:
    s.update()

    # Control game speed based on score
    if sc > 50:
        delay = 0.1
    if sc > 150:
        delay = 0.05  # Faster gameplay after score 150

    a.speed(0.6)  # Maintain a consistent movement speed for the player

    if a.xcor() > 230 or a.xcor() < -230 or a.ycor() > 230 or a.ycor() < -230:
        time.sleep(1)
        a.goto(0, 0)
        a.direction = "stop"
        delay = 0.1
        life -= 1
        score.clear()
        food.goto(50, 0)

        score.write("Score : {} High Score : {} Life: {} ".format(sc, hs, life), align="center", font=("candra", 16, "bold"))
        if life == 0:
            if sc > hs:
                hs = sc
            time.sleep(1)
            a.goto(0, 0)
            sc = 0
            life = 3
            score.clear()
            score.write("Score : {} High Score : {} Life: {} ".format(sc, hs, life), align="center", font=("candra", 16, "bold"))
    if a.distance(food) < 20:
        food.goto(50, 0)
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        food.goto(x, y)
        sc += 10
        score.clear()
        score.write("Score : {} High Score : {} Life: {} ".format(sc, hs, life), align="center", font=("candra", 16, "bold"))

    move()
    time.sleep(delay)
