from tkinter import *
from tkinter import messagebox as tkmsg

root = Tk()
root.geometry("500x200")
def order():
    if a.get()=="Radio":
        tkmsg.showerror("No order received","Sorry we did not receive your order")
    else:
        tkmsg.showinfo("Thanks for ordering",f"We have received your order of {a.get()}.\nIt will arrive soon.")

a = StringVar()
a.set("Radio")

label = Label(root, text="What would you like to order?",font="comicsansms 15 bold").pack()

radio = Radiobutton(root, text="Rajma-Rice",font="comicsansms 8 bold",variable=a, value="Rajma-Rice", padx=14).pack(anchor="w")
radio = Radiobutton(root, text="Maggi",variable=a,font="comicsansms 8 bold",value="Maggi", padx=14).pack(anchor="w")
radio = Radiobutton(root, text="McDonalds Burger",font="comicsansms 8 bold",variable=a, value="A McDonalds Burger", padx=14).pack(anchor="w")
radio = Radiobutton(root, text="Diet Coke",font="comicsansms 8 bold",variable=a, value="A Diet Coke", padx=14).pack(anchor="w")

Button(root, text="Order now!",font="comicsansms 10 bold", command=order).pack()
root.mainloop()