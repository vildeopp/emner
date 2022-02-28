import numpy as np


def parabola(a: float, b: float, c: float, xs: np.ndarray):
    poly = np.poly1d([a,b,c])
    arr = poly(xs)
    return arr


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    xs = np.linspace(-6, 6)

    ys = parabola(-1.5, .5, 25, xs)

    plt.plot(xs, ys, '-r')
    plt.grid(alpha=.5, linestyle='--')

    # Adds axis to the plot
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    #plt.show()

#oppgave8

arr = np.arange(1,16)
parr = (arr % 2 == 0)
print(arr[parr])

#oppgave9 
import numpy as np

arr = np.arange(1,16)
arr = np.arange(1,16)
parr = (arr % 2 == 0)
arr[parr] = 0
print(arr)

#oppgave10 
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(12)

N_steps = 1000000
expected_R = np.sqrt(N_steps)

###################################
#     generate one random walk    #
###################################
# a list of 4 directions 0,1,2,3

repeat = 5
for n in range(repeat):
    dirs = np.random.randint(0, 4, N_steps)
    # a 2D list of steps, empty for now
    steps = np.empty((N_steps,2))
    # fill the list of steps according to direction
    steps[dirs == 0] = [0,1]  # 0 - right
    steps[dirs == 1] = [0,-1] # 1 - left
    steps[dirs == 2] = [1,0]  # 2 - up
    steps[dirs == 3] = [-1,0] # 3 - down
    ###################################
    # use cumsum to sum up the individual steps to get current position
    steps = steps.cumsum(axis=0)
    ###################################
    print('Final position:',steps[-1])
    ###################################
    # draw only a selection of points, max 5000, to save memory
    skip = N_steps//5000 + 1
    xs = steps[::skip,0]
    ys = steps[::skip,1]
    plt.plot(xs,ys)
    ###################################

    ###################################
    # add a circle with expected distance
    circle = plt.Circle((0,0), radius=expected_R, color='k')
    plt.gcf().gca().add_artist(circle)
    

    # equal axis size
    plt.gcf().gca().set_aspect('equal')
    plt.xlim(-1500,1500)
    plt.ylim(-1500,1500)
###################################



plt.show()