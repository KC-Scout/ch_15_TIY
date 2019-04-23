import matplotlib.pyplot as plt


# 15-1 Cubes
# ~ x_values = list(range(5000))
# ~ y_values = [x**3 for x in x_values]

# ~ plt.scatter(x_values, y_values)

# ~ plt.show()

# 15-2 Colored cubes
x_values = list(range(5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c = x_values, cmap = 'ocean')

plt.show()
