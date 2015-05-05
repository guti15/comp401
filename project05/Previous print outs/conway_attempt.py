import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation 
import matplotlib
import math
import pylab






rows = 5
cols = 5

def init():
    line.set_data([], [])
    return line,

def init_universe(rows, cols):
    grid = np.zeros([rows, cols])
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = round(random.random())

    return grid


def evolve(grid,pars):
    overcrowd, underpop, reproduction =  pars # 3-tuple
    rows, cols = grid.shape                   # 2-tuple
    newgrid = np.zeros([rows, cols])          # create a new grid
    neighbor = np.zeros([rows, cols])

    # Adding an Auxilary padded grid

    pboard = np.zeros([rows+2 , cols+2])
    pboard[:-2, :-2] = grid

    # make new neighbor and new grid
    #  make this into a new funtion
    
    for i in range(rows):
        for j in range(cols):
            neighbor[i][j] += sum([pboard[a][b] for a in [i-1, i, i+1] \
                                   for b in [j-1, j, j+1]])

            neighbor[i][j] -= pboard[i][j]
            #evolution logic
            newgrid[i][j] = grid [i][j]
            if grid[i][j] and \
               (neighbor[i][j] > overcrowd or neighbor [i][j] < underpop):
                newgrid[i][j] = 0

            elif not( grid[i][j] and neighbor[i][j] == reproduction):
                newgrid[i][j] = 1

        return newgrid



pars = 3, 2, 3
rows, cols = 20, 20
fig = plt.figure()
ax = plt.axes()
im = ax.matshow(init_universe(rows,cols),cmap=cm.binary)
ax.set_axis_off()



grid = init_universe(rows, cols)
fig,ax = plt.subplots()
mat = ax.matshow(grid)
newgrid = evolve(grid, pars)


# saving the file into an svg
pylab.grid(True)
fig.savefig('try.svg')


fig2,ax2 = plt.subplots()

pylab.grid(True)
fig2.savefig('attempt2.svg')

    

 
def init():
    im.set_data(init_universe(rows, cols))
 
def animate(i):
    a = im.get_array()
    a = evolve(a, pars)
    im.set_array(a)
    return [im]



# grid =init_universe(rows, cols)
# newgrid = evolve(grid, pars)

# plt.plot(init_universe(rows, cols))
# plt.show()

    
# pp = pdfPages('multipages.pdf')    



# grid  = init_universe(rows, cols)
# ax = plt.axes()
# ax.matshow(grid,cmap=cm.binary)
# ax.set_axis_off()

# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, blit=False)
# matplotlib.use('TKAgg') 
# anim.save('animation_random.mp4', fps=10) # fps = FramesPerSecond


print "done.\n"
