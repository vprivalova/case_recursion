import turtle
import ru_local as ru


def tree(n, size, angle):
    if n == 0:
        return None
    turtle.forward(size)
    turtle.right(angle)
    tree(n-1, 0.6 * size, angle)
    turtle.left(angle)
    tree(n-1, 0.6 * size, angle)
    turtle.left(angle)
    tree(n-1, 0.6 * size, angle)
    turtle.right(angle)
    tree(n-1, 0.6 * size, angle)
    turtle.backward(size)


def main_tree():
    turtle.left(90)
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина отрезка:'))
    ang = int(input('Угол между ветками:'))

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
    tree(n, a, ang)


if __name__ == '__main__':
    main_tree()
