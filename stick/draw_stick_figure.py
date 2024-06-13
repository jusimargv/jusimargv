import turtle

def draw_stick_figure():
    # Draw the torso
    turtle.color('blue')
    turtle.right(90)
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(90)

    # Draw the legs
    turtle.color('green')
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(30)
    turtle.backward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.backward(30)
    turtle.right(45)
    turtle.backward(100)
    turtle.left(90)

    # Draw the arms
    turtle.color('yellow')
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.backward(30)
    turtle.left(180)
    turtle.forward(30)
    turtle.backward(30)
    turtle.left(90)
    turtle.backward(30)
    turtle.left(90)

    # Draw the head
    turtle.color('purple')
    turtle.forward(25)
    turtle.circle(25)
    turtle.backward(25)

def main():
    turtle.speed(1)
    for i in range(5):
        draw_stick_figure()
        turtle.forward(100)

    turtle.hideturtle()
    turtle.done()

main()