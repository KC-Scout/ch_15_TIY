import matplotlib.pyplot as plt
import matplotlib.axes as ax
from random_walk_15_5 import RandomWalk

# Make a random walk, and plot the points

while True: 
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Set the size of the plotting window
    plt.figure(dpi = 128, figsize = (10, 6))
    
    point_numbers = list(range(rw.num_points))    
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, 
        cmap = plt.cm.Blues, edgecolor = 'none', s = 1)
    plt.scatter(rw.x_values[0], rw.y_values[0], s = 100, c = 'red')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], s = 100,c = 'orange')
    
    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    
    keep_running = input("Do you want to generate another plot?")
    if keep_running.lower() == 'n':
        break
