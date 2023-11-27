import turtle
import ru_local as ru


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
    squares(n, a)


if __name__ == '__main__':
    main_squares()
