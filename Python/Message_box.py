from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("hello")
root.iconbitmap("icon.ico")

#showinfo ,showwarning,showerror ,askquestion ,askokcancel,askyesno

def popup():
    response = messagebox.showinfo("This is my popup","Hello World!")
    Label(root,text = response).pack()
    
Button(root,text = "popup",command = popup).pack()


def popup1():
    response = messagebox.askquestion("This is my popup1","Hello World!")
    Label(root,text = response).pack()
    
Button(root,text = "popup1",command = popup1).pack()


def popup2():
    response = messagebox.askyesno("This is my popup2","Hello World!")
    Label(root,text = response).pack()
    
Button(root,text = "popup2",command = popup2).pack()


def popup3():
    response = messagebox.askokcancel("This is my popup3","Hello World!")
    Label(root,text = response).pack()
    
Button(root,text = "popup3",command = popup3).pack()

def popup4():
    response = messagebox.showerror("This is my popup4","Hello World!")
    Label(root,text = response).pack()
    
Button(root,text = "popup4",command = popup4).pack()

def popup5():
    response = messagebox.showwarning("This is my popup5","Hello World!")
    Label(root,text = response).pack()
    
Button(root,text = "popup5",command = popup5).pack()
root.mainloop()
