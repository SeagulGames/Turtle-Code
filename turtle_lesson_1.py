"""
ONE IMPORTANT NOTICE:
MAKE SURE TO INSTALL TURTLE BY RUNNING "pip install turtle" BEFORE RUNNING THIS PROGRAM
"""
import turtle #this line of code just imports turtle which is like installing a mod onto a game so it adds something but keeps it mostly the same
stop = True #you will see how this works later in the program
number = 0 #you will see how this works later in the program too
screen = turtle.Screen() #this makes the screen appear for the program
turtle = turtle.Turtle() #this makes the turtle appear
turtle.pendown() #when the turtle characters move it makes them have a "pen" which means when they move it draws with the pen
turtle.shape("turtle") #this makes the shape of the turtle turtle
while stop: #this makes whatever is indented with the while stop reapeat until stop = false
    if number == 2: #this uses the number variable and makes this section of the program so when number = 2 than it does whatever is in the if loop
        stop = False
        turtle.forward(100) #this makes it so the turtle finishes it's final side before the program stops
        turtle.right(90) #I couldn't figure out why the program needed this but if I didn't add this than the program would bug
    turtle.forward(100) #this makes the turtle go forward 100 pxls
    turtle.right(90) #this rotates the turtle 90 degrees to the right
    number = number + 1 #this keeps track of how many times it did the loop
input("Press enter to close out of turtle window") #this makes it so the turtle window stays up and than when you hit enter it ends the program so the window closes
