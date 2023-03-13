import mymath
from tkinter import *
from tkinter import messagebox as mb


class Start(Frame):
    def __init__(self, parent):
        super(Start, self).__init__()
        self.parent = parent
        self.main_window_setting()
        self.f_main = Frame(self.parent)
        self.f_main.pack(expand=1, fill=BOTH)
        self.button_plus_minus = Button(self.f_main, text='Сложение', command=self.call_UnitPlusMinus)
        self.button_plus_minus.pack()

    def call_UnitPlusMinus(self):
        self.f_main.destroy()
        self.button_plus_minus.destroy()
        UnitPlusMinus(self.parent)

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


class UnitPlusMinus(Frame):
    def __init__(self, parent):
        super(UnitPlusMinus, self).__init__()
        self.parent = parent
        self.main_window_setting()

        # Main для основных действий программы, system - для вспомогательных
        self.f_main = LabelFrame(self.parent, text='1')
        self.f_system = LabelFrame(self.parent, text='2')
        self.f_main.pack(expand=1, fill=BOTH)
        self.f_system.pack(anchor=S, expand=0, fill=X)

        # main_menu = Menu(self.parent)
        # self.parent.config(menu=main_menu)
        # main_menu.add_command(label='Сложение/вычитание', command=choose_plus)
        # main_menu.add_command(label='Умножение/деление', command=choose_multi)

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
        button_new_window = Button(self.f_system, text='Главное меню', command=self.call_Start)
        button_new_window.pack(side=LEFT, anchor=W)

        # Забиндили энтер с той же функцией, что и button_answer
        parent.bind("<Return>", self.check_answer_press_enter)
        self.gen()

    def new_window(self):
        a = Toplevel()
        a.geometry('200x200')
        Label(a, text='лошадь').pack()
        button_quit1 = Button(a, text='Закрыть', command=self.quit)
        button_quit1.pack(side=RIGHT, anchor=E)

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

    def call_Start(self):
        self.f_main.destroy()
        self.f_system.destroy()
        Start(self.parent)


def main():
    main_window = Tk()
    app = Start(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    main()
