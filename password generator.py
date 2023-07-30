from msilib.schema import CheckBox
import random
from tkinter import *
import tkinter


# creating a window.
window = Tk()

# providing the title of the window.
window.title("Random Password Generator (using Python)")

# setting the size of the window.
window.geometry("600x600")

# adding a label
Label(window, font=('bold', 8), text='Generate Password').pack()


# converting the length into an integer.
length1 = tkinter.IntVar()
length2 = tkinter.IntVar()
length3 = tkinter.IntVar()
length4 = tkinter.IntVar()
length5 = tkinter.IntVar()
length6 = tkinter.IntVar()
length7 = tkinter.IntVar()
length8 = tkinter.IntVar()
length9 = tkinter.IntVar()
length10 = tkinter.IntVar()
length11 = tkinter.IntVar()
length12 = tkinter.IntVar()
length13 = tkinter.IntVar()
length14 = tkinter.IntVar()
length15 = tkinter.IntVar()
length20 = tkinter.IntVar()
length30 = tkinter.IntVar()
length40 = tkinter.IntVar()
length50 = tkinter.IntVar()


# function to generate random password
def passwordGeneration(n):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_'

    # generating random password ans strong it
    password = ''.join(random.sample(characters, n))

    # creating a label and adding the password on the label
    l = Label(window, text=password, font=('bold', 15))  # displaying password
    l.place(x=225, y=65)


# getLength function will call the passwordGeneration function
def getLength():
    if length1.get() == 1:
        passwordGeneration(1)
    elif length2.get() == 2:
        passwordGeneration(2)
    elif length3.get() == 3:
        passwordGeneration(3)
    elif length4.get() == 4:
        passwordGeneration(4)
    elif length5.get() == 5:
        passwordGeneration(5)
    elif length6.get() == 6:
        passwordGeneration(6)
    elif length7.get() == 7:
        passwordGeneration(7)
    elif length8.get() == 8:
        passwordGeneration(8)
    elif length9.get() == 9:
        passwordGeneration(9)
    elif length10.get() == 10:
        passwordGeneration(10)
    elif length11.get() == 11:
        passwordGeneration(11)
    elif length12.get() == 12:
        passwordGeneration(12)
    elif length13.get() == 13:
        passwordGeneration(13)
    elif length14.get() == 14:
        passwordGeneration(14)
    elif length15.get() == 15:
        passwordGeneration(15)
    elif length20.get() == 20:
        passwordGeneration(20)
    elif length30.get() == 30:
        passwordGeneration(30)
    elif length40.get() == 40:
        passwordGeneration(40)
    else:
        passwordGeneration(50)




# creating buttons
Button(window, text='Generate Password', font=('normal', 10),
       bg='blue', command=getLength).place(x=230, y=100)


# creating checkboxes
Checkbutton(text='1 character', onvalue=1, offvalue=0,
            variable=length1).place(x=250, y=150)
Checkbutton(text='2 character', onvalue=2, offvalue=0,
            variable=length2).place(x=250, y=170)
Checkbutton(text='3 character', onvalue=3, offvalue=0,
            variable=length3).place(x=250, y=190)
Checkbutton(text='4 character', onvalue=4, offvalue=0,
            variable=length4).place(x=250, y=210)
Checkbutton(text='5 character', onvalue=5, offvalue=0,
            variable=length5).place(x=250, y=230)
Checkbutton(text='6 character', onvalue=6, offvalue=0,
            variable=length6).place(x=250, y=250)
Checkbutton(text='7 character', onvalue=7, offvalue=0,
            variable=length7).place(x=250, y=270)
Checkbutton(text='8 character', onvalue=8, offvalue=0,
            variable=length8).place(x=250, y=290)
Checkbutton(text='9 character', onvalue=9, offvalue=0,
            variable=length9).place(x=250, y=310)
Checkbutton(text='10 character', onvalue=10, offvalue=0,
            variable=length10).place(x=250, y=330)
Checkbutton(text='11 character', onvalue=11, offvalue=0,
            variable=length11).place(x=250, y=350)
Checkbutton(text='12 character', onvalue=12, offvalue=0,
            variable=length12).place(x=250, y=370)
Checkbutton(text='13 character', onvalue=13, offvalue=0,
            variable=length13).place(x=250, y=390)
Checkbutton(text='14 character', onvalue=14, offvalue=0,
            variable=length14).place(x=250, y=410)
Checkbutton(text='15 character', onvalue=15, offvalue=0,
            variable=length15).place(x=250, y=430)
Checkbutton(text='20 character', onvalue=20, offvalue=0,
            variable=length20).place(x=250, y=450)
Checkbutton(text='30 character', onvalue=30, offvalue=0,
            variable=length30).place(x=250, y=470)
Checkbutton(text='40 character', onvalue=40, offvalue=0,
            variable=length40).place(x=250, y=490)
Checkbutton(text='50 character', onvalue=50, offvalue=0,
            variable=length50).place(x=250, y=510)



window.mainloop()
