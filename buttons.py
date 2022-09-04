from tkinter import *

root = Tk()
height = 800
width = 600
root.geometry(f"{height}x{width}")

def func1():
    print('This is the Button 1')

def func2():
    print('This is the Button 2')

def func3():
    print('This is the Button 3')

def func4():
    print('This is the Button 4')

f1 = Frame(root, borderwidth=6, bg = "blue", relief=RIDGE)
f1.pack(anchor="nw", side=LEFT)

b1 = Button(f1, text="Button 1", fg="green", command=func1,font="times 10 italic")
b1.pack(side=LEFT)

b2 = Button(f1, text="Button 2", fg="green", command=func2,font="times 10 italic")
b2.pack(side=LEFT)

b3 = Button(f1, text="Button 3", fg="green", command=func3,font="times 10 italic")
b3.pack(side=LEFT)

b4 = Button(f1, text="Button 4", fg="green", command=func4,font="times 10 italic")
b4.pack(side=LEFT)

root.mainloop()