import random
from turtle import Turtle, Screen, colormode
# we are importing the classes turtle and screen from the turtle module

tim = Turtle()
tim.shape('turtle')
tim.color('violet', 'pink')
tim.speed('slowest')
# This gives us the real turtle object
screen_1 = Screen()

def random_color():
    colormode(255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    tim.color(R, G, B)

def move_f():
    tim.forward(50)

def right_f():
    tim.right(90)

def left_f():
    tim.left(90)

def potty_f():
    tim.dot(20)

def change_clr():
    tim.color(random_color())

def clr():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown( )
# This gives us the real screen object
# while True:
tim.forward(10)
screen_1.listen()
screen_1.onkey(move_f, 'space')
screen_1.onkey(right_f, 'd')
screen_1.onkey(left_f, 'a')
screen_1.onkey(potty_f, 's')
screen_1.onkey(change_clr, 'c')
screen_1.onkey(clr, 'Tab')
# screen_1.onkey(move_while, 'w')
screen_1.exitonclick()

