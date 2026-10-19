#hello_robot.py - my first Robonav python project

from matplotlib.pylab import f


robot_name = "Robonav" 
x = 0.0              # position [m]
speed = 0.5          # [m/s]
dt =1.0              # time step [s]
print(f"Hello from {robot_name}!")
print (7/2)         #remember
print(7//2)         #integer division

for step in range(5):  #for (int step =0; step <5; step++)
    x = x + speed *dt
    print(f"step {step}: x = {x} m")
       