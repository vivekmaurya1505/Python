from tkinter import*
import tkinter.font
root = Tk()

root.title("List menu")
myFont = tkinter.font.Font(family = "Helvetica",size = 12,weight ="bold")

menuFrame = Frame(root)
menuFrame.pack(side = LEFT)
irrFrame = Frame(root)
dogFrame = Frame(root)
calcFrame = Frame(root)


### Event Fuctions ###

def buttonPress(): #Placeholder button event

    print("button pressed")

def callback():
    print("clicked at",event.x, event.y)

def menuManage(dummy): # Manage whta options are visible
    # start by hiding all buttons
    sel = Lb.curselection()
    irrFrame.pack_forget()
    dogFrame.pack_forget()
    calcFrame.pack_forget()

    #Show the relevent buttons depending on list selection

    if sel[0] == 0:
        irrFrame.pack(side = RIGHT)

    if sel[0] == 1:
        dogFrame.pack(side = RIGHT)

    if sel[0] == 2:
        calcFrame.pack(side = RIGHT)



###WIDGETS ###
#Listbox for text-item selection

Lb = Listbox(menuFrame)
Lb.insert(1,"Irrigation Controller")
Lb.insert(2,"Dog Walker")
Lb.insert(3,"Calculator")
Lb.bind("<Double-Button-1>",menuManage)#Attach Double click Event
##Lb.bind("<Double-Button-1>,callback")#Try running this line instead of the above
Lb.pack()

#Placeholder buttons for functinality

irrOn = Button(irrFrame,text = "On",font = myFont,command = buttonPress, bg = "bisque2",height = 1).pack(side = TOP)
irrOff = Button(irrFrame,text = "Off",font = myFont,command = buttonPress, bg = "bisque2",height = 1).pack(side= BOTTOM)

dogOn = Button(dogFrame,text = "Walk",font = myFont,command = buttonPress, bg = "bisque2",height = 1).pack(side = TOP)
dogOff = Button(dogFrame,text = "No-Walk",font = myFont,command = buttonPress, bg = "bisque2",height = 1).pack(side= BOTTOM)

calcPlus = Button(calcFrame,text = "+",font = myFont,command = buttonPress, bg = "bisque2",height = 1).pack(side = TOP)
calcMinus = Button(calcFrame,text = "-",font = myFont,command = buttonPress, bg = "bisque2",height = 1).pack(side= BOTTOM)

root.mainloop()
