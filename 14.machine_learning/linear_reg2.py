import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

np.random.seed(0)
num_samples=50
X=np.random.rand(num_samples,1)*10
y=3*X+10+np.random.randn(num_samples,1)*2

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

mse=mean_squared_error(y_test,y_pred)
print(f"Mean Squared Error: {mse:.2f}")

plt.scatter(X_test, y_test, label="True data")
plt.plot(X_test, y_pred, color='red',label="Predictions")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Hours vs Exam Scores")
plt.legend()
plt.show()