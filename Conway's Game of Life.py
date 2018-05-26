# Python code to implement Conway's Game Of Life
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# setting up the values for the grid
ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):

    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.5, 0.5]).reshape(N, N)


def addGlider(i, j, grid):

    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    255, 0],
                       [0,  0, 255],
                       [255,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def addBeeHive(i, j, grid):
    beeHive = np.array([[0,255,255,0],
                    [255,0,0,255],
                    [0,255,255,0]])
    grid[i:i+3, j:j+4] = beeHive

def addBlock(i, j, grid):
    block=np.array([[255,255],[255,255]])
    grid[i:i+2,j:j+2]=block

def addLoaf(i, j, grid):
    loaf=np.array([[0,255,255,0],
                  [255,0,0,255],
                  [0,255,0,255],
                  [0,0,255,0]])
    grid[i:i+4,j:j+4]=loaf

def addBoat(i, j, grid):
    boat=np.array([[255,255,0],
                   [255,0,255],
                   [0,255,0]])
    grid[i:i+3,j:j+3]=boat

def addTub(i, j, grid):
    tub=np.array([[0,255,0],
                   [255,0,255],
                   [0,255,0]])
    grid[i:i+3,j:j+3]=tub

def addBlinker(i, j, grid):
    blinker=np.array([255,255,255])
    grid[i:i+1,j:j+3]=blinker

def addToad(i, j, grid):
    toad=np.array([[0,255,255,255],
                   [255,255,255,0]])
    grid[i:i+2,j:j+4]=toad

def addBeacon(i, j, grid):
    beacon=np.array([[255,255,0,0],
                     [255,255,0,0],
                     [0,0,255,255],
                     [0,0,255,255]])
    grid[i:i+4,j:j+4]=beacon

def addPulsar(i, j, grid):
    pulsar=np.array([[0,0,0,0,255,0,0,0,0,0,255,0,0,0,0],
                    [0,0,0,0,255,0,0,0,0,0,255,0,0,0,0],
                    [0,0,0,0,255,255,0,0,0,255,255,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [255,255,255,0,0,255,255,0,255,255,0,0,255,255,255],
                    [0,0,255,0,255,0,255,0,255,0,255,0,255,0,0],
                    [0,0,0,0,255,255,0,0,0,255,255,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,255,255,0,0,0,255,255,0,0,0,0],
                    [0,0,255,0,255,0,255,0,255,0,255,0,255,0,0],
                    [255,255,255,0,0,255,255,0,255,255,0,0,255,255,255],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,255,255,0,0,0,255,255,0,0,0,0],
                    [0,0,0,0,255,0,0,0,0,0,255,0,0,0,0],
                    [0,0,0,0,255,0,0,0,0,0,255,0,0,0,0]])
    grid[i:i+15,j:j+15]=pulsar

def addPentadecathlon(i, j, grid):
    pentadecathlon=np.array([[255,255,255],
                             [0,255,0],
                             [0,255,0],
                             [255,255,255],
                             [0,0,0],
                             [255,255,255],
                             [255,255,255],
                             [0,0,0],
                             [255,255,255],
                             [0,255,0],
                             [0,255,0],
                             [255,255,255]
                             ])
    grid[i:i+12,j:j+3]=pentadecathlon

def addSpaceship(i, j, grid):
    spaceship=np.array([[255,0,0,255,0],
                   [0,0,0,0,255],
                   [255,0,0,0,255],
                   [0,255,255,255,255]])
    grid[i:i+4,j:j+5]=spaceship


def update(frameNum, img, grid, N):

    # copy grid since we require 8 neighbors
    # for calculation and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):

            # compute 8-neghbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulaton takes place on a toroidal surface.
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

            # apply Conway's rules
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# main() function
def main():

    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")

    # add arguments
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--beeHive', action='store_true', required=False)
    parser.add_argument('--block', action='store_true', required=False)
    parser.add_argument('--loaf', action='store_true', required=False)
    parser.add_argument('--boat', action='store_true', required=False)
    parser.add_argument('--tub', action='store_true', required=False)
    parser.add_argument('--blinker', action='store_true', required=False)
    parser.add_argument('--toad', action='store_true', required=False)
    parser.add_argument('--beacon', action='store_true', required=False)
    parser.add_argument('--pulsar', action='store_true', required=False)
    parser.add_argument('--pentadecathlon', action='store_true', required=False)
    parser.add_argument('--spaceship', action='store_true', required=False)

    args = parser.parse_args()

    # set grid size
    N = 50
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    # declare grid
    grid = np.array([])

    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)

    elif args.beeHive:
        grid = np.zeros(N*N).reshape(N, N)
        addBeeHive(1, 1, grid)

    elif args.block:
        grid = np.zeros(N*N).reshape(N, N)
        addBlock(1, 1, grid)

    elif args.loaf:
        grid = np.zeros(N*N).reshape(N, N)
        addLoaf(1, 1, grid)

    elif args.boat:
        grid = np.zeros(N*N).reshape(N, N)
        addBoat(1, 1, grid)

    elif args.tub:
        grid = np.zeros(N*N).reshape(N, N)
        addTub(1, 1, grid)

    elif args.blinker:
        grid = np.zeros(N*N).reshape(N, N)
        addBlinker(1, 1, grid)

    elif args.toad:
        grid = np.zeros(N*N).reshape(N, N)
        addToad(1, 1, grid)

    elif args.beacon:
        grid = np.zeros(N*N).reshape(N, N)
        addBeacon(1, 1, grid)

    elif args.pulsar:
        grid = np.zeros(N*N).reshape(N, N)
        addPulsar(1, 1, grid)

    elif args.pentadecathlon:
        grid = np.zeros(N*N).reshape(N, N)
        addPentadecathlon(10, 10, grid)

    elif args.spaceship:
        grid = np.zeros(N*N).reshape(N, N)
        addSpaceship(1, 1, grid)

    else:   # populate grid with random on/off -
            # more off than on
#        grid = randomGrid(N)
        grid=np.zeros((N,N))

        addSpaceship(1, 0, grid)
        addPentadecathlon(10, 5, grid)
        addPulsar(10, 13, grid)
        addBeacon(10,30, grid)
        addToad(10, 40, grid)
        addBlinker(20, 30, grid)
        addTub(15,35, grid)
        addBoat(20,35, grid)
        addLoaf(15, 40, grid)
        addBlock(20, 45, grid)
        addBeeHive(25, 30, grid)
        addGlider(30, 10, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 60,
                                  interval=updateInterval,
                                  save_count=50)
    plt.show()

# call main
if __name__ == '__main__':
    main()
