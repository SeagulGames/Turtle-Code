import turtle #this just imports turtle like the last lesson
screen = turtle.Screen() #this makes the screen like it did last lesson
screen.bgcolor("lightblue") #this makes the screen lightblue but if you are doing this by yourself you have to add the bg to bgcolor or it will not work
turtle = turtle.Turtle() #this adds the turtle
turtle.shape("turtle") #this makes the shape of the turtle a turtle
turtle.penup() #this makes sure the turtle character doesn't make a mess on the screen
turtle.backward(500) #this makes the turtle go backwards so you can see something funny at the end of the program
print("HIT CTRL+C TO STOP THE PROGRAM") #this just tells you that you can hit CTRL+C to stop the program if you aren't looking at this code
try: #I will later say in the program what this does
    while True: #this means that whatever comes after this will reapeat forever but remember you can hit CTRL+C to stop the program that is why there is a try and except so the program exits gracefully
        turtle.forward(10) #moves the turtle forward 10 pixls
        turtle.stamp() #This is a new function and what it does is the turtle stamps itself to the screen but the stamp can't move but the original turtle can move
except KeyboardInterrupt: #this makes it so when you hit CTRL+C it will gracefully stop the program
    pass #this just means that I have nothing to put here so it is a placeholder so if I do want to put something there I can
#so there you have it a program where it makes a catipillar of turtles
#18965
