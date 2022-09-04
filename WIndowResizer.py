from tkinter import *

root = Tk()
root.title("window resizer")

root.geometry("650x300")

def setvalue():
    SET_WIDTH = widthvalue.get()
    SET_HEIGHT = heightvalue.get()
    root.geometry(f"{SET_WIDTH}x{SET_HEIGHT}")
    widthvalue.set(0)
    heightvalue.set(0)

l1 = Label(root,text="Window resizer GUI",font="verdana 22 bold",bg="light blue")
l1.grid(row=0,column=3)

l2 = Label(root,text="Width -",font="verdana 15 italic",bg="light green")
l2.grid(row=2,column=1,pady=20)

l3 = Label(root, text="Height -",font="verdana 15 italic",bg="light green")
l3.grid(row=4,column=1,pady=20)

widthvalue = StringVar()
heightvalue = StringVar()

widthEntry = Entry(root, textvariable=widthvalue)
heightentry  = Entry(root, textvariable=heightvalue)
widthEntry.grid(row=2,column=2)
heightentry.grid(row=4,column=2)

b1 = Button(root, text="Apply Settings", font="verdana 10 bold", command=setvalue)
b1.grid(row=6,column=2)

root.mainloop()