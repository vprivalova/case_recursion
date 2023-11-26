import turtle


def tree(n, size):
    if n == 0:
        return None
    turtle.fd(size)
    turtle.rt(45)
    tree(n - 1, 0.6 * size)
    turtle.lt(90)
    tree(n - 1, 0.6 * size)
    turtle.rt(45)
    turtle.backward(size)


def main_tree():
    turtle.speed(10)
    turtle.left(90)
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина отрезка:'))
    tree(n, a)


if __name__ == '__main__':
    main_tree()
