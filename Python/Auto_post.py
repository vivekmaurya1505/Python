import pyautogui
import datetime
import time
#pyautogui.click(140,746)
pyautogui.rightClick(138, 744)
pyautogui.click(72,654)
time.sleep(2)
x,y,w,h = pyautogui.locateOnScreen(r"C:\Users\ankitaPC\Desktop\Post\Plus_red.png")
print(x,y,w,h)
pyautogui.click(x+4,y+5)
time.sleep(2)
pyautogui.click(242,50);pyautogui.typewrite("https://www.linkedin.com/feed/",interval = 0.1)

pyautogui.press("enter")
time.sleep(2)
pyautogui.click(619,120)
time.sleep(2)
pyautogui.click(619,240)
time.sleep(2)
pyautogui.click(431,293);pyautogui.typewrite("""Comment your answer below 👇 
#C #codingisfun #coders #coderlife #programminglife
#cdac #programming #codingchallenge #hackerrank""",interval = 0.1)
time.sleep(2)
pyautogui.click(497,466)
time.sleep(2)
pyautogui.click(199,426)
time.sleep(2)
date = []
dt = datetime.datetime.today()
date.append(dt.day)
date.append(dt.month)
date.append(dt.year)
date = str(date[0])+"-"+str(date[1])+"-"+str(date[2])
pyautogui.click(199,426);pyautogui.typewrite('18-5-2020',interval = 0.1)
pyautogui.click(512,461)

