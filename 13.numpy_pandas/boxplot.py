import random
import numpy as np
import matplotlib.pyplot as plt 

data1=np.random.normal(5,1,100)
data2=np.random.normal(10,2,100)
data3=np.random.normal(13,1.5,100)

outliers=[30,35,40]

data=[data1,data2,data3,outliers]

plt.boxplot(data)

plt.title('Box Plot of Random Data')
plt.xlabel('Data Distribution')
plt.ylabel('Value')

plt.show()