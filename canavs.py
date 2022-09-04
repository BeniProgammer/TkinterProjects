from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

widget = Canvas(root, height=canvas_height, width=canvas_width)
widget.pack()

#the line goes from x1,y1 to x2,y2
#widget.create_line(200,500,200,0)
widget.create_rectangle(700,300,100,80,fill="light blue")
widget.create_text(400,180,text="Python",font="verdana 30 bold")
root.mainloop()
