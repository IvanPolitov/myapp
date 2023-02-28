import mymath
import tkinter


class UnitPlusMinus(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()
        self.centerWindow()

    def centerWindow(self):
        w = 300
        h = 200

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
    def initUI(self):
        self.parent.title("Математика")
        self.pack(fill=tkinter.BOTH, expand=1)

        quitButton = tkinter.Button(self, text="Закрыть", command=self.quit, height=1)
        quitButton.place(x=5, y=170)

        frame = tkinter.Frame(self, relief=tkinter.RAISED, borderwidth=1)
        frame.pack(fill=tkinter.BOTH, expand=True)

        self.pack(fill=tkinter.BOTH, expand=True)

        closeButton = tkinter.Button(self, text="Закрыть")
        closeButton.pack(side=tkinter.RIGHT, padx=5, pady=5)
        okButton = tkinter.Button(self, text="Готово")
        okButton.pack(side=tkinter.RIGHT)

def main():
    mainWindow = tkinter.Tk()
    app = UnitPlusMinus(mainWindow)
    mainWindow.mainloop()


# def create_lb2_lb3():
#     lb2['text'], lb3['text'] = mymath.gen_plus_minus()
#
# def check_Entry():
#     if txt.get() == lb3['text']:
#         txt.delete(0, tkinter.END)
#         create_lb2_lb3()


if __name__ == '__main__':
    main()
    #
    # main_window = tkinter.Tk()
    # main_window.title("Математика")
    # main_window.geometry('300x200')
    #
    # lb1 = tkinter.Label(main_window, text="Пример: ")
    # lb1.grid(column=0, row=0)
    #
    # btn = tkinter.Button(main_window, text='Генерировать', command=create_lb2_lb3)
    # btn.grid(column=0, row=1)
    #
    # btn1 = tkinter.Button(main_window, text='Проверка', command=check_Entry)
    # btn1.grid(column=2, row=1)
    #
    # lb2 = tkinter.Label(main_window, text='')
    # lb2.grid(column=1, row=0)
    #
    # txt = tkinter.Entry(main_window, width=10)
    # txt.grid(column=2, row=0)
    #
    # lb3 = tkinter.Label(main_window, text='')
    # lb3.grid(column=3, row=0)
    #
    # create_lb2_lb3()
    # main_window.mainloop()
    #
