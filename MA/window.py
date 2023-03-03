import mymath
from tkinter import *


class UnitPlusMinus(Frame):
    def __init__(self, parent):
        super(UnitPlusMinus, self).__init__()
        self.parent = parent
        #self.center_window()
        self.init_ui()

    def center_window(self):
        """Размер окна и центрирование"""
        w = 300
        h = 200

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def init_ui(self):
        self.parent.title("Математика")

        f_main = LabelFrame(self.parent, text='Main block')
        f_system = LabelFrame(self.parent, text='system')
        f_main.pack(expand=1, fill=BOTH)
        f_system.pack(expand=1, fill=X)

        example = Label(f_main, text='example')
        example.pack()
        button_quit = Button(f_system, text='Закрыть', command=self.quit)
        button_quit.pack()


def main():
    main_window = Tk()
    app = UnitPlusMinus(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    main()
