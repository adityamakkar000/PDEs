import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as rnd

timeRange = 10000
dt = 1
timeSteps = np.arange(0, timeRange, dt)


bbox = [0, 0, 100000, 100000]
cell_size = 10000
rows = int((bbox[3] - bbox[1]) / cell_size)
cols = int((bbox[2] - bbox[0]) / cell_size)
k =  1
dx = int((bbox[2] - bbox[0]) / cell_size)

grid = np.zeros((rows, cols), dtype=np.int32)

for i in range(rows):
  for j in range(cols):
   grid[i, j] = math.cos(i)*100 + math.sin(j)*100


for t in timeSteps:
  for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
          if i == 0 and j == 0:
            grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i,j+1] - 2*grid[i,j])/dx**2
          elif i == 0 and j == cols-1:
            grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i,j-1] - 2*grid[i,j])/dx**2
          elif i == rows-1 and j == 0:
            grid[i,j] = grid[i,j] + k*(grid[i-1,j] + grid[i,j+1] - 2*grid[i,j])/dx**2
          elif i == rows-1 and j == cols-1:
            grid[i,j] = grid[i,j] + k*(grid[i-1,j] + grid[i,j-1] - 2*grid[i,j])/dx**2
          elif i == 0:
            grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i,j+1] + grid[i,j-1] - 3*grid[i,j])/dx**2
          elif i == rows-1:
            grid[i,j] = grid[i,j] + k*(grid[i-1,j] + grid[i,j+1] + grid[i,j-1] - 3*grid[i,j])/dx**2
          elif j == 0:
            grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i-1,j] + grid[i,j+1] - 3*grid[i,j])/dx**2
          elif j == cols-1:
            grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i-1,j] + grid[i,j-1] - 3*grid[i,j])/dx**2
        else:
          grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i-1,j] + grid[i,j+1] + grid[i,j-1] - 4*grid[i,j])/dx**2


  plt.imshow(grid, cmap='hot', vmin= -100, vmax=100, interpolation='nearest')
  plt.colorbar()
  plt.title(f'Time = {t*dt}')
  plt.pause(0.01)
  plt.clf()  # Clear the figure for the next plot
