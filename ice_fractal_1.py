import turtle


def ice_fractal_1(n, size):
    if n == 0:
        turtle.forward(size)
    else:
        ice_fractal_1(n-1, size / 2)
        turtle.left(90)
        ice_fractal_1(n-1,  size / 4)
        turtle.left(180)
        ice_fractal_1(n-1, size / 4)
        turtle.left(90)
        ice_fractal_1(n - 1, size / 2)


def main():
    turtle.tracer(0)
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    ice_fractal_1(n, a)
    turtle.update()
    turtle.done()


main()
turtle.mainloop()