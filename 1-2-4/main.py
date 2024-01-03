import turtle as trtl

# maze configuration variables
num_sides = 25
path_width = 15
wall_color = "blue"

# config maze
maze_painter = trtl.Turtle()
maze_painter.pensize(5)
maze_painter.pencolor(wall_color)
maze_painter.speed("fastest")

def drawSpiral():
    # Draw Sprial
    wall_len = path_width
    for w in range(num_sides):
        wall_len += path_width

        if (w > 4):
            maze_painter.left(90)

            draw_door()

            draw_barrier()

            # a common error for the student to make is not to
            # subtract the parts of the wall that are already drawn
            # (this is not seen as a problem here,
            # but becomes apparent in the next version when
            # walls may be rendererd too long/wide)
            maze_painter.forward(wall_len - 10 - path_width - 40)

def draw_door():
    # draw door
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()

def draw_barrier():
    # draw barrier wall
    maze_painter.forward(40)
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.backward(path_width * 2)
    maze_painter.right(90)

drawSpiral()
maze_painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()