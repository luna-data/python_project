import numpy as np
import matplotlib.pyplot as plt

height=np.random.normal(170,5,100)
weight=0.7 * height +np.random.normal(0,5,100)

plt.scatter(height,weight,label="Data",color="blue",alpha=0.6)

coefficients=np.polyfit(height, weight,1)
regression_line=np.poly1d(coefficients)
x_values=np.linspace(min(height),max(height),100)

plt.plot(x_values, regression_line(x_values),label="Regression Line",color='red')
plt.title('Scatter Plot with Regression Line')
plt.xlabel('Height (cm)')
plt.ylabel("Weight (kg)")

plt.legend()
plt.show()