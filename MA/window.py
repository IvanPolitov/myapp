import mymath
import tkinter

if __name__ == '__main__':
    main_window = tkinter.Tk()
    main_window.title("Математика")
    main_window.geometry('800x600')

    lb1 = tkinter.Label(main_window, text="Пример: ")
    lb1.grid(column=0, row=0)

    lb2 = tkinter.Label(main_window, text="1+1=")
    lb2.grid(column=1, row=0)

    main_window.mainloop()
