import mymath
from tkinter import *
from tkinter import messagebox as mb

BUTTON_W_MAIN_MENU = 170
BUTTON_H_MAIN_MENU = 40
GUIDE_TXT_FILE = 'guide_text.txt'


def call_Guide():
    file = open(GUIDE_TXT_FILE, 'r', encoding='utf-8')
    txt = file.read()
    file.close()
    wdw = Toplevel()
    Label(wdw, text=txt, font="Arial 11").pack(expand=1)
    Button(wdw, text='Закрыть', command=wdw.destroy, font="Arial 14").pack(side=RIGHT)


class MainWindow(Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__()
        self.pixelVirtual = PhotoImage(width=1, height=1)
        self.parent = parent

        self.window_setting()

        self.units_list = []

        self.UnitAdd = UnitAdd(self.parent)
        self.units_list.append(self.UnitAdd)

        self.UnitMulti = UnitMulti(self.parent)
        self.units_list.append(self.UnitMulti)

        self.UnitDiv = UnitDiv(self.parent)
        self.units_list.append(self.UnitDiv)

        self.MainMenu = MainMenu(self.parent, self.units_list)
        self.units_list.append(self.MainMenu)

        self.call_window(self.MainMenu)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        file_menubar = Menu(menubar, tearoff=0)
        file_menubar.add_command(label='О программе')
        file_menubar.add_command(label='Выход', command=quit)

        unit_menubar = Menu(menubar, tearoff=0)
        unit_menubar.add_command(label='Главное меню', command=lambda: self.call_window(self.MainMenu))
        unit_menubar.add_separator()
        unit_menubar.add_command(label='Сложение', command=lambda: self.call_window(self.UnitAdd))
        unit_menubar.add_command(label='Умножение', command=lambda: self.call_window(self.UnitMulti))
        unit_menubar.add_command(label='Деление', command=lambda: self.call_window(self.UnitDiv))

        menubar.add_cascade(label='Файл', menu=file_menubar)
        menubar.add_cascade(label='Выбор раздела', menu=unit_menubar)
        menubar.add_command(label='Справка', command=call_Guide)

    def call_window(self, name):
        for i in self.units_list:
            i.MainFrame_pack_forget()
        name.MainFrame_pack()

    def window_setting(self):
        """Размер окна и центрирование"""
        w = 565
        h = 400
        self.parent['bg'] = 'green'
        self.parent.title("Математика")
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.parent.resizable(False, False)
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


class MainMenu(Frame):
    def __init__(self, parent, units_list):
        super(MainMenu, self).__init__()
        self.parent = parent
        self.units_list = units_list
        self.pixelVirtual = PhotoImage(width=1, height=1)

        self.MainFrame = Frame(self.parent, bg='green')
        frame_btn_add_mult_div = Frame(self.MainFrame, bg='green')
        frame_btn_add_mult_div.pack(expand=1, fill=X)

        frame_btn_another = Frame(self.MainFrame, bg='green')
        frame_btn_another.pack(expand=1, fill=X, ipady=5)

        button_add = Button(frame_btn_add_mult_div,
                            text='Сложение',
                            command=lambda: self.call_window(self.units_list[0]),
                            image=self.pixelVirtual,
                            width=BUTTON_W_MAIN_MENU,
                            height=BUTTON_H_MAIN_MENU,
                            compound='center',
                            font="Arial 20")

        button_multiply = Button(frame_btn_add_mult_div,
                                 text='Умножение',
                                 command=lambda: self.call_window(self.units_list[1]),
                                 image=self.pixelVirtual,
                                 width=BUTTON_W_MAIN_MENU,
                                 height=BUTTON_H_MAIN_MENU,
                                 compound='center',
                                 font="Arial 20")

        button_div = Button(frame_btn_add_mult_div,
                            text='Деление',
                            command=lambda: self.call_window(self.units_list[2]),
                            image=self.pixelVirtual,
                            width=BUTTON_W_MAIN_MENU,
                            height=BUTTON_H_MAIN_MENU,
                            compound='center',
                            font="Arial 20")

        button_f1 = Button(frame_btn_another,
                           text='f1',
                           # command=self.call_window(self.units_list[0]),
                           image=self.pixelVirtual,
                           width=BUTTON_W_MAIN_MENU,
                           height=BUTTON_H_MAIN_MENU,
                           compound='center',
                           font="Arial 20")

        button_f2 = Button(frame_btn_another,
                           text='f2',
                           # command=self.call_window(self.units_list[0]),
                           image=self.pixelVirtual,
                           width=BUTTON_W_MAIN_MENU,
                           height=BUTTON_H_MAIN_MENU,
                           compound='center',
                           font="Arial 20")

        button_f3 = Button(frame_btn_another,
                           text='f3',
                           # command=self.call_window(self.units_list[0]),
                           image=self.pixelVirtual,
                           height=BUTTON_H_MAIN_MENU,
                           width=BUTTON_W_MAIN_MENU,
                           compound='center',
                           font="Arial 20")
        button_quit = Button(self.MainFrame,
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

    def call_window(self, name):
        for i in self.units_list:
            i.MainFrame_pack_forget()
        name.MainFrame_pack()

    def MainFrame_pack(self):
        self.MainFrame.pack(expand=1, fill=X)

    def MainFrame_pack_forget(self):
        self.MainFrame.pack_forget()


class UnitWindow(Frame):
    def __init__(self, parent):
        super(UnitWindow, self).__init__()
        self.parent = parent
        self.result = 0
        self.pixelVirtual = PhotoImage(width=1, height=1)

        self.MainFrame = Frame(self.parent)
        self.f_main = Frame(self.MainFrame, bg='green')
        self.f_system = Frame(self.MainFrame)

        self.f_main.pack(expand=1, fill=BOTH)
        self.f_system.pack(anchor=S, expand=0, fill=X)

        self.example = Label(self.f_main, font='Arial 20', width=7)
        self.example.pack(side=LEFT, anchor=NW)

        self.user_result = Entry(self.f_main, font='Arial 20', width=7)
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

        self.gen()

    def MainFrame_pack(self):
        self.MainFrame.pack(expand=1, fill=BOTH)

    def MainFrame_pack_forget(self):
        self.MainFrame.pack_forget()

    def check_answer(self):
        if self.check_isdigit():
            if self.user_result.get() == self.result:
                self.gen()
                self.user_result.delete(0, END)
            else:
                mb.showwarning("Неверно", "Неправильный ответ")

    def check_isdigit(self):
        s = self.user_result.get()
        if s != '' and (s.isdigit() or s[0] == '-' and s[1:].isdigit()):
            return True
        else:
            mb.showerror("Ошибка", "Введите число")
            return False

    def gen(self):
        self.example['text'], self.result = mymath.gen_plus_minus()


class UnitAdd(UnitWindow):
    def gen(self):
        self.example['text'], self.result = mymath.gen_plus_minus()


class UnitMulti(UnitWindow):
    def gen(self):
        self.example['text'], self.result = mymath.gen_multiply()


class UnitDiv(UnitWindow):
    def gen(self):
        self.example['text'], self.result = mymath.gen_division()

def main():
    main_window = Tk()
    app = MainWindow(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    main()
