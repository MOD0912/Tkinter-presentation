from tkinter import *
from PIL import ImageTk, Image
from win32api import GetSystemMetrics
def bg_colour():
    canvas.config(bg = "light grey")
h1 = GetSystemMetrics(1)
root = Tk()
img = ImageTk.PhotoImage(Image.open("HTL-Anichstrasse.png"))

frame=Frame(root,width=300,height=300)
frame.pack(expand = True, fill=BOTH)

root.wm_attributes("-fullscreen", True)
canvas = Canvas(frame,bg='white', width = 300,height = 300)
canvas.create_image(250,h1-50,image = img)
label = Label(canvas, image = img).pack(anchor = "s", side = "right")
coordinates = 20, 50, 210, 230

button = Button(canvas, text = "bg color changer", font = ("Ariel", 50),command = bg_colour)
button.pack()
arc = canvas.create_arc(coordinates, start=0, extent=250, fill="blue")
arc = canvas.create_arc(coordinates, start=250, extent=50, fill="red")
arc = canvas.create_arc(coordinates, start=300, extent=60, fill="yellow")
 
canvas.pack(expand = True, fill = BOTH)
 
root.mainloop()