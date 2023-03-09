import mymath
from tkinter import *
from tkinter import ttk


class UnitPlusMinus(Frame):
    def __init__(self, parent):
        super(UnitPlusMinus, self).__init__()
        self.parent = parent
        self.center_window()
        self.parent.title("Математика")


        f_main = LabelFrame(self.parent, text='Main block')
        f_system = LabelFrame(self.parent, text='system')
        f_main.pack(expand=1, fill=BOTH)
        f_system.pack(anchor=S, expand=0, fill=X)

        self.example = Label(f_main, text='example', font="Arial 20")
        self.example.pack(side=LEFT, anchor=NW)
        self.result = 0

        self.user_result = Entry(f_main, font="Arial 20", width=5)
        self.user_result.pack(side=LEFT, anchor=NW)

        button_answer = Button(f_main, text='Ответить', command=self.check_answer, font="Arial 14")
        button_answer.pack(side=LEFT, anchor=NW)

        button_quit = Button(f_system, text='Закрыть', command=self.quit)
        button_quit.pack(side=RIGHT, anchor=E)

        button_generate = Button(f_system, text='Новый пример', command=self.gen)
        button_generate.pack(side=LEFT, anchor=W)

        parent.bind("<Return>", self.check_answer_press_enter)

    def check_answer_press_enter(self, event):
        self.check_answer()
    def center_window(self):
        """Размер окна и центрирование"""
        w = 400
        h = 200

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.parent.resizable(False, False)
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def gen(self):
        self.example['text'], self.result = mymath.gen_plus_minus()

    def check_answer(self):
        if self.user_result.get() == self.result:
            self.gen()
            self.user_result.delete(0, END)


def main():
    main_window = Tk()
    app = UnitPlusMinus(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    main()
