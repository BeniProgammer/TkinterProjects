from tkinter import *
from tkinter import messagebox as tkmsg
import os

root = Tk()
root.geometry("800x550")
root.title("Menus and Submenus")
def help():
    print("Helping")
    msg = tkmsg.showwarning("Help", "This is a program created by Beni with Python")
def feedback():
    b = tkmsg.askquestion("Feedback", "Was your experience good?")
    print(b)
    if b == "yes":
        msg = "That's great Please do rate us on appstore."
    else:
        msg = "Please tell us what went wrong, we will try to improve."
    tkmsg.showinfo("Feedback",msg)
def contact():
    tkmsg.showinfo("Contact", "You Can contact us on WhatsApp and Call at 9810802217")

def error():
    tkmsg.showerror("Error 404","The Developer hasn't added this Feature yet")

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="Save",command=error)
m1.add_command(label="Save as",command=error)
m1.add_command(label="Print",command=error)
m1.add_separator()
m1.add_command(label="Open file",command=error)
m1.add_command(label="New File",command=error)
m1.add_command(label="Delete File",command=error)
m1.add_separator()
m1.add_command(label="New Folder",command=error)
m1.add_command(label="Open Folder",command=error)
m1.add_command(label="Delete Folder",command=error)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut",command=error)
m2.add_command(label="Copy",command=error)
m2.add_command(label="Paste",command=error)
m2.add_command(label="Find",command=error)
m2.add_separator()
m2.add_command(label="Undo",command=error)
m2.add_command(label="Redo",command=error)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Feedback", command=feedback)
m3.add_command(label="Call the Developer", command=contact)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)

root.mainloop()