import turtle
import ru_local as ru


def ice_fractal_1(n, size):
    if n == 0:
        turtle.forward(size)
    else:
        ice_fractal_1(n - 1, size / 2)
        turtle.left(90)
        ice_fractal_1(n - 1,  size / 4)
        turtle.left(180)
        ice_fractal_1(n-1, size / 4)
        turtle.left(90)
        ice_fractal_1(n - 1, size / 2)


def main_ice1():
    turtle.up()
    turtle.speed(10)
    turtle.goto(-100, 0)
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
    ice_fractal_1(n, a)


if __name__ == '__main__':
    main_ice1()
