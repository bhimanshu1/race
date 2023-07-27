from turtle import Turtle, Screen, colormode
import random

turt_1 = Turtle(shape='turtle')
turt_2 = Turtle(shape='turtle')
turt_3 = Turtle(shape='turtle')
turt_4 = Turtle(shape='turtle')
turt_5 = Turtle(shape='turtle')
turt_6 = Turtle(shape='turtle')

race_on = False
screen_1 = Screen()
screen_1.setup(width=1000, height=600)
user_guess = screen_1.textinput(title='Make your Bet', prompt='Guess Whose gonna Win the game? (Color)')
print(user_guess)

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'pink']
turtles = [turt_1, turt_2, turt_3, turt_4, turt_5, turt_6]
count = 0
y = -60
for turt in turtles:
    turt.color(colors[count])
    turt.penup()
    turt.goto(x=-490, y = y)
    count += 1
    y += 30

if user_guess:
    race_on = True
        
turt.speed('slow')
while race_on:
    for turt in turtles:
        if turt.xcor() >= 400:
            color_tup = turt.color()
            print(f'{color_tup[0]} is the Winner!')
            race_on = False
            if user_guess == color_tup[0]:
                print('You Wonnn!')
                break
            else:
                print("You Losttt!")
                break
        rand_num = random.randint(1, 20)
        turt.forward(rand_num)
        
screen_1.exitonclick()
            


