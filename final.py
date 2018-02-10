### INITIALIZE VPYTHON
# -----------------------------------------------------------------------

from __future__ import division
from visual import *
from visual.graph import *

### SETUP ELEMENTS FOR GRAPHING, SIMULATION, VISUALIZATION, TIMING
# ------------------------------------------------------------------------

# Set window title
scene.title = "Incline Plane"
scene.width = 1000
scene.height = 1000

# Make scene background black
scene.background = color.black
scene.center = (1, 1, 0)

# Define scene objects (units are in meters)
shift = 10
inclinedPlane = box(pos = vector(1, 0, 0), size = (5, 0.02, 0.2), color = color.green, opacity = 0.3)
cart = box(size = (0.2, 0.06, 0.06), color = color.blue)
sensor = box(pos=vector(3.5,0.02, 0), size=(0.2,0.02,0.02))
pointer = arrow(pos=(3.5,0,0), axis=-cart.axis, shaftwidth=0.02)
# Set up trail to mark the cart's trajectory
trail = curve(color = color.yellow, radius = 0.01) # units are in meters


### SETUP PARAMETERS AND INITIAL CONDITIONS
# ----------------------------------------------------------------------------------------

# Define parameters
cart.m = 0.5 # mass of cart in kg
cart.pos = vector(1.5, 0.04, 0.08) # initial position of the cart in(x, y, z) form, units are in meters
cart.v = vector(0, 0, 0) # initial velocity of car in (vx, vy, vz) form, units are m/s

# angle of inclined plane relative to the horizontal
theta = pi/15

# rotate the cart and the inclined plane based on the specified angle
inclinedPlane.rotate(angle = theta, origin = (0, 0, 0), axis = (0,0,1))
cart.rotate(angle = theta, origin = (0, 0, 0), axis = (0,0,1))
sensor.rotate(angle = theta, origin = (0, 0, 0), axis = (0,0,1))
g = -9.8 # acceleration due to gravity; units are m/s/s

# Define time parameters
t = 0 # starting time
deltat = 0.001  # time step units are s
period = 1
maxAngle = 20
deltaTheta = radians(maxAngle*deltat/period)
print("Delta theta = {}".format(deltaTheta))
inclinedPlane.w = (0, 0, 2 * pi / period)
### CALCULATION LOOP; perform physics updates and drawing
# ------------------------------------------------------------------------------------
distText = label(pos=(0,0.25,0), text='This is a box')
running = True
while running :  # while the cart's y-position is greater than 0 (above the ground)
    rate(1000)    
    Fnet = norm(inclinedPlane.axis)
    Fnet.mag = cart.m * g * sin(theta)
    
    theta += deltaTheta
    print("Theta = {}".format(theta))
    inclinedPlane.rotate(angle = theta, origin = (0, 0, 0), axis = (0,0,1))
    
    cart.axis = 0.1 * inclinedPlane.axis.norm()
    cart.v = cart.v + (Fnet/cart.m * deltat)
    # Position update 
    cart.pos = cart.pos + cart.v * deltat
    
    diff = cart.pos - sensor.pos
    pointer.axis = -inclinedPlane.axis.norm() * diff.mag 
    pointer.pos = sensor.pos
    # Time update
    distText.text = "{:.2f} units".format(diff.mag)
    if theta >= radians(maxAngle):
        deltaTheta *= -1
    if theta <= radians(-maxAngle):
        deltaTheta *= -1
    t = t + deltat
        
### OUTPUT
# --------------------------------------------------------------------------------------

# Print the final time and the cart's final position
print t
print cart.pos
