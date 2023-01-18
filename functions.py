from data_base import list_view, write_data, write_data1, write_read_csv
import controller
from pathlib import Path
import logger
from tkinter import *


def func_1():  # Просмотр всей тел книги: 1
    logger.log("Просмотрена телефонная книга")
    return list_view()


def func_2():  # Добавление новой записи: 2
    add_rec1 = controller.v1.get()
    add_rec2 = controller.v2.get()
    add_rec3 = controller.v3.get()
    write_data(add_rec1, add_rec2, add_rec3)
    logger.log('Добавлен абонент: {} {} {}'.format(
        add_rec1, add_rec2, add_rec3))
    return str(add_rec1 + add_rec2 + add_rec3)
    

def func_3():  # Удаление записи тел книги по фамилии или имени
    global x
    x = str("")
    if controller.v2.get() == "" and controller.v3.get() == "":
        del_rec = controller.v1.get()
    elif controller.v1.get() == "" and controller.v3.get() == "":
        del_rec = controller.v2.get()
    elif controller.v1.get() == "" and controller.v2.get() == "":
        del_rec = controller.v3.get()
    logger.log('Пользователь сделал запрос на удаление: {}'.format(del_rec))
    a = list_view().split()
    if del_rec not in a:
        controller.mistake_entry() # вызывает сообщение о том что адонента нет в списке
    else:
        index = a.index(del_rec)
        if (index-1) % 3 == 0 or index == 1:
            logger.log('Удален абонент: {} {} {}'.format(
                a[index - 1], a[index], a[index + 1]))
            x = str(a[index - 1] + a[index] + a[index + 1])    
            del a[index+1]
            del a[index]
            del a[index-1]

        elif index == 0 or index % 3 == 0:
            logger.log('Удален абонент: {} {} {}'.format(
                a[index], a[index + 1], a[index + 2]))
            x = str(a[index] + a[index + 1] + a[index + 2])    
            del a[index+2]
            del a[index+1]
            del a[index]

        elif index != 0 or (index + 1) % 3 == 0:
            logger.log('Удален абонент: {} {} {}'.format(
                a[index - 2], a[index - 1], a[index]))
            x = str(a[index - 2] + a[index - 1] + a[index])    
            del a[index]
            del a[index-1]
            del a[index-2]
    z = len(a)
    d = Path('Phonebook.txt')
    with open(d, 'w', encoding="utf-8") as data:
        data.seek(0)
        data.truncate()
    while z != 0:
        write_data1(a[0], a[1], a[2])
        del a[:3]
        z = z - 3
    func_3_1()

def func_3_1(): # дает ФИО и тел удаленного абонента для передачи в контроллер для показа в отдельном окне
    return x

def func_4():  # Редактирование записи в тел книге (кнопка Редактировать)
    global a, edit_line
    a = list_view().split()  # получаем список строк из файла phonebook.txt
    if controller.v2.get() == "" and controller.v3.get() == "": # проверяем что введено: фамилия, имя или телефон
        edit_line = controller.v1.get()
    elif controller.v1.get() == "" and controller.v3.get() == "": # проверяем что введено: фамилия, имя или телефон
        edit_line = controller.v2.get()
    elif controller.v1.get() == "" and controller.v2.get() == "": # проверяем что введено: фамилия, имя или телефон
        edit_line = controller.v3.get()
    logger.log('Пользователь сделал запрос на редактирование: {}'.format(edit_line)) # отправляем данные в лог файл

    if edit_line not in a:  # проверяем наличие введенного значения в списке строк (наличие абонента в тел справочнике)
        controller.mistake_entry() # вызывает сообщение о том что абонента нет в списке
    else:
        index = a.index(edit_line)# получаем индекс искомого значения в списке
        if (index-1) % 3 == 0 or index == 1:  # если введено имя
            y = str(a[index-1] + a[index] + a[index+1])    
        elif index == 0 or index % 3 == 0:  # если была введена фамилия
            y = str(a[index] + a[index + 1] + a[index + 2])    
        elif index != 0 or (index + 1) % 3 == 0:  # если был введен номер телефона
            y = str(a[index - 2] + a[index - 1] + a[index])    
    return y    

def func_4_1(): # Редактирование записи в тел книге (кнопка Ок). После того как введены отредактированные данные в поле "e4_changed_name"
    global y, a, edit_line, c
    y = str("")
    a = list_view().split()  # получаем список строк из файла phonebook.txt
    if controller.v2.get() == "" and controller.v3.get() == "": # проверяем что введено: фамилия, имя или телефон
        edit_line = controller.v1.get()
    elif controller.v1.get() == "" and controller.v3.get() == "": # проверяем что введено: фамилия, имя или телефон
        edit_line = controller.v2.get()
    elif controller.v1.get() == "" and controller.v2.get() == "": # проверяем что введено: фамилия, имя или телефон
        edit_line = controller.v3.get()
    index = a.index(edit_line)# получаем индекс искомого значения в списке

    if (index-1) % 3 == 0 or index == 1:  # если введено имя
        c = controller.v4.get()
        add_rec = list(map(str,c.split()))
        logger.log("Данные абонента: {} {} {} заменены на: {}".format(
            a[index - 1], a[index], a[index + 1], str(' '.join(add_rec))))
        del a[index + 1]# удаляем из списка указанного пользователем абонента
        del a[index]
        del a[index - 1]

    elif index == 0 or index % 3 == 0:  # если была введена фамилия
        c = controller.v4.get()
        add_rec = list(map(str,c.split()))
        logger.log("Данные абонента: {} {} {} заменены на: {}".format(
            a[index], a[index + 1], a[index + 2], str(' '.join(add_rec))))
        del a[index + 2]# удаляем из списка указанного пользователем абонента
        del a[index + 1]
        del a[index]

    elif index != 0 or (index + 1) % 3 == 0:  # если был введен номер телефона
        c = controller.v4.get()
        add_rec = list(map(str,c.split()))
        logger.log("Данные абонента: {} {} {} заменены на: {}".format(
            a[index - 2], a[index - 1], a[index], str(' '.join(add_rec))))
        del a[index]  # удаляем из списка указанного пользователем абонента
        del a[index - 1]
        del a[index - 2]
    b = a + add_rec  # суммируем  список строк из файла phonebook.txt и список строк add_rec введенный пользователем
    z = len(b)
    d = Path('Phonebook.txt')
    with open(d, 'w', encoding="utf-8") as data:
        data.seek(0)
        data.truncate()  # очищаем файл phonebook.txt
    while z != 0:
        # записываем построчно в файл phonebook.txt (в одной строке фам имя тел)
        write_data1(b[0], b[1], b[2])
        # удаляем перв строку из списка b и снова записываем в файл phonebook.txt следующую тройку
        del b[:3]
        z = z - 3  # уменьшаем счетчик


def func_5():  # Поиск по тел книге: 5
    global g
    a = list_view().split()
    
    if controller.v2.get() == "" and controller.v3.get() == "": # проверяем что введено: фамилия, имя или телефон
        find_line = controller.v1.get()
    elif controller.v1.get() == "" and controller.v3.get() == "": # проверяем что введено: фамилия, имя или телефон
        find_line = controller.v2.get()
    elif controller.v1.get() == "" and controller.v2.get() == "": # проверяем что введено: фамилия, имя или телефон
        find_line = controller.v3.get()

    if find_line not in a:
        controller.mistake_entry() # вызывает сообщение о том что адонента нет в списке
    else:
        index = a.index(find_line)
        if (index-1) % 3 == 0 or index == 1:
            g = str(a[index - 1] + a[index] + a[index + 1])
            logger.log('Выполнен поиск абонента: {} {} {}'.format(
                a[index - 1], ' ', a[index], ' ', a[index + 1]))
        elif index == 0 or index % 3 == 0:
            g = str(a[index] + a[index + 1] + a[index + 2])
            logger.log('Выполнен поиск абонента: {} {} {}'.format(
                a[index], ' ', a[index + 1], ' ', a[index + 2]))
        elif index != 0 or (index + 1) % 3 == 0:
            g = str(a[index - 2] + a[index - 1] + a[index])
            logger.log('Выполнен поиск абонента: {} {} {}'.format(
                a[index - 2], ' ', a[index - 1], ' ', a[index]))
    func_5_1()


def func_5_1(): # дает ФИО и тел искомого абонента для передачи в контроллер для показа в лэйбле
    return g

def func_6():  # Экспорт тел книги в csv файл: 6
    write_read_csv()
    logger.log("Телефонная книга экспортированна в csv файл")
