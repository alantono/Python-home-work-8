
import functions
import logger
from tkinter import *
from tkinter import font

def button_click():
    logger.log("Программа запущена")

root = Tk()
root.title("Телефонный справочник")
root.geometry("820x400+400+400")
root.resizable(width=False, height=False)

def clear_entry_1(): # очистка лэйблов: редактируемых
        l4_1 = Label(root, text="                                                                                \n                                                                                    ", font=("Arial", 8), justify=LEFT)
        l4_1.place(x = 10, y = 270)
        # l4_1.place_forget()
        l4_2 = Label(root, text="                                                 ", font=("Arial", 9))
        l4_2.place(x = 290, y = 280)
        # l4_2.place_forget()
        e4_changed_name.delete(0, END)


def clear_entry(): # очистка полей: имя фамилия телефон
        e1_surname.delete(0, END)
        e2_name.delete(0, END)
        e3_ph_number.delete(0, END)

def mistake_entry(): # ошибочный ввод данных
        mistake_entry = Tk()
        mistake_entry.title("Сообщение")
        mistake_entry.geometry("300x30+1200+400")
        label = Label(mistake_entry, text="Такой записи нет в тел книге!", font=("Arial", 12))
        label.pack()
        clear_entry()
        mistake_entry.mainloop()


def enter1(event):# вывод в отдельном окне Списка абонентов
        window_text = Tk()
        window_text.title("Список абонентов")
        window_text.geometry("200x400+1400+400")
        t = Text(window_text)
        t.pack()
        t.insert(1.0, functions.func_1())
        window_text.mainloop()

def enter2(event): # Добавление нового абонента
        add_abonent = Tk() # вывод в отдельном окне добавленного абонента
        add_abonent.title("Добавлен абонент")
        add_abonent.geometry("400x30+1200+400")
        label_aa = Label(add_abonent, text="", font=("Arial", 12))
        label_aa["text"] = functions.func_2()
        label_aa.pack()
        clear_entry()
        add_abonent.mainloop()
        functions.func_2()
        
    
def enter3(event): # удаление абонента
        functions.func_3()
        del_abonent = Tk() # вывод в отдельном окне удаленного абонента
        del_abonent.title("Удален абонент")
        del_abonent.geometry("400x30+1200+400")
        label_da = Label(del_abonent, text="", font=("Arial", 12))
        label_da["text"] = functions.func_3_1()
        label_da.pack()
        clear_entry()
        del_abonent.mainloop()
      

def enter4(event): # редактирование абонента. кнопка Редактировать
        l4_1 = Label(root, text='Введите исправленные фамилию,имя и телефон\nчерез пробел в поле справа и нажмите "Ок"', font=("Arial", 8), justify=LEFT)
        l4_1.place(x = 10, y = 270)
        l4_2 = Label(root, text="", font=("Arial", 9))
        l4_2["text"] = functions.func_4()
        l4_2.place(x = 290, y = 280)
    

def enter4_1(event): # редактирование абонента. кнопка Ок
        functions.func_4_1()
        clear_entry_1()
        clear_entry()


def enter5(event):
        e5_found_name.delete(0, END)
        functions.func_5()
        e5_found_name.insert(0, functions.func_5_1())

def enter6(event):
        functions.func_6()

l2 = Label(root, text='Для добавления абонента заполните поля выше и нажмите "Добавить"', font=("Arial", 10)).place(x = 10, y = 180)
l3 = Label(root, text='Для удаления абонента введите фамилию или имя или номер абонента и нажмите "Удалить"', font=("Arial", 10)).place(x = 10, y = 210)
l4 = Label(root, text='Для редактирования введите фамилию или имя абонента в поле выше и нажмите "Редактировать"', font=("Arial", 10)).place(x = 10, y = 240)
l5 = Label(root, text='Введите фамилию или имя или телефон абонента в поле выше и нажмите Найти"', font=("Arial", 10)).place(x = 10, y = 320)
l5_2 = Label(root, text='Найден абонент:', font=("Arial", 10)).place(x = 10, y = 350)


b1 = Button(root, text="Просмотр всей тел книги", width=39, height=1)
b2 = Button(root, text="Добавить", width=11, height=1)
b3 = Button(root, text="Удалить", width=11, height=1)
b4 = Button(root, text="Редактировать", width=11, height=1)
b4_1 = Button(root, text="Ok", width=11, height=1)
b5 = Button(root, text="Найти", width=11, height=1)
b6 = Button(root, text="Экспорт тел книги в csv файл", width=39, height=1)

l_surname = Label(root, text='Фамилия', font=("Arial", 10)).place(x = 10, y = 20)
l_name = Label(root, text='Имя', font=("Arial", 10)).place(x = 10, y = 50)
l_ph_number = Label(root, text='Номер телефона', font=("Arial", 10)).place(x = 10, y = 80)


v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar() 
v5 = StringVar()


e1_surname = Entry(root, textvariable=v1, width=18, justify=CENTER,
        font=font.Font(family="Arial Black", size=10))
e1_surname.place(x=120, y=20)
e2_name = Entry(root, textvariable=v2, width=18, justify=CENTER,
        font=font.Font(family="Arial Black", size=10))
e2_name.place(x = 120, y = 50)
e3_ph_number = Entry(root, textvariable=v3, width=18, justify=CENTER,
        font=font.Font(family="Arial Black", size=10))
e3_ph_number.place(x = 120, y = 80)
e4_changed_name = Entry(root, textvariable=v4, width= 22, justify=LEFT,
        font=font.Font(family="Arial Black", size=10))
e4_changed_name.place(x = 520, y = 280)
e5_found_name = Entry(root, textvariable=v5, width= 33, justify=CENTER,
        font=font.Font(family="Arial Black", size=10))
e5_found_name.place(x = 130, y = 350)


b1.bind('<Button-1>', enter1)
b1.place(x = 10, y = 120)
b2.bind('<Button-1>', enter2)
b2.place(x = 720, y = 180)
b3.bind('<Button-1>', enter3)
b3.place(x = 720, y = 210)
b4.bind('<Button-1>', enter4)
b4.place(x = 720, y = 240)
b4_1.bind('<Button-1>', enter4_1)
b4_1.place(x = 720, y = 280)
b5.bind('<Button-1>', enter5)
b5.place(x = 720, y = 320)
b6.bind('<Button-1>', enter6)
b6.place(x = 10, y = 150)

root.mainloop()
logger.log("Программа закрыта")