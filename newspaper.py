from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Al-Habibi News")
root.geometry("1050x800")

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%60==0 and i!=0:
            final_text += "\n"
    return final_text

texts = []
photos =[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f'{i+1}.png')
    image = image.resize((330,220), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, height=70,width=800)
Label(f0,text="Python Times News",font="verdana 33 bold").pack()
f0.pack()
f1 = Frame(root, height=70,width=800)
Label(f1,text="8 August 2022",font="verdana 18 bold").pack()
f1.pack()

frame1 = Frame(root,height=200,width = 900)
Label(frame1, text=texts[0],pady=30,padx=30,font="verdana 14 italic",bg="light blue").pack(side=LEFT)
frame1.pack(anchor="w")
Label(frame1, image=photos[0],anchor="e").pack()

frame1 = Frame(root,height=200,width = 900)
Label(frame1, text=texts[1],pady=30,padx=30,font="verdana 14 italic",bg="light blue").pack(side=LEFT,padx = 55)
frame1.pack(anchor="w")
Label(frame1, image=photos[1],anchor="e").pack()

frame1 = Frame(root,height=200,width = 900)
Label(frame1, text=texts[2],padx=30,font="verdana 14 italic",bg="light blue").pack(side=LEFT)
frame1.pack(anchor="w")
Label(frame1, image=photos[2],anchor="e").pack()


root.mainloop()