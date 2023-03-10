#import os
import turtle
import random  
from time import sleep
star = turtle.Turtle()
colours = ["red", "blue", "grey", "purple"]  
star.width(2.5)
star.penup()
star.forward(20)

for i in range(35):
    star.color(random.choice(colours)) 
    star.forward(i * 10)
    star.right(144)
 
star.color('black')
message2 = "\t\t\t\t\t Did you like it?   Thank you :) "
star.write(message2, font=("Arial", 13, "normal"))
print(message2)
sleep(5)
star.clear()
message = "\t\t\t\t\t\t\t\t Wait..."
star.write(message, font=("Arial", 30, "italic"))
print(message)
sleep(3)
star.clear()
star.home()
star.penup()
star.forward(20)
star.pendown()
for i in range(35):
    star.color(random.choice(colours)) 
    star.forward(i * 10)
    star.right(144)


sleep(5)
star.clear()
star.color('purple')
message = "\t\t\t\t\t\t\t Thanks for watching!"
star.write(message, font=("Arial", 20, "normal"))
print(message)

turtle.done()
