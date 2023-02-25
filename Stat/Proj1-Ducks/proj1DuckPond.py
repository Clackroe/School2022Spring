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
gui.configure(background="blue")
gui.title("Duck Pond Project")

#Setup Canvas
c = Canvas(gui, width=x_center*2, height=y_center*2, )
c.pack()

c.create_text(150, 35, text="Number of Ducks:")

entry_ducks = tk.Entry(gui)
c.create_window(150, 50, window=entry_ducks,)

c.create_text(150, 85, text="Angle:")

entry_angle = tk.Entry(gui)
c.create_window(150, 100, window=entry_angle)

c.create_text(150, 135, text="Iterations:")

entry_iterations = tk.Entry(gui)
c.create_window(150, 150, window=entry_iterations)


display_successes = tk.StringVar()
display_successes.set("Successful Iterations: 0")
successes_label = tk.Label(gui, textvariable=display_successes)
c.create_window(150, 200, window=successes_label)

display_iterations = tk.StringVar()
display_iterations.set("Iterations: 0")
iteration_label = tk.Label(gui, textvariable=display_iterations)
c.create_window(150, 225, window=iteration_label)

display_curr_prob = tk.StringVar()
display_curr_prob.set("Relative Frequency: 0")
curr_prob_label = tk.Label(gui, textvariable=display_curr_prob)
c.create_window(150, 245, window=curr_prob_label)

display_prob = tk.StringVar()
display_prob.set("Exact Probability: 0")
prob_label = tk.Label(gui, textvariable=display_prob)
c.create_window(150, 265, window=prob_label)


current_points_drawn = []




#Draw Circle Based off Geometric Circle
c.create_oval(center[0] - radius, center[1] + radius, center[0] + radius, center[1] - radius, outline="red")

#Setup Variables
points = []




def main():
    button_run = tk.Button(text="Run Simulation", background="red", command=run_app)
    c.create_window(150, 300, window=button_run)
    gui.mainloop()
    
        
        

def run_app():
    success = 0  
    
    num_ducks = int(entry_ducks.get())
    angle_degrees = float(entry_angle.get())
    
    exact_prob = num_ducks * ((angle_degrees/360) ** (num_ducks - 1))
    
      
    for p in range(num_ducks):
        points.append(rand_point)
    
    for i in range(int(entry_iterations.get())):
        generate_points()
        
        
        for p in points:
            if in_sector(points.index(p), math.radians(angle_degrees)):
                success += 1
            
        
        if(i != 0):  
         prob = success/(i)
        else:
            prob = 0
            
        prob = "{:.5f}".format(prob)
        
        display_successes.set(f"Successful Iterations: {success}")
            
        display_curr_prob.set(f"Relative Frequency: {prob}")
        display_prob.set(f"Exact Probability: {exact_prob}")
        
        
        if len(current_points_drawn) >0:
            destroy_drawn_points()
        draw_all_points()
        
        display_iterations.set(f"Iterations: {i+1}")
        
        gui.update()



def in_sector(input_point, input_angle):
    
    reference_angle = math.atan2(points[input_point][1] - y_center, points[input_point][0] - x_center)
    for input_point in points:
        dx = input_point[0] - x_center
        dy = input_point[1] - y_center
        angle = math.atan2(dy, dx)

        delta_angle = angle - reference_angle

        if delta_angle > math.pi:
            delta_angle -= 2 * math.pi
        elif delta_angle < -math.pi:
            delta_angle += 2 * math.pi

        if abs(delta_angle) > input_angle / 2:
            return False

    return True  
    


#Return Random Point Within Circle
def rand_point():
        output = [0, 0]
        while True:
            output[0], output[1] = random.uniform(x_min, x_max), random.uniform(y_min, y_max)
            if sqrt(pow(output[0]-x_center,2) + pow(output[1]-y_center,2)) <= radius:
                return [output[0], output[1]]
            
            
def generate_points():
    for i in range(int(entry_ducks.get())):
        points[i] = rand_point()


def draw_all_points():
    for i in range(len(points)):
        draw_point(points[i][0], points[i][1], "yellow")


#Draw a given point
def draw_point(x, y, col: StringVar):
    current_points_drawn.append(c.create_oval(x-5, y+5, x+5, y-5, fill=col))
    
def destroy_drawn_points():
    for p in current_points_drawn:
        c.delete(p)
    

    

if __name__ == '__main__':
    main()
    


    



    