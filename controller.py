from view import menu, get_num
from functions import func_1, func_2, func_3, func_4, func_5, func_6
import logger


def button_click():
    logger.log("Программа запущена")
    n = get_num()
    if n == 5:
        logger.log("Нажата клавиша - 5")
        func_5()
    elif n == 1:
        logger.log("Нажата клавиша - 1")
        func_1()
    elif n == 2:
        logger.log("Нажата клавиша - 2")
        func_2()
    elif n == 3:
        logger.log("Нажата клавиша - 3")
        func_3()
    elif n == 4:
        logger.log("Нажата клавиша - 4")
        func_4()
    elif n == 6:
        logger.log("Нажата клавиша - 6")
        func_6()
    else:
        button_click()
    logger.log("Программа выполнена")


menu()
