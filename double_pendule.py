import turtle
import math as m

# screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Double pendulum")
screen.tracer(0)

# head
h = turtle.Turtle()
h.hideturtle()
h.dot(5, "blue")
h.pencolor("blue")
h.goto(0, 300)
h.penup()
h.pencolor("green")
h.pensize(5)

#variable
length_1 = 300
length_2 = 200
grav_const = 1
mass1 = 1
mass2 = 1

def step(phi1, phi2):
    phi1_dd = (-grav_const * (2 *mass1 + mass2)* m.sin(phi1) - mass2 * grav_const * m.sin(phi1 - 2 * phi2))

def draw(phi1, phi2):
    h.clear()
    h.pendown()

    phi1 = m.radians(phi1)
    phi2 = m.radians(phi2)

    x = length_1 * m.sin(phi1)
    y = 300 - length_1 * m.cos(phi1)
    k = x + length_2 * m.sin(phi2)
    l = y - length_2 * m.cos(phi2)

    h.goto(x, y)
    h.goto(k, l)
    h.penup()
    h.goto(x, y)
    h.dot(20, "red")
    h.goto(k, l)
    h.dot(20, "red")
    h.goto(0, 300)


draw(0, 0)

screen.update()
turtle.exitonclick()
