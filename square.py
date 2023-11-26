import turtle


def squares(order, size):
    if order == 0:
        turtle.forward(1)
    else:
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.right(5)
        turtle.up()
        turtle.forward(10)
        turtle.down()
        squares(order-1, size - 10)


def main_squares():
    turtle.up()
    turtle.speed(10)
    turtle.goto(-100, 0)
    turtle.setheading(0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    squares(n, a)


if __name__ == '__main__':
    main_squares()
