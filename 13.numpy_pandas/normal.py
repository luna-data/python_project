import numpy as np
import matplotlib.pyplot as plt

mean=0
std=1
num_samples=1000

data=np.random.normal(mean,std,num_samples)

plt.figure(figsize=(8,6))
plt.histo(data, bins=30, density=True, alpha=0.7, color='skyblue',edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Normal Distribution Histogram')
plt.grid(True)
plt.show()