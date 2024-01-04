import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def update(t):
    for i in range(rows):
      for j in range(cols):
          if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            if i == 0 and j == 0:
              grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i,j+1] - 2*grid[i,j])/cell_size**2
            elif i == 0 and j == cols-1:
              grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i,j-1] - 2*grid[i,j])/cell_size**2
            elif i == rows-1 and j == 0:
              grid[i,j] = grid[i,j] + k*(grid[i-1,j] + grid[i,j+1] - 2*grid[i,j])/cell_size**2
            elif i == rows-1 and j == cols-1:
              grid[i,j] = grid[i,j] + k*(grid[i-1,j] + grid[i,j-1] - 2*grid[i,j])/cell_size**2
            elif i == 0:
              grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i,j+1] + grid[i,j-1] - 3*grid[i,j])/cell_size**2
            elif i == rows-1:
              grid[i,j] = grid[i,j] + k*(grid[i-1,j] + grid[i,j+1] + grid[i,j-1] - 3*grid[i,j])/cell_size**2
            elif j == 0:
              grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i-1,j] + grid[i,j+1] - 3*grid[i,j])/cell_size**2
            elif j == cols-1:
              grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i-1,j] + grid[i,j-1] - 3*grid[i,j])/cell_size**2
          else:
            grid[i,j] = grid[i,j] + k*(grid[i+1,j] + grid[i-1,j] + grid[i,j+1] + grid[i,j-1] - 4*grid[i,j])/cell_size**2
    im.set_array(grid)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"t = {t*dt:.2f}")
    return im, ax.title, ax.xaxis.label, ax.yaxis.label

bbox = [0, 0, 100000, 100000]
cell_size = 5000
rows = int((bbox[3] - bbox[1]) / cell_size)
cols = int((bbox[2] - bbox[0]) / cell_size)

fig, ax = plt.subplots()
grid = np.zeros((rows, cols), dtype=np.int32)
cbar = fig.colorbar(ax.imshow(grid, cmap='hot', interpolation='nearest'))

for i in range(rows):
    for j in range(cols):
        grid[i, j] = math.cos(i)*100 + math.sin(j)*100

time_range = 200
dt = 1
k = 1
time_steps = np.arange(0, time_range, dt)

im = ax.imshow(grid, animated=True, cmap='hot', interpolation='nearest')
ani = animation.FuncAnimation(fig, update, frames=time_steps, interval=50, blit=True)

ani.save('heat_equation_2d.gif', writer='imagemagick')
