from tkinter import *

root= Tk()

root.geometry("700x700")
root.title("MU_GUI")
#Iportant Label Operation

#text - adds the text
#bd- background
#fg - foreground
#font - sets the font
#1. font=("comicsansms", 19, "bold")
#2. font="comicsansms 19 bold"
# padx - x padding
# pady - y padding
# relief border styling - SUNKEN,RAISED,GROOVE,RIDGE


title_label = Label(text='''Connect on Teams anywhere with Windows, Mac,\n
                    iOS and Android devices, or bring remote \n
                    participants into meeting spaces of all sizes
                    with Teams.''',
                    bg="yellow",fg="blue",padx=100,pady=200,font="comicsansms 19 bold",borderwidth =20,relief= RIDGE
                    )

#Iportant pack option
#anchor = nw
#side= TOP,BOTTOM,LEFT,RIGHT
#fill
#padx
#pady

title_label.pack(side=RIGHT,fill=Y,padx=100,pady=34)
#title_label.pack()

root.mainloop()

