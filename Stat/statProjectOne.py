from ast import List
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
points = [Point2D]

num_points = 3

def main():

    generate_points()
    draw_all_points()

    sp.geometry.Line(points[1], center)
        
  #  a = c.create_line(points[1][0], points[1][1], center[0], center[1, ])
    
    
    gui.mainloop()



#Return Random Point Within Circle
def rand_point():
        output = [0, 0]
        while True:
            output[0], output[1] = random.uniform(x_min, x_max), random.uniform(y_min, y_max)
            if sqrt(pow(output[0]-x_center,2) + pow(output[1]-y_center,2)) <= radius:
                return Point(output[0], output[1])
            
            
def generate_points():
    for i in range(num_points):
        points.append(rand_point())


def draw_all_points():
    for i in range(len(points)):
        draw_point(points[i].coordinates[0], points[i], "yellow")


#Draw a given point
def draw_point(x, y, col: StringVar):
    c.create_oval(x-5, y+5, x+5, y-5, fill=col)
    
    
    

if __name__ == '__main__':
    main()
    


    



    