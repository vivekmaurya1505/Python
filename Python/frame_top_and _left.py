from tkinter import *
root = Tk()

root.geometry("700x700")
root.title("frame with topic")

f1=Frame(root,bg="blue",borderwidth=6,relief=SUNKEN)
f1.pack(side = TOP,fill="x")

l1=Label(f1,text="hello",bg="red",padx=30)
l1.pack(padx=300)

f2=Frame(root,bg="blue",borderwidth=6,relief=SUNKEN)
f2.pack(side = LEFT,fill="y")

l2=Label(f2,text="bye",pady=20,font="Helvetica 16 bold")
l2.pack(pady=300)



root.mainloop()
