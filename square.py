from turtle import *


def squares(order, size):
    if order == 0:
        forward(1)
    else:
        forward(size)
        right(90)
        forward(size)
        right(90)
        forward(size)
        right(90)
        forward(size)
        right(90)
        right(5)
        up()
        forward(10)
        down()
        squares(order-1, size - 10)


def main():
    up()
    goto(-100, 0)
    setheading(0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    squares(n, a)


main()
mainloop()
