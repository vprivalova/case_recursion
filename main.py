import turtle
import minkovsky_curve
import square
import tree
import branch
import curve
import snowflake
import ice_fractal_1
import ice_fractal_2
import levi_curve
import new_fractal


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
    
    Для завершения работы введите "END"
    """
    print(hello_script)
    start = input('Ввод: ')
    turtle.reset()
    if start == 'END':
        return None
    else:
        if start == '1':
            square.main_squares()
            menu()
        elif start == '2':
            tree.main_tree()
            menu()
        elif start == '3':
            branch.main_branch()
            menu()
        elif start == '4':
            curve.main_curve()
            menu()
        elif start == '5':
            snowflake.main_snowflake()
            menu()
        elif start == '6':
            minkovsky_curve.main_minkovskycurve()
            menu()
        elif start == '7':
            ice_fractal_1.main_ice1()
            menu()
        elif start == '8':
            ice_fractal_2.main_ice2()
            menu()
        elif start == '9':
            levi_curve.main_levicurve()
            menu()
        elif start == '10':
            new_fractal.main_newfractal()
            menu()


menu()
