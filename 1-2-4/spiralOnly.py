# Imports
import turtle as trtl

# Setup Turtles
maze_painter = trtl.Turtle()
wn = trtl.Screen()

# Configuration Values
wall_length = 10
wall_increment = 10
wall_color = "black"
door_width = 15

# Configure Turtles
maze_painter.speed(0)
maze_painter.pencolor(wall_color)
'''
Psuedocode for drawing the basic spiral
x = starting distance
y = incremental distance

In a loop:
    1. go forward x
    2. turn left 90 degrees
    3. go forward x + y
    2. turn left 90 degrees
'''

def draw_spiral():
    global wall_length, wall_increment
    maze_painter.penup()
    maze_painter.goto(0,0)
    maze_painter.pendown()
    for wall in range (25):
        maze_painter.left(90)

        maze_painter.forward(wall_length + wall_increment)
        wall_increment += 10
    maze_painter.hideturtle()

# Draw door method


draw_spiral()

wn.mainloop()
