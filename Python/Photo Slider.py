from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("hello")
root.iconbitmap("icon.ico")


my_Image1 = ImageTk.PhotoImage(Image.open("C:/Users/ankitaPC/Desktop/1.jpg"))
my_Image2 = ImageTk.PhotoImage(Image.open("C:/Users/ankitaPC/Desktop/3.jpg"))
my_Image3 = ImageTk.PhotoImage(Image.open("C:/Users/ankitaPC/Desktop/4.jpg"))

image_list = [my_Image1,my_Image2,my_Image3]

status = Label(root,text = "Image 1 of "+ str(len(image_list)),bd = 1,relief = SUNKEN, anchor = E )

my_label = Label(image = my_Image1)
my_label.grid(row =0, column =0,columnspan = 3)
                            
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    button_forward = Button(root,text= ">>",command = lambda : forward(image_number+1))
    button_back = Button(root,text= "<<",command = lambda : back(image_number-1))
    
    if (image_number == 3):
        button_forward = Button(root,text = ">>",state = DISABLED )

    #Update Status Bar
    status = Label(root,text = "Image" + str(image_number)+" of "+ str(len(image_list)),bd = 1,relief = SUNKEN, anchor = E )
    status.grid(row = 2,column = 0,columnspan = 3, sticky = W+E)

    my_label.grid(row = 0, column = 0,columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

def back(image_number):

    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    button_forward = Button(root,text= ">>",command = lambda : forward(image_number+1))
    button_back = Button(root,text= "<<",command = lambda : back(image_number-1))

    if (image_number == 1):
        button_back = Button(root,text = "<<",state = DISABLED )
    #Update Status Bar  
    status = Label(root,text = "Image" + str(image_number)+" of "+ str(len(image_list)),bd = 1,relief = SUNKEN, anchor = E )
    status.grid(row = 2,column = 0,columnspan = 3, sticky = W+E)
        
    my_label.grid(row = 0, column = 0,columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)


button_back = Button(root,text = "<<",command = back,state = DISABLED)
button_exit = Button(root,text = "Exit Program", command = root.quit)
button_forward = Button(root,text = ">>",command = lambda : forward(2))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)

status.grid(row = 2,column = 0,columnspan = 3, sticky = W+E)



root.mainloop()
