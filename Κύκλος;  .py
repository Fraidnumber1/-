#Athanasios Lappas, 7/9/22 : 12:00
#Change "acuracy" as you may, (make integers floats if you may (by not printing turtle... python's dissadvantages, or use matplotlib... !)) and run it!
import math
import turtle
to_circle = turtle.Turtle()
screen = turtle.Screen()
#--------------------"acuracy----------------------
accuracy = 9
#--------------------"acuracy----------------------
starting_step=1
previous_step = 0
next_step = 1
to_circle.speed(10)
i=0
for i in range(previous_step,accuracy):
    for next_step in range(previous_step,accuracy):   
        next_step += 1
        to_circle.forward(next_step-previous_step)
        to_circle.left((next_step-previous_step))
        print(starting_step/accuracy)
        print((starting_step/accuracy+1)/((starting_step)/accuracy))
print(math.pi)
