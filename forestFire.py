import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as rnd


def updateTemp(grid, k, dx, timeSteps):
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
  return grid

timeRange = 100
dt = 1
timeSteps = np.arange(0, timeRange, dt)


bbox = [0, 0, 100000, 100000]
cell_size = 1000
rows = int((bbox[3] - bbox[1]) / cell_size)
cols = int((bbox[2] - bbox[0]) / cell_size)

fuelGrid = np.zeros((rows, cols), dtype=np.int3)
fireGrid = np.zeros((rows, cols), dtype=np.double)
tempGrid = np.zeros((rows, cols), dtype=np.double)

for i in range(rows):
  for j in range(cols):
    fireGrid[i, j] = 25

for i in range(rows):
  for j in range(cols):
    fuelGrid[i, j] = rnd.random()

# plt.imshow(fireGrid, cmap='hot', interpolation='nearest')
# plt.show()
# plt.pause(2)
# plt.imshow(fuelGrid, cmap='hot', interpolation='nearest')
# plt.show()
# plt.pause(2)
# plt.close()

a = 1000

a = int(input())
b = int(input())


for i in range(25):
  for j in range(25):
    fuelGrid[a+i, b+j] = 100 + math.cos(i)*100 + math.sin(j)*100
    fireGrid[a+i, b+j] = 100 +  math.cos(i)*100 + math.sin(j)*100



for t in range(100):
  temp_grid = np.zeros((rows, cols), dtype=np.double)
  for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
          if i == 0 and j == 0:
            fireGrid[i,j] = fireGrid[i,j] + fuelGrid[i,j] +a*(
              fireGrid[i+1,j] + fireGrid[i,j+1] - 2*fireGrid[i,j])/cell_size**2
          elif i == 0 and j == cols-1:
           fireGrid[i,j] = fireGrid[i,j] + fuelGrid[i,j] +a*(
              fireGrid[i+1,j] + fireGrid[i,j-1] - 2*fireGrid[i,j])/cell_size**2
          elif i == rows-1 and j == 0:
            fireGrid[i,j] = fireGrid[i,j] + fuelGrid[i,j] +a*(
              fireGrid[i-1,j] + fireGrid[i,j+1] - 2*fireGrid[i,j])/cell_size**2
          elif i == rows-1 and j == cols-1:
            fireGrid[i,j] = fireGrid[i,j] + fuelGrid[i,j] +a*(
              fireGrid[i-1,j] + fireGrid[i,j-1] - 2*fireGrid[i,j])/cell_size**2
          elif i == 0:
            fireGrid[i,j] = fireGrid[i,j] + fuelGrid[i,j] +a*(
              fireGrid[i+1,j] + fireGrid[i,j+1] + fireGrid[i,j-1] - 3*fireGrid[i,j])/cell_size**2
          elif i == rows-1:
            fireGrid[i,j] = fireGrid[i,j] + fuelGrid[i,j] +a*(
              fireGrid[i-1,j] + fireGrid[i,j+1] + fireGrid[i,j-1] - 3*fireGrid[i,j])/cell_size**2
          elif j == 0:
            fireGrid[i,j] = fireGrid[i,j] + fuelGrid[i,j] +a*(
              fireGrid[i+1,j] + fireGrid[i-1,j] + fireGrid[i,j+1] - 3*fireGrid[i,j])/cell_size**2
          elif j == cols-1:
            fireGrid[i,j] = fireGrid[i,j] + fuelGrid[i,j] +a*(
              fireGrid[i+1,j] + fireGrid[i-1,j] + fireGrid[i,j-1] - 3*fireGrid[i,j])/cell_size**2
        else:
          fireGrid[i,j] = fireGrid[i,j] + fuelGrid[i,j] +a*(
            fireGrid[i+1,j] + fireGrid[i-1,j] + fireGrid[i,j+1] + fireGrid[i,j-1] - 4*fireGrid[i,j])/cell_size**2

  for i in range(rows):
    for j in range(cols):
        fuelGrid[i,j] = fuelGrid[i,j]/(a*fireGrid[i,j])

  plt.imshow(fireGrid, cmap='hot', interpolation='nearest')
  plt.colorbar()
  plt.title(f'Time = {t*dt}')
  plt.pause(0.1)  # Pause for 0.01 seconds
  plt.clf()
