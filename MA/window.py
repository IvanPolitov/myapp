import mymath
from tkinter import *


class UnitPlusMinus:
    def __init__(self, parent):
        self.parent = parent
        self.initUI()
        self.centerWindow()
        self.ent = Entry(self, width=20)
        self.ent.pack()


    def centerWindow(self):
        """Размер окна и центрирование"""
        w = 300
        h = 200

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
    def initUI(self):
        self.parent.title("Математика")

def main():
    mainWindow = Tk()
    app = UnitPlusMinus(mainWindow)
    mainWindow.mainloop()


if __name__ == '__main__':
    main()
