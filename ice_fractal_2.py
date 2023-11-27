import turtle


def ice_fractal_2(n, size):
    if n == 0:
        turtle.forward(size)
    else:
        ice_fractal_2(n - 1, size)
        turtle.left(120)
        ice_fractal_2(n - 1, size / 2)
        turtle.left(180)
        ice_fractal_2(n - 1, size / 2)
        turtle.left(120)
        ice_fractal_2(n - 1, size / 2)
        turtle.left(180)
        ice_fractal_2(n - 1, size / 2)
        turtle.left(120)
        ice_fractal_2(n - 1, size)


def main_ice2():
    turtle.up()
    turtle.speed(10)
    turtle.goto(-100, 0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    ice_fractal_2(n, a)


if __name__ == '__main__':
    main_ice2()
