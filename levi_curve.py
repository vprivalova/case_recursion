import turtle


def levi(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        turtle.left(45)
        levi(order - 1, size/2)
        turtle.right(90)
        levi(order - 1, size/2)
        turtle.left(45)


def main_levicurve():
    turtle.up()
    turtle.speed(10)
    turtle.goto(-100, 0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    levi(n, a)


if __name__ == '__main__':
    main_levicurve()
