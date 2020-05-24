'''
from tkinter import *

master = Tk()

variable = StringVar(master)
variable.set("one") # default value

w = OptionMenu(master, variable, "one", "two", "three")
w.pack()

mainloop()
'''
#=====================================================
'''
from tkinter import *

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

mainloop()
'''
#==================================================
'''
from tkinter import *

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def ok():
    print ("value is:" + variable.get())

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()
'''
#========================================================
'''
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Hello Vivek maurya")
root.geometry("400x400")

def selected ():
    mylabel = Label(root,text = clicked.get()).pack()

Options = [
    "Vivek",
    "Maurya",
]

clicked = StringVar()
clicked.set(Options[0])

drop = OptionMenu(root,clicked,*Options)
drop.pack(pady = 20)


myButton = Button(root, text = "select from list", command = selected)
myButton.pack()

root.mainloop()
'''
#====================================================
'''
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Hello Vivek maurya")
root.geometry("400x400")

def selected (event):
    mylabel = Label(root,text = clicked.get()).pack()

Options = [
    "Vivek",
    "Maurya",
]

clicked = StringVar()
clicked.set(Options[0])

drop = OptionMenu(root,clicked,*Options,command = selected)
drop.pack(pady = 20)


#myButton = Button(root, text = "select from list", command = selected)
#myButton.pack()

root.mainloop()
'''
#==============================================================
'''
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Hello Vivek maurya")
root.geometry("400x400")

def selected (event):
    mylabel = Label(root,text = clicked.get()).pack()
def comboclick(event):
     mylabel = Label(root,text = myCombo.get()).pack()
Options = [
    "Vivek",
    "Maurya",
]

clicked = StringVar()
clicked.set(Options[0])

drop = OptionMenu(root,clicked,*Options,command = selected)
drop.pack(pady = 20)

myCombo = ttk.Combobox(root,value = Options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>",comboclick)
myCombo.pack()
root.mainloop()
'''
#==================================================================
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Hello Vivek maurya")
root.geometry("400x400")

   
def comboclick(event):
     myLabel = Label(root,text = myCombo.get()).pack()
     #print(myCombo.get())
     
Options = [
    "Vivek",
    "Maurya",
]

clicked = StringVar()
clicked.set(Options[0])

myCombo = ttk.Combobox(root,value = Options,width = 50)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>",comboclick)
myCombo.pack()
root.mainloop()
















    
    
