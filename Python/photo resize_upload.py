# importing only those functions 
# which are needed 
from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
# creating tkinter window 
root = Tk()

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP)
'''  
# Adding widgets to the root window 
Label(root, text = 'GeeksforGeeks', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 
'''  
# Creating a photoimage object to use image 
photo = PhotoImage(file = "xyz.png") 
  
# Resizing image to fit on button 
photoimage = photo.subsample(10, 10) 
  
# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
#Button(top_frame, text = 'Click Me !', image = photoimage, 
 #                   compound = LEFT).pack(side = LEFT) 
  
mainloop() 
