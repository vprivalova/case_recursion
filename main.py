import turtle


def menu():
    hello_script = """ 
    Меню:
    Квадраты - введите 1
    Двоичное дерево - введите 2
    Ветка - введите 3
    Кривая Коха - введите 4
    Снежинка Коха - введите 5
    Кривая Минковского - введите 6
    Ледяной фрактал 1 - введите 7
    Ледяной фрактал 2 - введите 8
    Кривая Леви - введите 9
    Уникальный фрактал - введите 10
    """
    print(hello_script)
    start = input()
    if start == '1':
        squares()
    elif start == '2':
        tree()
    elif start == '3':
        branch()
    elif start == '4':
        koch_curve()
    elif start == '5':
        koch_snowflake()
    elif start == '6':
        minkovsky_curve()
    elif start == '7':
        ice_fractal_1()
    elif start == '8':
        ice_fractal_2()
    elif start == '9':
        levi_curve()
    elif start == '10':
        new_fractal()


def squares():
    pass


def tree():
    pass


def branch():
    pass


def koch_curve():
    pass


def koch_snowflake():
    pass


def minkovsky_curve():
    pass


def ice_fractal_1():
    pass


def ice_fractal_2():
    pass


def levi_curve():
    pass


def new_fractal():
    pass


menu()
