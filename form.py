from tkinter import *
import sys
import time 

root = Tk()
root.geometry('450x250')

def quit():
    time.sleep(0.5)
    sys.exit()

def getval():
    print(f"The Username is {userentry.get()}")
    print(f"The password is {passentry.get()}")

l1 = Label(root, text="Username -", font="comicsansms 15 italic")
l1.grid()
l2 = Label(root, text="Password -", font="comicsansms 15 italic",pady = 30)
l2.grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0,column=1,padx=20)
passentry.grid(row=1,column=1)

b1 = Button(text="Submit", command=getval, width=10, height=2,relief=GROOVE,borderwidth=
4, font = "comicsansms 12 italic")
b1.grid()

b2 = Button(text="Quit",command=quit, width=10, height=2,relief=GROOVE,borderwidth=4
, font = "comicsansms 12 italic")
b2.grid()

root.mainloop()