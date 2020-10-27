import turtle
import math


def main():
    draw_board()
    input()


def draw_board():
    # Draw both of the horizontal lines, starting from different heights.
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)

    # Draw both of the vertical lines
    for i in range(2):
        drawer.penup()
        drawer.goto(-100 + 200 * i, 300)
        drawer.pendown()
        drawer.forward(600)

    # Add numbers to the top corner of each square.
    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280 - i * 200)
            drawer.pendown()
            drawer.write(num, font=("Arial", 12, "normal"))
            num += 1

    # Update the screen with the new changes
    screen.update()


def draw_x(x, y):
    # Move to the correct spot
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.setheading(60)

    # Draw the lines of the draw
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)

    # Update the screen with the new changes
    screen.update()


def draw_o(x, y):
    # Move to the correct spot
    drawer.penup()
    drawer.goto(x, y + 75)
    drawer.pendown()
    drawer.setheading(0)

    # Draw a circle with the correct size
    for i in range(180):
        drawer.forward((150 * math.pi) / 180)
        drawer.right(2)

    # Update the screen with the new changes
    screen.update()


# Create turtle
drawer = turtle.Turtle()
drawer.pensize(10)
drawer.ht()
# Create screen
screen = turtle.Screen()
screen.tracer(0)

if __name__ == '__main__':
    main()
