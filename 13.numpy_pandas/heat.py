import random
import numpy as np
import matplotlib.pyplot as plt

data=np.random.rand(10,10)

plt.imshow(data, cmap='viridis',interpolation='nearest')
plt.colorbar()

plt.title('Heatmap of 2D Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
