import turtle


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
            drawer.write(num, font = ("Arial", 12))
            num += 1

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
