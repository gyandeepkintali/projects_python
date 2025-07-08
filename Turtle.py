import turtle as t

screen = t.Screen()
screen.title("Turtle Graphics")  
timmy_the_turtle = t.Turtle()
timmy_the_turtle.speed(5)  
for i in range(4):
    for _ in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(90)
    timmy_the_turtle.left(90)

screen.mainloop()