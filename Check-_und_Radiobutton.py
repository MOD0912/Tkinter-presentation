from tkinter import *
 
root = Tk()
root.geometry("200x150")
def sel():
    print("hi")
Var1 = IntVar()
Var2 = IntVar()
 
ChkBttn = Checkbutton(  variable = Var2, width = 15, text = "checkbutton")
ChkBttn.pack(padx = 5, pady = 5)
Radiobutton( text="Radiobutton1", padx = 5, variable=Var1, value=1).pack()
Radiobutton( text="Radiobutten2" ,padx = 5, variable=Var1, value=2).pack()

root.mainloop()