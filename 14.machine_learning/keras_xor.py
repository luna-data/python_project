import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 1, 1, 0])

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=8, input_dim=2, activation='relu'))
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

model.complie(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5000, verbose=0)

predictions = model.predict(x_train)
print(predictions)