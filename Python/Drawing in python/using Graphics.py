#pip install graphics.py
import time
from graphics import *
def main():
    win = GraphWin("Display Window",600,600)

    a = Point(25,25)
    b = Point(100,175)
    c = Point(100,100)

    rect = Rectangle(a,b)
    circ = Circle(c,50)
    rect.setFill("red")
    circ.setFill("Blue")
    rect.setOutline("Green")
    circ.setOutline("Yellow")
    rect.setWidth(5)
    circ.setWidth(10)

    rect.draw(win)
    circ.draw(win)
    input("Please enter to quit")
    win.close()
    
main()
time.sleep(5)
