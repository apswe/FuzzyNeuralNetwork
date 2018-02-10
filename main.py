from visual import *
from visual.graph import *
import numpy as np
from math import *

# This is the main box

scene.title = "Fuzzy Neural Network Simulation"
# Make scene background black
scene.background = color.black
scene.width = 1000
scene.height = 1000

theta = 0
platform = box(pos = vector(0, 0, 0), size = (5, 0.02, 0.2), color = color.green, opacity = 0.3)
cart = box(pos=(0,0.02*2,0), size = (0.2, 0.06, 0.06), color = color.blue)
cart.v = vector(0, 0, 0)
g = 9.81
cart.m = 0.1

running = True
delta = 0.0001
deltat = 0.02
i = 0
t = 0
deltat = 0.1 
while running:
    rate(50)
    theta += delta
    platform.rotate(angle=theta, origin = (0,0,0), axis = (0,0,1))
    cart.rotate(angle=theta, origin = (0,0,0), axis = (0,0,1))
    Fnet = norm(platform.axis)
    Fnet.mag = cart.m * g * sin(theta)
    cart.v = cart.v + (Fnet/cart.m * deltat)
    cart.pos = cart.pos + cart.v * deltat
    print("Theta = {}".format(theta))
    if theta > 0.0073/2:
        delta *= -1 
    if theta < -0.0073:
        delta *= -1
    t = t + deltat
    
