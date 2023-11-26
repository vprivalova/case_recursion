import turtle


def unique(order, size):
    if order == 0:
        turtle.circle(size, 180)
        turtle.right(30)
    else:
        turtle.left(90)
        unique(order - 1, size / 2)
        turtle.right(120)
        unique(order - 1, size / 2)
        turtle.left(90)


def main_newfractal():
    turtle.up()
    turtle.speed(10)
    turtle.goto(-100, 0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    unique(n, a)


if __name__ == '__main__':
    main_newfractal()
