def main():
    turtle.speed(1)
    for i in range(5):
        turtle.penup()
        turtle.setx(i * 100)
        turtle.sety(0)
        turtle.pendown()
        draw_stick_figure()

    turtle.hideturtle()
    turtle.done()

main()