from tkinter import *
from tkinter import messagebox as tkmsg 

root = Tk()
root.geometry("455x150")
root.title("Please Rate us")

def getval():
    if mainslider.get() >= 6:
        tkmsg.showinfo("Thanks for Rating","Thanks for your Valuable feedback")
    else:
        tkmsg.showinfo("Thanks for rating",'We respect your feedback Please contact us for your issues')
    with open("servicevalue.txt","a") as f:
        f.write(f"{mainslider.get()}\n")

Label(root, text="On a scale of 1 to 10, How do you rate us?",font="comicsansms 15 bold").pack()
mainslider = Scale(root, from_=0, to=10, orient=HORIZONTAL, tickinterval=1, length=400)
mainslider.set(5)
mainslider.pack()
Button(root, text="Give Rating!", font="comicsansms 10 bold", command=getval, pady=10).pack()

root.mainloop()