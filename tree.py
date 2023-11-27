import turtle


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
    turtle.tracer(0)
    turtle.left(90)
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина отрезка:'))
    ang = int(input('Угол между ветками:'))
    tree(n, a, ang)
    turtle.update()
    turtle.done()


if __name__ == '__main__':
    main_tree()
