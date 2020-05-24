from tkinter import *
root=Tk()

root.geometry("700x700")

def hello():
    print("hello tkinter button")

def name():
    print("Name is vivek")

frame = Frame(root,borderwidth=5,bg="grey",relief=SUNKEN)
frame.pack(side=RIGHT,anchor="nw")

b1=Button(frame,fg="red",text="Press1",command=hello)
b1.pack(padx=23,side=LEFT)

b2=Button(frame,fg="red",text="Press2",command=name)
b2.pack(padx=23,side=LEFT)

root.mainloop()
