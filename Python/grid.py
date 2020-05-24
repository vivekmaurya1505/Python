from tkinter import *
import tkinter as tk
root=Tk()

root.title("Grid")
root.geometry("700x700")

def getvals():
    
    print(userentry.get())
    print(passentry.get())
    print(f"the value of username is{userentry.get()}")
    print(f"the value of password is {passentry.get()}")

user = tk.Label(root,text="User Name")
password= Label(root,text="Password")

user.grid(row=0)
password.grid(row=1)

userentry=Entry(root)
passentry=Entry(root)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(root,text="Show",command=getvals).grid(row=2,column=0,pady=4)
Button(root,text="Quit",command=getvals).grid(row=2,column=1,pady=4)
root.mainloop()
