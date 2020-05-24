
from tkinter import filedialog
from tkinter import *

root = Tk()
root.title("Select A File")
root.geometry("420x100")
root.minsize(420,100)


def fileDialog():
    global filename
    filename=  filedialog.askopenfilename(initialdir = "/",title = "choose file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
    print (filename)


def openFileDialog():
    global filename1
    filename1 =  filedialog.askopenfilename(initialdir = "C:/Users/ankitaPC/Desktop/vivek_office/Indranil_doc/Python_code",title = "choose file",filetypes = (("all files","*.xlsx"),("all files","*.*")))
    print (filename1)
    

     
title_label = Label(text='''Choose A File''',padx=70,bg="gray",font="comicsansms 11 bold")
title_label.pack(fill=X)

#frame = Frame(root,borderwidth=2,bg="gray",relief=SUNKEN)
#frame.pack(anchor="nw")

b1=Button(fg="red",text='''       Choose xyz File       ''',command=fileDialog)
b1.pack(side= LEFT,anchor="nw")


b2=Button(fg="red",text="Choose xyz File",command=fileDialog)
b2.pack(side= LEFT,anchor="nw")

b3=Button(fg="red",text="Open xyz File",command=openFileDialog)
b3.pack(side= RIGHT,anchor="sw")



root.mainloop()


