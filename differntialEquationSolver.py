
# differentialEquationSolver for a second order differential equation

import numpy as np
import math
import matplotlib.pyplot as plt


def grad_x(coords):
    x = coords[0]
    y = coords[1]
    # return the first equation
    return f1
def grad_y(coords):
    x = coords[0]
    y = coords[1]
    # return the second equation
    return f2


size = 1000
lin = np.linspace(-1*size,size,10)
x,y = np.meshgrid(lin,lin)
pf_px = f1 # also first equation
pf_py = f2 # also second equation
# print(pf_px)
# print(pf_py)
d = 0.1 # step size
intial_point = [[3,4]] # initial condition

plt.ion()

for i in range(0,100):
  plt.quiver(x,y,pf_px, pf_py)
  # use for loop for trace remove it if you want no trace and
  # just make intial_point a 1x2 array and then directly update that instead 
  for point in intial_point:
    plt.plot(point[0],point[1],'ro')
  point = intial_point[len(intial_point)-1]
  new_point = []
  new_point.append(point[0] + (grad_x(point))*d)
  new_point.append(point[1] + (grad_y(point))*d)
  intial_point.append(new_point)

  if(intial_point[len(intial_point)- 1][0] > 1000
     or intial_point[len(intial_point)-1][0] < -1000
     or intial_point[len(intial_point)-1][1] > 1000
     or intial_point[len(intial_point)-1][1] < -1000):
    new_point_final = []
    new_point_final.append(point[0] + (grad_x(point))*d)
    new_point_final.append(point[1] + (grad_y(point))*d)
    plt.plot(new_point_final[0],new_point_final[1],'ro')
    intial_point.append(new_point_final)
    plt.draw()
    plt.pause(100)
  else:
    plt.draw()
    plt.pause(0.1)
    plt.clf()



# plt.quiver(x,y,pf_px, pf_py)
# plt.show()
