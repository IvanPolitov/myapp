import mymath
from tkinter import *
from tkinter import messagebox as mb

BUTTON_W_MAIN_MENU = 170
BUTTON_H_MAIN_MENU = 40
GUIDE_TXT_FILE = 'guide_text.txt'

class MainWindow(Frame):
    def __init__(self, parent):
        self.pixelVirtual = PhotoImage(width=1, height=1)
        super(MainWindow, self).__init__()
        self.parent = parent
        self.window_setting()
        self.make_MainMenu()
        self.parent.bind("<q>", self.vihod)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        file_menubar = Menu(menubar, tearoff=0)
        file_menubar.add_command(label='О программе')
        file_menubar.add_command(label='Выход', command=quit)

        menubar.add_cascade(label='Файл', menu=file_menubar)
        menubar.add_command(label='Справка', command=self.call_Guide)

    def make_MainMenu(self):
        self.frame_MainMenu = Frame(self.parent)
        self.frame_MainMenu.pack(expand=1, fill=X)

        frame_btn_add_mult_div = Frame(self.frame_MainMenu)
        frame_btn_add_mult_div.pack(expand=1, fill=X)

        frame_btn_another = Frame(self.frame_MainMenu)
        frame_btn_another.pack(expand=1, fill=X, ipady=5)

        button_add = Button(frame_btn_add_mult_div,
                                   text='Сложение',
                                   command=self.call_UnitAdd,
                                   image=self.pixelVirtual,
                                   width=BUTTON_W_MAIN_MENU,
                                   height=BUTTON_H_MAIN_MENU,
                                   compound='center',
                                   font="Arial 20")

        button_multiply = Button(frame_btn_add_mult_div,
                                 text='Умножение',
                                 command=self.call_UnitMultiply,
                                 image=self.pixelVirtual,
                                 width=BUTTON_W_MAIN_MENU,
                                 height=BUTTON_H_MAIN_MENU,
                                 compound='center',
                                 font="Arial 20")

        button_div = Button(frame_btn_add_mult_div,
                            text='Деление',
                            command=self.call_UnitAdd,
                            image=self.pixelVirtual,
                            width=BUTTON_W_MAIN_MENU,
                            height=BUTTON_H_MAIN_MENU,
                            compound='center',
                            font="Arial 20")

        button_f1 = Button(frame_btn_another,
                                   text='f1',
                                   # command=self.call_UnitAdd,
                                   image=self.pixelVirtual,
                                   width=BUTTON_W_MAIN_MENU,
                                   height=BUTTON_H_MAIN_MENU,
                                   compound='center',
                                   font="Arial 20")

        button_f2 = Button(frame_btn_another,
                                 text='f2',
                                 # command=self.call_UnitMultiply,
                                 image=self.pixelVirtual,
                                 width=BUTTON_W_MAIN_MENU,
                                 height=BUTTON_H_MAIN_MENU,
                                 compound='center',
                                 font="Arial 20")

        button_f3 = Button(frame_btn_another,
                            text='f3',
                            # command=self.call_UnitAdd,
                            image=self.pixelVirtual,
                            width=BUTTON_W_MAIN_MENU,
                            height=BUTTON_H_MAIN_MENU,
                            compound='center',
                            font="Arial 20")
        button_quit = Button(self.frame_MainMenu,
                            text='Выход',
                            command=quit,
                            image=self.pixelVirtual,
                            width=BUTTON_W_MAIN_MENU,
                            height=BUTTON_H_MAIN_MENU,
                            compound='center',
                            font="Arial 20")


        button_add.pack(side=LEFT, padx=8)
        button_multiply.pack(side=LEFT)
        button_div.pack(side=LEFT, padx=8)
        button_f1.pack(side=LEFT, padx=8)
        button_f2.pack(side=LEFT)
        button_f3.pack(side=LEFT, padx=8)
        button_quit.pack(pady=15)


    def call_Guide(self):
        file = open(GUIDE_TXT_FILE, 'r', encoding='utf-8')
        txt = file.read()
        file.close()

        wdw = Toplevel()
        Label(wdw, text=txt, font="Arial 11").pack(expand=1)
        Button(wdw, text='Закрыть', command=wdw.destroy, font="Arial 14").pack(side=RIGHT)


    def call_UnitAdd(self):
        self.frame_MainMenu.pack_forget()
        self.make_UnitAdd()

    def call_MainMenu(self):
        self.frame_MainMenu.pack(expand=1, fill=X)

    def make_UnitAdd(self):
        # Main для основных действий программы, system - для вспомогательных
        self.f_main = Frame(self.parent)
        self.f_system = Frame(self.parent)
        self.f_main.pack(expand=1, fill=BOTH)
        self.f_system.pack(anchor=S, expand=0, fill=X)

        # Строка где будут наши выражения
        self.example = Label(self.f_main, text='example', font="Arial 20", width=7)
        self.example.pack(side=LEFT, anchor=NW)
        self.result = 0

        # Поле для ввода данных
        self.user_result = Entry(self.f_main, font="Arial 20", width=5)
        self.user_result.pack(side=LEFT, anchor=NW)

        # Кнопка для проверки введенного ответа
        button_answer = Button(self.f_main, text='Ответить', command=self.check_answer, font="Arial 14")
        button_answer.pack(side=LEFT, anchor=NW)

        # Кнопка для выхода
        button_quit = Button(self.f_system, text='Закрыть', command=self.quit)
        button_quit.pack(side=RIGHT, anchor=E)

        # Кнопка для генерации нового выражения в строке example
        button_generate = Button(self.f_system, text='Новый пример', command=self.gen)
        button_generate.pack(side=LEFT, anchor=W)

        # Кнопка для генерации нового окна
        button_new_window = Button(self.f_system, text='Главное меню', command=self.call_MainMenu)
        button_new_window.pack(side=LEFT, anchor=W)

        # Забиндили энтер с той же функцией, что и button_answer
        self.parent.bind("<Return>", self.check_answer_press_enter)

        self.gen()

    def check_answer_press_enter(self, event):
        self.check_answer()

    def vihod(self, event):
        self.quit()
    def gen(self):
        self.example['text'], self.result = mymath.gen_plus_minus()

    # Проверка ответа
    def check_answer(self):
        if self.check_isdigit():
            if self.user_result.get() == self.result:
                self.gen()
                self.user_result.delete(0, END)
            else:
                mb.showwarning("Неверно", "Неправильный ответ")

    # Проверка, число ли вписано
    def check_isdigit(self):
        s = self.user_result.get()
        if s != '' and (s.isdigit() or s[0] == '-' and s[1:].isdigit()):
            return True
        else:
            mb.showerror("Ошибка", "Введите число")
            return False

    # def call_MainWindow(self):
    #     self.f_main.destroy()
    #     self.f_system.destroy()
    #     self.make_MainMenu()


    def call_UnitMultiply(self):
        self.f_main.destroy()
        UnitMultiply(self.parent)

    def window_setting(self):
        """Размер окна и центрирование"""
        w = 565
        h = 400
        self.parent.title("Математика")
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.parent.resizable(False, False)
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


class UnitPlusMinus(Frame):
    def __init__(self, parent):
        super(UnitPlusMinus, self).__init__()
        self.parent = parent
        self.main_window_setting()

        # Main для основных действий программы, system - для вспомогательных
        self.f_main = Frame(self.parent)
        self.f_system = Frame(self.parent)
        self.f_main.pack(expand=1, fill=BOTH)
        self.f_system.pack(anchor=S, expand=0, fill=X)

        # Строка где будут наши выражения
        self.example = Label(self.f_main, text='example', font="Arial 20")
        self.example.pack(side=LEFT, anchor=NW)
        self.result = 0

        # Поле для ввода данных
        self.user_result = Entry(self.f_main, font="Arial 20", width=5)
        self.user_result.pack(side=LEFT, anchor=NW)

        # Кнопка для проверки введенного ответа
        button_answer = Button(self.f_main, text='Ответить', command=self.check_answer, font="Arial 14")
        button_answer.pack(side=LEFT, anchor=NW)

        # Кнопка для выхода
        button_quit = Button(self.f_system, text='Закрыть', command=self.quit)
        button_quit.pack(side=RIGHT, anchor=E)

        # Кнопка для генерации нового выражения в строке example
        button_generate = Button(self.f_system, text='Новый пример', command=self.gen)
        button_generate.pack(side=LEFT, anchor=W)

        # Кнопка для генерации нового окна
        button_new_window = Button(self.f_system, text='Главное меню', command=self.call_MainWindow)
        button_new_window.pack(side=LEFT, anchor=W)

        # Забиндили энтер с той же функцией, что и button_answer
        parent.bind("<Return>", self.check_answer_press_enter)
        self.gen()


    # check_answer для энтера
    def check_answer_press_enter(self, event):
        self.check_answer()

    # Настройка параметров окна приложения
    def main_window_setting(self):
        """Размер окна и центрирование"""
        w = 400
        h = 200
        self.parent.title("Математика")
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.parent.resizable(False, False)
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Генерация выражения и правильного ответа для проверки
    def gen(self):
        self.example['text'], self.result = mymath.gen_plus_minus()

    # Проверка ответа
    def check_answer(self):
        if self.check_isdigit():
            if self.user_result.get() == self.result:
                self.gen()
                self.user_result.delete(0, END)
            else:
                mb.showwarning("Неверно", "Неправильный ответ")

    # Проверка, число ли вписано
    def check_isdigit(self):
        s = self.user_result.get()
        if s != '' and (s.isdigit() or s[0] == '-' and s[1:].isdigit()):
            return True
        else:
            mb.showerror("Ошибка", "Введите число")
            return False

    def call_MainWindow(self):
        self.f_main.destroy()
        self.f_system.destroy()
        MainWindow(self.parent)

class UnitMultiply(Frame):
    def __init__(self, parent):
        super(UnitMultiply, self).__init__()
        self.parent = parent
        self.main_window_setting()

        # Main для основных действий программы, system - для вспомогательных
        self.f_main = Frame(self.parent)
        self.f_system = Frame(self.parent)
        self.f_main.pack(expand=1, fill=BOTH)
        self.f_system.pack(anchor=S, expand=0, fill=X)

        # Строка где будут наши выражения
        self.example = Label(self.f_main, text='example', font="Arial 20")
        self.example.pack(side=LEFT, anchor=NW)
        self.result = 0

        # Поле для ввода данных
        self.user_result = Entry(self.f_main, font="Arial 20", width=5)
        self.user_result.pack(side=LEFT, anchor=NW)

        # Кнопка для проверки введенного ответа
        button_answer = Button(self.f_main, text='Ответить', command=self.check_answer, font="Arial 14")
        button_answer.pack(side=LEFT, anchor=NW)

        # Кнопка для выхода
        button_quit = Button(self.f_system, text='Закрыть', command=self.quit)
        button_quit.pack(side=RIGHT, anchor=E)

        # Кнопка для генерации нового выражения в строке example
        button_generate = Button(self.f_system, text='Новый пример', command=self.gen)
        button_generate.pack(side=LEFT, anchor=W)

        # Кнопка для генерации нового окна
        button_new_window = Button(self.f_system, text='Главное меню', command=self.call_MainWindow)
        button_new_window.pack(side=LEFT, anchor=W)

        # Забиндили энтер с той же функцией, что и button_answer
        parent.bind("<Return>", self.check_answer_press_enter)
        self.gen()

    # check_answer для энтера
    def check_answer_press_enter(self, event):
        self.check_answer()

    # Настройка параметров окна приложения
    def main_window_setting(self):
        """Размер окна и центрирование"""
        w = 400
        h = 200
        self.parent.title("Математика")
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.parent.resizable(False, False)
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Генерация выражения и правильного ответа для проверки
    def gen(self):
        self.example['text'], self.result = mymath.gen_multiply()

    # Проверка ответа
    def check_answer(self):
        if self.check_isdigit():
            if self.user_result.get() == self.result:
                self.gen()
                self.user_result.delete(0, END)
            else:
                mb.showwarning("Неверно", "Неправильный ответ")

    # Проверка, число ли вписано
    def check_isdigit(self):
        s = self.user_result.get()
        if s != '' and (s.isdigit() or s[0] == '-' and s[1:].isdigit()):
            return True
        else:
            mb.showerror("Ошибка", "Введите число")
            return False

    def call_MainWindow(self):
        self.f_main.destroy()
        self.f_system.destroy()
        MainWindow(self.parent)

def main():
    main_window = Tk()
    app = MainWindow(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    main()
