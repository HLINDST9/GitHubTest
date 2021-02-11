import matplotlib.pyplot as plt
import numpy as np

# setting the x - coordinates
x = np.linspace(-np.pi/2, np.pi/2, 100)
# setting the corresponding y - coordinates
y = np.sin(x)

# potting the points
plt.plot(x, y)
# function to show the plot
plt.show()
