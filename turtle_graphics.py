import turtle
import pyautogui

tanmay_turtle = turtle.Turtle()

def square():

    tanmay_turtle.speed(1)
    tanmay_turtle.pensize(5)
    tanmay_turtle.forward(100)
    tanmay_turtle.right(90)
    tanmay_turtle.forward(100)
    tanmay_turtle.right(90)
    tanmay_turtle.forward(100)
    tanmay_turtle.right(90)
    tanmay_turtle.forward(100)
    
def click():

    tanmay_turtle.screen.onclick(tanmay_turtle.goto)

def paint():

    color = pyautogui.prompt("COLOR")

    tanmay_turtle.pencolor(color)
    tanmay_turtle.color(color)
    tanmay_turtle.shape("circle")
    tanmay_turtle.speed(0.5)
   
    tanmay_turtle.pensize(15)
    tanmay_turtle.ondrag(tanmay_turtle.goto,1,None)
    

def abstract():
    tanmay_turtle.pensize(2)
    tanmay_turtle.speed(0)

    for i in range(500):
        tanmay_turtle.shape("circle")
        tanmay_turtle.forward(i)
        tanmay_turtle.right(91)
       
        
paint()
#click()
#abstract()
#square()









input()
