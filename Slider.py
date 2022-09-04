from tkinter import messagebox as tkmsg
from tkinter import *
import time

root = Tk()
root.geometry("455x233")

def getdollars():
    tkmsg.showinfo("Information",f"{slider.get()} Dollars have been credited to your bank account")
Label(root, text="How many dollars do you want?",font="comicsansms 15 bold").pack()

slider= Scale(root, from_=0,to=1000, orient=HORIZONTAL)
slider.pack()

Button(root, text="Claim now!",font="comicsansms 10 bold", command=getdollars).pack()

root.mainloop()