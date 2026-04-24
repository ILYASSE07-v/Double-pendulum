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

# variable
length_1 = 300
length_2 = 200
grav_const = 1
mass1 = 1
mass2 = 1
phi1_d = 0
phi2_d = 0
temp1 = 100
temp2 = 20


def step(tet1, tet2):
    global phi1_d, phi2_d, temp1, temp2
    dt = 0.05
    dev = (2 * mass1 + mass2 - mass2 * m.cos(2 * tet1 - 2 * tet2))
    phi1_dd = (-grav_const * (2 * mass1 + mass2) * m.sin(tet1) - mass2 * grav_const * m.sin(tet1 - 2 * tet2) - 2 * m.sin(tet1 -
               tet2) * mass2 * (((phi2_d) ** 2) * length_2 + ((phi1_d) ** 2) * length_1 * m.cos(tet1 - tet2))) / (length_1 * dev)
    phi2_dd = (2 * m.sin(tet1 - tet2) * (((phi1_d) ** 2) * length_1 * (mass1 + mass2) + grav_const * (mass1 +
               mass2) * m.cos(tet1) + ((phi2_d) ** 2) * length_2 * mass2 * m.cos(tet1 - tet2))) / (length_2 * dev)
    phi1_d += phi1_dd * dt
    phi2_d += phi2_dd * dt
    phi1_d *= 0.9999999
    phi2_d * + 0.9999999
    tet1 += phi1_d * dt
    tet2 += phi2_d * dt
    temp1 = tet1
    temp2 = tet2
    return tet1, tet2


def draw(phi1, phi2):
    h.clear()
    h.pendown()

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


temp1 = m.radians(temp1)
temp2 = m.radians(temp2)
while True:
    draw(*step(temp1, temp2))
    screen.update()
