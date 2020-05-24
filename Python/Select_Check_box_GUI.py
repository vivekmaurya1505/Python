from tkinter import *
master = Tk() 
var1 = IntVar()
print (var1)
a=Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
print(a)
var2 = IntVar()
print (var2)
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)

mainloop() 

