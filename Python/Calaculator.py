from tkinter import *
root = Tk()

#columnspan cover number of Column
root.title("Simple Calculator")
e = Entry(root,width = 35,borderwidth = 5)
e.grid(row = 0,column = 0, columnspan = 3,padx = 10,pady = 10)
e.insert(0,0)

math = 0
def button_Click(number):
   current = e.get()
   e.delete(0,END)
   e.insert(0,str(current) + str(number))

def button_Clear():
    e.delete(0,END)
 
def button_equal():
    
    global math
    
    if(math != 0):
        if(e.get()!= ""):
            Second_number = int(e.get())
            e.delete(0,END)
        
            if(math == "addition" ):
               e.insert(0,(First_number + Second_number))

            if(math == "subtract" ):
                e.insert(0,(First_number - Second_number))

            if(math == "multiply" ):
                e.insert(0,(First_number * Second_number))

            try:
                if(math == "division" ):
                    e.insert(0,(First_number / Second_number))
            except:
                e.insert(0,"Error")
            math = 0            

    
    
def button_add():

    if(e.get() != ""):
        global First_number
        global math
        
        
        math = "addition"
        
        
        First_number = int(e.get())
        e.delete(0,END)
    
   
def button_subtract():
    
    if(e.get() != ""):
        global First_number
        global math
        
        math = "subtract"
        
        First_number = int(e.get())
        e.delete(0,END)
    
def button_multiply():
    
    if(e.get() != ""):    
        global First_number
        global math
        
        math = "multiply"
        
        First_number = int(e.get())
        e.delete(0,END)
    
def button_division():
    
    if(e.get() != ""):    
        global First_number
        global math
        
        math = "division"
        
        First_number = int(e.get())
        e.delete(0,END)
    


button_1 = Button(root,text = "1",padx = 40,pady = 20,command = lambda : button_Click(1))
button_2 = Button(root,text = "2",padx = 40,pady = 20,command = lambda : button_Click(2))
button_3 = Button(root,text = "3",padx = 40,pady = 20,command = lambda : button_Click(3))

button_4 = Button(root,text = "4",padx = 40,pady = 20,command = lambda : button_Click(4))
button_5 = Button(root,text = "5",padx = 40,pady = 20,command = lambda : button_Click(5))
button_6 = Button(root,text = "6",padx = 40,pady = 20,command = lambda : button_Click(6))

button_7 = Button(root,text = "7",padx = 40,pady = 20,command = lambda : button_Click(7))
button_8 = Button(root,text = "8",padx = 40,pady = 20,command = lambda : button_Click(8))
button_9 = Button(root,text = "9",padx = 40,pady = 20,command = lambda : button_Click(9))

button_0 = Button(root,text = "0",padx = 40,pady = 20,command = lambda : button_Click(0))

button_add = Button(root,text = "+",padx = 39,pady = 20,command = button_add)
button_subtrat = Button(root,text = "-",padx = 39,pady = 20,command = button_subtract)
button_multipy = Button(root,text = "*",padx = 39,pady = 20,command = button_multiply)
button_division = Button(root,text = "%",padx = 39,pady = 20,command = button_division)

button_equal = Button(root,text = "=",padx = 91,pady = 20,command = button_equal)
button_clear = Button(root,text = "Clear",padx = 79,pady = 20,command = button_Clear)

#put the button on the screen
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1,columnspan = 2)

button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1,columnspan = 2)

button_subtrat.grid(row = 6, column = 0)
button_multipy.grid(row = 6, column = 1)
button_division.grid(row = 6, column = 2)


root.mainloop()


 

