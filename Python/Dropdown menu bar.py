from tkinter import*
root = Tk()
root.title("Menu Bar")
def abc():
    pass
Menubar = Menu(root)


filename =  Menu(Menubar,tearoff = 0)
filename.add_command(label = "Open",command = abc)
filename.add_command(label = "close",command = abc)
filename.add_separator()
filename.add_command(label = "Quit",command = root.quit)
Menubar.add_cascade(label = "File",menu = filename)

filename =  Menu(Menubar,tearoff = 0)
filename.add_command(label = "Open",command = abc)
filename.add_command(label = "close",command = abc)
filename.add_separator()
filename.add_command(label = "Quit",command = root.quit)
Menubar.add_cascade(label = "Help",menu = filename)

root.config(menu = Menubar)
root.mainloop()

