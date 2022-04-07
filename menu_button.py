from tkinter import *
def prnt(essen):
    print(essen)
root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

MenuBttn = Menubutton(frame, text = "Favourite food", relief = RAISED)
 
Menu1 = Menu(MenuBttn, tearoff = 0)
 
Menu1.add_checkbutton(label = "Pizza", command = lambda: prnt("Pizza"))
Menu1.add_cascade(label = "Burger", command = lambda: prnt("Burger"))
Menu1.add_command(label = "Both of the aboth",command = lambda: prnt("Both of the aboth"))
Menu1.add_radiobutton(label = "all of the above",command = lambda: prnt("all of the above"))
MenuBttn["menu"] = Menu1

MenuBttn.pack()
root.mainloop()