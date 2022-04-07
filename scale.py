from tkinter import *
from win32api import GetSystemMetrics 
def resize_window():
    width = Scala2.get()
    height = Scala.get()
    width = str(width)
    height = str(height)
    root.geometry(height + "x" + width)


w1 = GetSystemMetrics(0)
h1 = GetSystemMetrics(1)
root = Tk()
root.geometry("200x200")
frame = Frame(root)
frame.pack()

Scala = Scale(frame, from_ = 0, to = w1, orient = HORIZONTAL)
Scala.pack(padx = 5, pady = 5)
Scala.set(200)

Scala2 = Scale(frame, from_ = 0, to = h1, orient = VERTICAL)
Scala2.pack(padx = 5, pady = 5)
Scala2.set(200)

button = Button(text = "resize Window", bd = 5, command = resize_window)
button.pack(padx = 5, pady = 5)
root.mainloop()