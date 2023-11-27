import turtle


def squares(order, size):
    if order == 0:
        return None
    else:
        for i in range(4):
            turtle.forward(size)
            turtle.right(90)
        turtle.forward(size * 0.05)
        turtle.right(10)
        squares(order - 1, size - 5)


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
