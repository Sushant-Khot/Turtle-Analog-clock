import time
import turtle
import math

# Setup screen
wn = turtle.Screen()
wn.bgcolor("#121212")  
wn.setup(width=600, height=600)
wn.title("Simple Analog Clock By Team GOLD")
wn.tracer(0)

# Create drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):
    # Draw outer frame
    pen.up()
    pen.goto(0, -210)
    pen.setheading(0)
    pen.color("gold")
    pen.down()
    pen.circle(210)

    # Draw hour ticks
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    for _ in range(12):
        pen.fd(180)
        pen.pendown()
        pen.fd(30)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Draw minute ticks
    pen.setheading(90)
    for _ in range(60):
        pen.fd(200)
        pen.pendown()
        pen.fd(10)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(6)

    # Draw hour numbers (1 to 12)
    pen.color("white")
    pen.up()
    font = ("Courier", 14, "bold")
    for hour in range(1, 13):
        angle = math.radians(90 - hour * 30)
        x = 160 * math.cos(angle)
        y = 160 * math.sin(angle)
        pen.goto(x, y - 10)  # slight vertical adjust
        pen.write(str(hour), align="center", font=font)

    # Draw center pivot
    pen.goto(0, 0)
    pen.dot(12, "white")

    # Hour hand
    pen.color("cyan")
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (h % 12 + m / 60) * 30
    pen.rt(angle)
    pen.pendown()
    pen.fd(90)

    # Minute hand
    pen.color("cyan")
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (m + s / 60) * 6
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    # Second hand
    pen.color("gray")
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = s * 6
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(h, m, s, pen)
    wn.update()
    time.sleep(1)
    pen.clear()

wn.mainloop()
