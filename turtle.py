import turtle 
screen = turtle.Screen()
screen.title("Amyra's Square design")
screen.bgcolor("lightblue")
pen=turtle.Turtle()
pen.pensize(5)
pen.speed(3)
colors = ["red", "blue", "green", "purple"]
for i in range(4):
    pen.color(colors[i])
    pen.forward(150)
    pen.right(90)
pen.hideturtle()
screen.mainloop()

