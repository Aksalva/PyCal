'''PyCalc v0.1
This is a calculator with a basic GUI built on Python-Tkinter.
This is the first build and hence may have unoptimized code or unexpected behaviour.
Made By Gorakh Nath Sharma
'''

from tkinter import *

#define root (main) window
root = Tk()
root.title("PyCalc v0.1")

#input box definition
e=Entry(root, width=20, borderwidth=5, font="Consolas 22")
e.grid(row=0,column=0, columnspan=4, padx=2, pady=10)

#Insert character in input box

def onclick(inp):
    cur=e.get()     #get expression currrently in input box
    e.delete(0, END)
    e.insert(0, cur+str(inp))

#Function for Calculation

def calc():
    exp=e.get()
    e.delete(0, END)
    try:
        a=eval(exp)
        e.insert(0, a)
    except ZeroDivisionError:
        e.insert(0, "Can't Divide By Zero")
    except:
        e.insert(0, "Invalid Expression")

#Clear the input box

def clear():
    e.delete(0, END)

#Button Dimensions

px=40
py=20

#Button Defintion

key_1 = Button(root, text="1", padx=px, pady=py, command=lambda: onclick(1))
key_2 = Button(root, text="2", padx=px, pady=py, command=lambda: onclick(2))
key_3 = Button(root, text="3", padx=px, pady=py, command=lambda: onclick(3))
key_4 = Button(root, text="4", padx=px, pady=py, command=lambda: onclick(4))
key_5 = Button(root, text="5", padx=px, pady=py, command=lambda: onclick(5))
key_6 = Button(root, text="6", padx=px, pady=py, command=lambda: onclick(6))
key_7 = Button(root, text="7", padx=px, pady=py, command=lambda: onclick(7))
key_8 = Button(root, text="8", padx=px, pady=py, command=lambda: onclick(8))
key_9 = Button(root, text="9", padx=px, pady=py, command=lambda: onclick(9))
key_0 = Button(root, text="0", padx=px, pady=py, command=lambda: onclick(0))
key_dec = Button(root, text=".", padx=px, pady=py, command=lambda: onclick('.'))
key_add = Button(root, text="+", padx=px, pady=py, command=lambda: onclick('+'))
key_sub = Button(root, text="-", padx=px, pady=py, command=lambda: onclick('-'))
key_mul = Button(root, text="*", padx=px, pady=py, command=lambda: onclick('*'))
key_div = Button(root, text="/", padx=px, pady=py, command=lambda: onclick('/'))
key_bro = Button(root, text="(", padx=px, pady=py, command=lambda: onclick('('))
key_brc = Button(root, text=")", padx=px, pady=py, command=lambda: onclick(')'))
key_clc = Button(root, text="=", padx=px, pady=py, command=calc)
key_clr = Button(root, text="CE", padx=px, pady=py, command=clear)

#Putting Button on-screen

key_add.grid(row=1, column=1)
key_sub.grid(row=1, column=2)
key_mul.grid(row=1, column=3)
key_7.grid(row=2, column=0)
key_8.grid(row=2, column=1)
key_9.grid(row=2, column=2)
key_div.grid(row=2, column=3)
key_4.grid(row=3, column=0)
key_5.grid(row=3, column=1)
key_6.grid(row=3, column=2)
key_bro.grid(row=3, column=3)
key_1.grid(row=4, column=0)
key_2.grid(row=4, column=1)
key_3.grid(row=4, column=2)
key_brc.grid(row=4, column=3)
key_dec.grid(row=5, column=0)
key_0.grid(row=5, column=1)
key_clr.grid(row=5, column=2)
key_clc.grid(row=5, column=3)

root.mainloop()