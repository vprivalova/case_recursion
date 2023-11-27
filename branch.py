import turtle
import ru_local as ru

def branch(n, size):
    if n == 0:
        turtle.left(180)
        return

    x = size / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        turtle.left(90)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)


def main_branch():
    turtle.up()
    turtle.speed(10)
    turtle.goto(0, -100)
    turtle.left(90)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина векти:'))

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
    branch(n, a)


if __name__ == '__main__':
    main_branch()
