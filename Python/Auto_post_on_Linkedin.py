import pyautogui
import datetime
import time
import keyboard 
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog




def Auto_Post():
    
    root = Tk()
    #root.title("Upload post on Linkedin")
    root.geometry("0x0")

    root.iconbitmap("Auto_Post_icon.ico")
    
    Result = None
    #print(Result)
    
    Key_Pressed = True

    pyautogui.rightClick(138, 744)

    while (Key_Pressed):

        
        
        if keyboard.is_pressed('ctrl'):
            print("Exit1")
            Key_Pressed = False
            break
       
        
        elif((Result  is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\2.png"))):
            x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\2.png")
            pyautogui.click(x,y)
            print(x,y)
            print("Enter1")
            break
        else:
            print("Not_Enter1")

        if((Result  is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\2_1.png"))):
            x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\2_1.png")
            pyautogui.click(x,y)
            print(x,y)
            print("Enter1_1")
            break
        else:
            print("Not_Enter1")
            
            
        
    while (Key_Pressed):
        
        if keyboard.is_pressed('ctrl'):  
            print("Exit2")
            Key_Pressed = False
            break
        
        elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\3.png"))):
            x,y,w,h = pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\3.png")
            pyautogui.click(x+4,y+4)
            print("Enter2")
            break
        
        elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\3_4.png"))):
            x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\3_4.png")
            pyautogui.click(x,y)
            print("Enter2_4")
            break
        
        elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\3_5.png"))):
            x,y,w,h = pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\3_5.png")
            pyautogui.click(x,y)
            print("Enter2_5")
            break
        
        elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\3_1.png"))):
            print("Enter2_1")
            break    
        elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\3_2.png"))):
            print("Enter2_2")
            break
        elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\3_3.png"))):
            print("Enter2_3")
            break


        
        else:
            print("Not_Enter2")           
        
    while (Key_Pressed):
        
        if keyboard.is_pressed('ctrl'):  
            print("Exit3")
            Key_Pressed = False
            break
        
        elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\4_1.png"))):
            x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\4_1.png")
            pyautogui.click(x+100,y);pyautogui.typewrite("https://www.linkedin.com/feed/",interval = 0.1)
            pyautogui.press("enter")
            print("Enter3")
            break   
        else:
            print("Not_Enter3")
         
       
    while (Key_Pressed):
        
        if keyboard.is_pressed('ctrl'):  
            print("Exit4")
            Key_Pressed = False
            break
        
        elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\5.png"))):
            x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\5.png")
            pyautogui.click(x,y)
            print("Enter4")
            break
        else:
            print("Not_Enter4")

    while (Key_Pressed):
        
        if keyboard.is_pressed('ctrl'):  
            print("Exit5")
            Key_Pressed = False
            break
        
        elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\6.png"))):
            x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\6.png")
            pyautogui.click(x,y);pyautogui.typewrite("""Comment your answer below \n#C #codingisfun #coders #coderlife
    #programminglife  #cdac #programming #codingchallenge #hackerrank """,interval = 0.1)
            print("Enter5")
            break
        else:
            print("Not_Enter5") 

    while (Key_Pressed):
        
        if keyboard.is_pressed('ctrl'):  
            print("Exit6")
            Key_Pressed = False
            break
        
        elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\7.png"))):
            x,y,w,h = pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\7.png")
            pyautogui.click(x,y)
            
            date = [] 
            dt = datetime.datetime.today()
            date.append(dt.day)
            date.append(dt.month)
            date.append(dt.year)
            date = str(date[0])+"-"+str(date[1])+"-"+str(date[2])
            
            
            print("Enter6")
            break
        else:
            print("Not_Enter6")
            

    if ((Key_Pressed == True) and (os.path.exists("C:\\Users\\ankitaPC\\Desktop\\Post\\"+ str(date) + ".png"))):
        
        time.sleep(2)
        #pyautogui.typewrite([r"C:\Users\ankitaPC\Desktop\Post\\","backsapce" , str(date)],interval = 0.1)
        #pyautogui.typewrite( str(date),interval = 0.1)

        
        while (Key_Pressed):
            
            if keyboard.is_pressed('ctrl'):  
                print("Exit7")
                Key_Pressed = False
                break
            
            elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\8.png"))):
                x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\8.png")
                print(x,y)
                pyautogui.click(x+100,y+3);pyautogui.typewrite( r"C:\Users\ankitaPC\Desktop\Post",interval = 0.1)
                pyautogui.typewrite("\\",interval = 0.1)
                #pyautogui.press('backspace')
                pyautogui.typewrite( str(date),interval = 0.1)

                
                print("Enter7")
                break
            
            else:
                print("Not_Enter7")


        
        while (Key_Pressed):
                
            if keyboard.is_pressed('ctrl'):  
                print("Exit8")
                Key_Pressed = False
                break
                
            elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\9.png"))):
                x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\9.png")
                pyautogui.click(x,y)
                print("Enter8")
                break
            
            elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\9_1.png"))):
                x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\9_1.png")
                pyautogui.click(x,y)
                print("Enter8_1")
                break
            else:
                print("Not_Enter8")
                
        while (Key_Pressed):
                
            if keyboard.is_pressed('ctrl'):  
                print("Exit9")
                
                Key_Pressed = False
                break
                
            elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\10.png"))):
                x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\10.png")
                pyautogui.click(x,y)
                print("Enter9")
                break
            else:
                print("Not_Enter9")

        while (Key_Pressed):
                
            if keyboard.is_pressed('ctrl'):  
                print("Exit10")
                
                Key_Pressed = False
                break
                
            elif((Result is not pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\11.png"))):
                x,y = pyautogui.locateCenterOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Auto_post\11.png")
                pyautogui.click(x,y)
                print("Enter10")
                break
            else:
                print("Not_Enter10")

    elif(Key_Pressed == False):
        
        print("Exit7777")
        messagebox.showwarning("Linkedin Post","Canceled")


    else:
        print("File Not Found")
        #time.sleep(1)
        pyautogui.hotkey('win',"d")
        messagebox.showerror("Error",str(date) + ".png" + "\nFile Not Found")
        os.system("taskkill /f /im  Auto_post_1.exe")
    root.mainloop()        


if __name__ == "__main__":
    
    if messagebox.askyesno("Auto Post", "Do you want to Post?"):
        Auto_Post()
    

