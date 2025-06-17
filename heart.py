import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")  # You can change background color if you want

# Create turtle pen
pen = turtle.Turtle()
pen.color("red")
pen.begin_fill()

# Draw the heart shape
pen.left(120)
pen.forward(100)
pen.circle(-50,120)
pen.left(120)
pen.circle(-50, 120)
pen.forward(100)

pen.end_fill()
pen.hideturtle()

# Keep the window open
screen.mainloop()
           # Keep the window open


