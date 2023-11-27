import turtle
import ru_local as ru


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

    available_colors = [ru.RED, ru.YELLOW, ru.GREEN, ru.BLUE, ru.BLACK, ru.VIOLET, ru.ORANGE]
    available_colors_eng = {ru.RED: 'red', ru.YELLOW: 'yellow', ru.GREEN: 'green', ru.BLUE: 'blue',
                            ru.BLACK: 'black', ru.VIOLET: 'violet', ru.ORANGE: 'orange'}

    print(ru.ACCEPTABLE_COLORS)

    for element in available_colors:
        print(element)

    color_name1 = input('\n' + ru.COLOR1_INPUT)
    while color_name1 not in available_colors:
        color_name1 = input(ru.COLOR1_INPUT_AGAIN)

    color_name1 = available_colors_eng.setdefault(color_name1)
    turtle.pencolor(color_name1)

    minkovsky_curve(n, a)


if __name__ == '__main__':
    main_minkovskycurve()
