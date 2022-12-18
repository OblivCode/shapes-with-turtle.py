from turtle import *
from math import *

def square(length: int):
    for _ in range(4):
        forward(length)
        right(90)

def rectangle(length: int, height: int):
    for n in range(4):
        n = n/2
        if n == round(n):
            forward(length)
        else:
            forward(height)       
        right(90)

def parallelogram(length: int, height: int, top_right_angle: int = None, top_left_angle:int = None):
    angles_sum = 360
    if top_right_angle == None:
        if top_left_angle == None:
            return ValueError("A top right or top left angle needs to be input.")
        top_right_angle = (angles_sum - (top_left_angle*2))/2
    elif top_left_angle == None:
        top_left_angle = (angles_sum - (top_right_angle*2))/2
    
    for n in range(4):
        n = n/2
        if n == round(n):
            forward(length)
            right(top_right_angle)
        else:
            forward(height)
            right(top_left_angle)

def polygon(length: int, sides: int):
    angle_sum = 360
    angle = angle_sum / sides

    for _ in range(sides):
        forward(length)
        right(angle)
        
color('red', 'yellow')
begin_fill()

#Make a hexagon with 100 pixel long sides
polygon(100, 6)

end_fill()
done()
