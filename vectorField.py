import numpy as np
import math
import matplotlib.pyplot as plt


def grad_x(coords):
    return 2*coords[0] + coords[1]

def grad_y(coords):
    return 2*coords[1] - coords[0]


size = 100
lin = np.linspace(-1*size,size,10)
x,y = np.meshgrid(lin,lin)
pf_px = 2*x + y
pf_py = 2*y - x
print(pf_px)
print(pf_py)
dx,dy = 0.1,0.1
intial_point = [3,4]

plt.ion()

for i in range(0,1000):
  # plt.quiver(x,y,pf_px, pf_py)
  plt.plot(intial_point[0],intial_point[1],'ro')
  intial_point[0] = intial_point[0] + (grad_x(intial_point))*dx
  intial_point[1] = intial_point[1] + (grad_y(intial_point))*dy
  plt.draw()
  plt.pause(0.1)
  plt.clf()



# plt.quiver(x,y,pf_px, pf_py)
# plt.show()
