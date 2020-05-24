from tkinter import *
root=Tk()
#GUI Title name
root.title("My_GUI")
#Width x Hight 
root.geometry("500x500")
#Width , Hight
root.minsize(100,100)
#Width , Hight
root.maxsize(700,700)
#Text Label on GUI frame
label1 = Label(text="hello")
label1.pack()
#photo Label on GUI frame
photo= PhotoImage(file="\xyz.png")
label2 = Label(image=photo)
label2.pack()


root.mainloop()
