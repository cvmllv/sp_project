import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import collections

# Set up the figure and axis
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-')  # 'r-' is the color and line style

# Number of seconds to display data for
display_seconds = 60

# Using deque as a fixed-size queue to store the last 'display_seconds' points
data_queue = collections.deque(maxlen=display_seconds)

def init():
    ax.set_xlim(0, display_seconds - 1)
    ax.set_ylim(-1, 1)  # Set this to the expected range of your data
    return ln,

def update(frame):
    # Simulate new data coming in
    new_data = np.sin(frame / 8)  # Replace this with your actual data source
    data_queue.append(new_data)

    # Update data for plot
    xdata = np.arange(len(data_queue)) - (len(data_queue) - 1)
    ydata = list(data_queue)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.arange(1000), init_func=init, blit=True, interval=1000)
plt.show()
