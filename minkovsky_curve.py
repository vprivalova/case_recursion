import turtle


def minkovsky_curve(n, size):
    if n == 0:
        turtle.forward(size)
    else:
        minkovsky_curve(n - 1, size)
        turtle.left(90)
        minkovsky_curve(n - 1, size)
        turtle.right(90)
        minkovsky_curve(n - 1, size)
        turtle.right(90)
        minkovsky_curve(n - 1, size)
        minkovsky_curve(n - 1, size)
        turtle.left(90)
        minkovsky_curve(n - 1, size)
        turtle.left(90)
        minkovsky_curve(n - 1, size)
        turtle.right(90)
        minkovsky_curve(n - 1, size)


def main_minkovskycurve():
    turtle.up()
    turtle.speed(10)
    turtle.goto(-400, 0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    minkovsky_curve(n, a)


if __name__ == '__main__':
    main_minkovskycurve()
