from data_base import list_view, write_data, write_data1, write_read_csv
from pathlib import Path
import logger
from prettytable import PrettyTable


def func_1():  # Просмотр всей тел книги: 1
    a = list_view().split()
    b = []
    c = []
    while len(a) > 0:
        b.append(a[0])
        b.append(a[1])
        b.append(a[2])
        del a[2]
        del a[1]
        del a[0]
        c.append(b)
        b = []
    mytable = PrettyTable()
    mytable.field_names = ["Фамилия", "Имя", "Номер телефона"]
    mytable.add_rows(c)
    print(mytable)
    logger.log("Просмотрена телефонная книга")


def func_2():  # Добавление новой записи: 2
    add_rec1 = str(input('Введите фамилию абонента: '))
    add_rec2 = str(input('Введите имя абонента: '))
    add_rec3 = str(input('Введите номер телефона абонента: '))
    write_data(add_rec1, add_rec2, add_rec3)
    print('Добавлен абонент:', add_rec1, ' ', add_rec2, ' ', add_rec3)
    logger.log('Добавлен абонент: {} {} {}'.format(
        add_rec1, add_rec2, add_rec3))


def func_3():  # Удаление записи тел книги по фамилии или имени: 3
    del_rec = str(input('Введите фамилию или имя или номер абонента: '))
    logger.log('Пользователь сделал запрос на удаление: {}'.format(del_rec))
    a = list_view().split()
    if del_rec not in a:
        print('Такой записи нет в тел книге')
        func_3()
    else:
        index = a.index(del_rec)
        if (index-1) % 3 == 0 or index == 1:
            logger.log('Удален абонент: {} {} {}'.format(
                a[index - 1], a[index], a[index + 1]))
            print('Удален абонент: {} {} {}'.format(
                a[index - 1], a[index], a[index + 1]))
            del a[index+1]
            del a[index]
            del a[index-1]

        elif index == 0 or index % 3 == 0:
            logger.log('Удален абонент: {} {} {}'.format(
                a[index], a[index + 1], a[index + 2]))
            print('Удален абонент: {} {} {}'.format(
                a[index], a[index + 1], a[index + 2]))
            del a[index+2]
            del a[index+1]
            del a[index]

        elif index != 0 or (index + 1) % 3 == 0:
            logger.log('Удален абонент: {} {} {}'.format(
                a[index - 2], a[index - 1], a[index]))
            print('Удален абонент: {} {} {}'.format(
                a[index - 2], a[index - 1], a[index]))
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


def func_4():  # Изменение записи в тел книге: 4
    a = list_view().split()  # получаем список строк из файла phonebook.txt
    edit_line = str(
        input('Введите фамилию или имя или телефон абонента для редактирования записи: '))
    logger.log(
        'Пользователь сделал запрос на редактирование: {}'.format(edit_line))
    if edit_line not in a:  # проверяем наличие введенного значения в списке строк
        print('Такой записи нет в тел книге')
        func_4()
    else:
        # получаем индекс искомого значения в списке
        index = a.index(edit_line)
        if (index-1) % 3 == 0 or index == 1:  # если введено имя
            print(a[index-1], ' ', a[index], ' ', a[index+1])
            add_rec = list(map(str, input(
                'Введите исправленные фамилию, имя и телефон через пробел:').split()))
            logger.log("Данные абонента: {} {} {} заменены на: {}".format(
                a[index - 1], a[index], a[index + 1], str(' '.join(add_rec))))
            print("Данные абонента: {} {} {} заменены на: {}".format(
                a[index - 1], a[index], a[index + 1], str(' '.join(add_rec))))
            # удаляем из списка указанного пользователем абонента
            del a[index + 1]
            del a[index]
            del a[index - 1]

        elif index == 0 or index % 3 == 0:  # если была введена фамилия
            print(a[index], ' ', a[index + 1], ' ', a[index + 2])
            add_rec = list(map(str,
                               input('Введите исправленные фамилию, имя и телефон через пробел:').split()))
            logger.log("Данные абонента: {} {} {} заменены на: {}".format(
                a[index], a[index + 1], a[index + 2], str(' '.join(add_rec))))
            print("Данные абонента: {} {} {} заменены на: {}".format(
                a[index], a[index + 1], a[index + 2], str(' '.join(add_rec))))
            # удаляем из списка указанного пользователем абонента
            del a[index + 2]
            del a[index + 1]
            del a[index]

        elif index != 0 or (index + 1) % 3 == 0:  # если был введен номер телефона
            print(a[index - 2], ' ', a[index - 1], ' ', a[index])
            add_rec = list(map(str,
                               input('Введите исправленные фамилию, имя и телефон через пробел:').split()))
            logger.log("Данные абонента: {} {} {} заменены на: {}".format(
                a[index - 2], a[index - 1], a[index], str(' '.join(add_rec))))
            print("Данные абонента: {} {} {} заменены на: {}".format(
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
    a = list_view().split()
    find_line = str(
        input('Введите фамилию или имя или телефон абонента для поиска записи: '))
    if find_line not in a:
        print('Такой записи нет в тел книге')
        func_5()
    else:
        index = a.index(find_line)
        if (index-1) % 3 == 0 or index == 1:
            print(a[index - 1], ' ', a[index], ' ', a[index + 1])
            logger.log('Выполнен поиск абонента: {} {} {}'.format(
                a[index - 1], ' ', a[index], ' ', a[index + 1]))
        elif index == 0 or index % 3 == 0:
            print(a[index], ' ', a[index + 1], ' ', a[index + 2])
            logger.log('Выполнен поиск абонента: {} {} {}'.format(
                a[index], ' ', a[index + 1], ' ', a[index + 2]))
        elif index != 0 or (index + 1) % 3 == 0:
            print(a[index - 2], ' ', a[index - 1], ' ', a[index])
            logger.log('Выполнен поиск абонента: {} {} {}'.format(
                a[index - 2], ' ', a[index - 1], ' ', a[index]))


def func_6():  # Экспорт тел книги в csv файл: 6
    write_read_csv()
    logger.log("Телефонная книга экспортированна в csv файл")
