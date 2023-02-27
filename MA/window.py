import mymath
import tkinter


def create_lb2_lb3():
    lb2['text'], lb3['text'] = mymath.gen_plus_minus()


def check_Entry():
    if txt.get() == lb3['text']:
        txt.delete(0, tkinter.END)
        create_lb2_lb3()


if __name__ == '__main__':
    main_window = tkinter.Tk()
    main_window.title("Математика")
    main_window.geometry('800x600')

    lb1 = tkinter.Label(main_window, text="Пример: ")
    lb1.grid(column=0, row=0)

    btn = tkinter.Button(main_window, text='Генерировать', command=create_lb2_lb3)
    btn.grid(column=0, row=1)

    btn1 = tkinter.Button(main_window, text='Проверка', command=check_Entry)
    btn1.grid(column=2, row=1)

    lb2 = tkinter.Label(main_window, text='')
    lb2.grid(column=1, row=0)

    txt = tkinter.Entry(main_window, width=10)
    txt.grid(column=2, row=0)

    lb3 = tkinter.Label(main_window, text='')
    lb3.grid(column=3, row=0)

    main_window.mainloop()
