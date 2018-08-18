# Python program to print partial Koch Curve.
# importing the libraries : turtle standard
# graphics library for python
from turtle import *

#function to create koch snowflake or koch curve
def snowflake(lengthSide, levels):
    if levels == 0:
        print('Forward ' + str(lengthSide) + str(levels))
        forward(lengthSide)
        input()
        return
    lengthSide /= 3.0
    print('1st Snowflake function called recursively')
    snowflake(lengthSide, levels-1)
    left(60)
    print('Left 60 deg')
    print('2nd Snowflake function called recursively')
    snowflake(lengthSide, levels-1)
    right(120)
    print('Right 120')
    print('3rd Snowflake function called recursively')
    snowflake(lengthSide, levels-1)
    left(60)
    print('Left 60')
    print('4th Snowflake function called recursively')
    snowflake(lengthSide, levels-1)

# main function
if __name__ == "__main__":

    # defining the speed of the turtle
    speed(1)
    length = 300.0

    # Pull the pen up – no drawing when moving.
    penup()

    # Move the turtle backward by distance,
    # opposite to the direction the turtle
    # is headed.
    # Do not change the turtle’s heading.
    backward(length/2.0)

    # Pull the pen down – drawing when moving.
    pendown()
    for i in range(3):
        print('snowflake function ' + str(i+1))
        snowflake(length, 3)
        print('Right 120 deg')
        right(120)

    # To control the closing windows of the turtle
    mainloop()
