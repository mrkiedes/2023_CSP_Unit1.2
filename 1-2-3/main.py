#   a123_apple_1.py
import turtle as trtl

# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
drawer = trtl.Turtle()

wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.addshape(pear_image)  # Make the screen aware of the new file

apple = trtl.Turtle()


# -----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
    active_apple.shape(apple_image)
    drawAnA(active_apple.xcor(), active_apple.ycor())
    wn.update()


def drop_apple():
    apple.penup()
    apple.goto(apple.xcor(), apple.ycor() - 200)
    drawer.clear()
    drawer.hideturtle()
    apple.hideturtle()


def drawAnA(x, y):
    drawer.penup()
    drawer.goto(x - 18, y - 40)
    drawer.color("white")
    drawer.write("A", font=("Arial", 55, "bold"))


# -----function calls-----
draw_apple(apple)
wn.onkeypress(drop_apple, "a")

wn.listen()
wn.bgpic("background.gif")
wn.mainloop()
