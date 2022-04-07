from tkinter import*
from win32api import GetSystemMetrics
w1 = GetSystemMetrics(0)
h1 = GetSystemMetrics(1)
def NewWindow():
    window = Toplevel()

    label = Label(window, text = "Child(Slave) window", font = ("Ariel", 100)).pack()
    
    window.title("Child(Slave) window")
 
 
root = Tk()
root.wm_attributes("-fullscreen", True)
 
myframe = Frame(root)
myframe.place(x = 0, y = 0, width = w1, height = h1)

label = Label(myframe, text = "Parent(Master) window", font = ("Raleway", 100)).pack(pady = 100)

destroy = Button(myframe, text = "destroy window", command = root.destroy, bg = "blue", activebackground = "blue", font = ("Ariel", 50)).pack()

mybutton = Button(myframe, text = "Child(Slave)", command = NewWindow, width = 13,  bg = "blue", activebackground = "blue", font = ("Ariel", 50)).pack()

root.mainloop()