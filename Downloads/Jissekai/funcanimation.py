import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

def plot(data):
    plt.cla()
    plt.tick_params(labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False)
    plt.tick_params(bottom=False,
            left=False,
            right=False,
            top=False)
    x = np.random.randn(20)
    y = np.random.randn(20)
    # im = plt.plot(x)
    im = plt.scatter(x, y)

ani = animation.FuncAnimation(fig, plot, interval=50)
plt.show()

