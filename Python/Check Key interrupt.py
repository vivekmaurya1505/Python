import os
import keyboard  
Key_Pressed = True

while Key_Pressed:  
    if keyboard.is_pressed('enter'):  
        print('You Pressed A Key!')
        os.kill()
               


