import turtle
import random

turtle.speed(0)
turtle.bgcolor('black')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white']

def draw_shape(size):
    for _ in range(6):
        turtle.color(random.choice(colors))
        turtle.forward(size)
        turtle.left(60)

def draw_art():
    for _ in range(36):
        draw_shape(100)
        turtle.right(10)

draw_art()
turtle.mainloop()