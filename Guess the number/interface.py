from tkinter import *
import time
import random

MIN = 1
MAX = 1000
numb = random.randrange(1, 1000)

def start():


    after_start = Label(window, text='Ok \n You need to guess a number from 1 to 999 \n'
                                     ' I will offer you a version \n'
                                     'And you have to push button "<" or ">" \n'
                                     'So my first version is:', font=('Arial', 14), bg='Grey')
    after_start.grid(column=0, row=3, columnspan=3)
    version = Label(window, text=numb, font=("Arial Bold", 28), bg='Grey')
    version.grid(column=1, row=5)

    def min():
        global numb
        global MAX
        MAX = numb
        numb += MIN
        numb /= 2
        version.configure(text='{}'.format(int(numb)))

    def max():
        global numb
        global MIN
        MIN = numb
        numb += MAX
        numb /= 2
        version.configure(text='{}'.format(int(numb)))

    empty2 = Label(window, text=' ', bg='Grey')
    empty2.grid(column=0, row=2)
    empty = Label(window, text=' ', bg='Grey')
    empty.grid(column=0, row=4)
    button_min = Button(window, text='<', bg='Green', command=min, font=('Arial', 14))
    button_min.grid(column=0, row=5)
    button_max = Button(window, text='>', bg='Green', command=max, font=('Arial', 14))
    button_max.grid(column=2, row=5)




window = Tk()
window.title('Guess the number',)
lbl = Label(window, text='THIS PROGRAM WILL GUESS YOUR NUMBER', font=('Arial', 20), bg='Grey')
lbl.grid(column=0, row=0, columnspan=3)
window.geometry('640x480')
window.config(bg='Grey')
but = Button(window, text='START!', bg='Red', command=start, font=('Arial', 18))
but.grid(column=0, row=1, columnspan=3)


window.mainloop()