from ast import List
import math

import random

import tkinter as tk
from tkinter import *

import numpy as np

import sympy as sp
from sympy import *
from sympy.geometry import *
  
  
#Setup Circle
x_center = 500
y_center = 250
center = Point(x_center, y_center)
radius = 200
circ = sp.geometry.Circle(center, radius)

#Min Max
x_min = x_center - radius
x_max = x_center + radius

y_min = y_center - radius
y_max = y_center + radius


#Setup gui
gui = Tk()
gui.configure(background="green")
gui.title("Duck Pond Project")

#Setup Canvas
c = Canvas(gui, width=1000, height=1000, )
c.pack()


#Draw Circle Based off Geometric Circle
c.create_oval(center[0] - radius, center[1] + radius, center[0] + radius, center[1] - radius, outline="red")

#Setup Variables
points = []

num_points = 3

exact_prob = 0.75

sector = 180

LD = Line(center, slope=0)

def main():
    
    success = 0    
    
    for i in range(10000):
        generate_points()
        # draw_all_points()
        # gui.mainloop()
        
        if in_sector():
            success +=1
        if(i != 0):  
         prob = success/(i)
        else:
            prob = 0
        
        print(f"Current Prob: {prob}, Exact Prob: {exact_prob}")
        
    print(len(points))
        
        




def in_sector():
    

    # Find the center of the circle
    cx, cy = (x_center, y_center)
    for p in points:
        cx += p[0]
        cy += p[1]
    cx /= num_points
    cy /= num_points

    # Calculate the angle between each duck's position and the center of the circle
    angles = []
    for p in points:
        dx = p[0] - cx
        dy = p[1] - cy
        angle = math.atan2(dy, dx)
        angles.append(angle)

    # Sort the angles in ascending order
    angles.sort()

    # Check if all the ducks are on one side of the circle
    temp1 = True
    temp2 = True
    for p in range(num_points):
        for i in range(num_points - 1):
            if abs(angles[i + 1] - angles[i]) >= math.pi:
                temp1 = False
        for i in range(num_points - 1):
            if abs(angles[i + 1] - angles[i]) <=  -math.pi:
                temp2 = False
    if (not(temp1) or not(temp2)):
        return True
    else:
        return False
                
                
                
                
    

def calculate_sector(p1, p2, sector):
    l1 =  sp.Line(p1, center)
    l2 = sp.Line(p2, center)
    
    angle_to_beat = l1.angle_between(LD)
    angle_to_beat = deg(angle_to_beat)
    angle_to_beat = angle_to_beat.evalf(4)
    angle_to_beat = angle_to_beat + sector
    angle_to_beat = angle_to_beat % 360
    
    angle = l2.angle_between(LD)
    angle = deg(angle)
    angle = angle.evalf(4)
    angle = angle % 360
    
    if (angle <= angle_to_beat and sector > 0):
        return True
    elif (angle >= angle_to_beat and sector < 0):
        return True
    else:
        return False
    
    


#Return Random Point Within Circle
def rand_point():
        output = [0, 0]
        while True:
            output[0], output[1] = random.uniform(x_min, x_max), random.uniform(y_min, y_max)
            if sqrt(pow(output[0]-x_center,2) + pow(output[1]-y_center,2)) <= radius:
                return [output[0], output[1]]
            
            
def generate_points():
    points.clear()
    for i in range(num_points):
        points.append(rand_point())


def draw_all_points():
    for i in range(len(points)):
        draw_point(points[i][0], points[i][1], "yellow")


#Draw a given point
def draw_point(x, y, col: StringVar):
    c.create_oval(x-5, y+5, x+5, y-5, fill=col)
    
    
    

if __name__ == '__main__':
    main()
    


    



    