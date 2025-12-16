import random
import numpy as np
import matplotlib.pyplot as plt

data=np.random.randint(0,100,1000)
plt.hist(data,bins=20,color='skyblue',edgecolor='black')

plt.title("Histogram od Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()