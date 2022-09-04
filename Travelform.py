from tkinter import *


def getval():
    print(f"{namevalue.get()}")
    print(f"{phonevalue.get()}")
    print(f"{gendervalue.get()}")
    print(f"{vehiclevalue.get()}")
    print(f"{foodservicevalue.get()}")

    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), vehiclevalue.get(), foodservicevalue.get()}\n")

root = Tk()

root.geometry("550x225")
root.minsize(550,225)
root.maxsize(550,250)

l1 = Label(root, text="Welcome to Al-Habibi Travels!",font="verdaba 20 bold",pady=15)
l1.grid(row=0, column=3)

name = Label(root, text="Name -",font="verdana 10 bold")
phone = Label(root, text="Phone -",font="verdana 10 bold")
gender = Label(root, text="Gender -",font="verdana 10 bold")
vehicle = Label(root, text="Vehicle -",font="verdana 10 bold")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
vehicle.grid(row=4,column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
vehiclevalue = StringVar()
foodservicevalue = IntVar()

name_entry = Entry(root,textvariable=namevalue)
phone_entry = Entry(root,textvariable=phonevalue)
gender_entry = Entry(root,textvariable=gendervalue)
vehicle_entry = Entry(root,textvariable=vehiclevalue)

name_entry.grid(row=1,column=3)
phone_entry.grid(row=2,column=3)
gender_entry.grid(row=3,column=3)
vehicle_entry.grid(row=4,column=3)

foodservice = Checkbutton(text="Food Service(Optional)", variable=foodservicevalue,font="verdana 10 bold")
foodservice.grid(row=6,column=3)

btn = Button(text="Submit to CEO", font="verdana 10 bold", command=getval)
btn.grid(row = 8, column=3)

root.mainloop()