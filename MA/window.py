import mymath
from tkinter import *
from tkinter import messagebox as mb

BUTTON_W_MAIN_MENU = 170
BUTTON_H_MAIN_MENU = 40
GUIDE_TXT_FILE = 'guide_text.txt'

class MainWindow(Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__()
        self.pixelVirtual = PhotoImage(width=1, height=1)
        self.parent = parent
        self.window_setting()
        self.make_MainMenu()

        self.parent.bind("<q>", self.quit)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        file_menubar = Menu(menubar, tearoff=0)
        file_menubar.add_command(label='О программе')
        file_menubar.add_command(label='Выход', command=quit)

        menubar.add_cascade(label='Файл', menu=file_menubar)
        menubar.add_command(label='Справка', command=self.call_Guide)

    def call_Guide(self):
        file = open(GUIDE_TXT_FILE, 'r', encoding='utf-8')
        txt = file.read()
        file.close()
        wdw = Toplevel()
        Label(wdw, text=txt, font="Arial 11").pack(expand=1)
        Button(wdw, text='Закрыть', command=wdw.destroy, font="Arial 14").pack(side=RIGHT)

    def vihod(self, event):
        self.quit()

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


    def call_UnitAdd(self):
        self.frame_MainMenu.pack_forget()
        self.q = UnitWindow(self.parent)

    def call_MainMenu(self):
        self.frame_MainMenu.pack(expand=1, fill=X)

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

class UnitWindow(Frame):
    def __init__(self, parent):
        super(UnitWindow, self).__init__()
        self.parent = parent
        self.result = 0

        self.UnitFrame = Frame(self.parent)
        self.UnitFrame.pack(expand=1, fill=BOTH)
        self.f_main = Frame(self.UnitFrame)
        self.f_system = Frame(self.UnitFrame)
        #
        # self.f_main = Frame(self.parent)
        # self.f_system = Frame(self.parent)
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

        # Кнопка для генерации нового окна
        # button_new_window = Button(self.f_system, text='Главное меню', command=self.call_MainMenu)
        # button_new_window.pack(side=LEFT, anchor=W)

        # Забиндили энтер с той же функцией, что и button_answer
        # self.parent.bind("<Return>", self.check_answer_press_enter)

        self.gen()

    def check_answer(self):
        if self.check_isdigit():
            if self.user_result.get() == self.result:
                self.gen()
                self.user_result.delete(0, END)
            else:
                mb.showwarning("Неверно", "Неправильный ответ")

    def check_answer_press_enter(self, event):
        self.check_answer()

    def check_isdigit(self):
        s = self.user_result.get()
        if s != '' and (s.isdigit() or s[0] == '-' and s[1:].isdigit()):
            return True
        else:
            mb.showerror("Ошибка", "Введите число")
            return False

    def gen(self):
        self.example['text'], self.result = mymath.gen_plus_minus()



def main():
    main_window = Tk()
    app = MainWindow(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    main()
