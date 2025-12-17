import tensorflow as tf
import numpy as np

model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=2,input_dim=2,activation="sigmoid"))
model.add(tf.keras.layers.Dense(units=1,activation="sigmoid"))

model.compile(loss='mean_squared_error',optimizer='sgd',metrics=['accuracy'])

X=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([[0],[1],[1],[1]])
model.fit(X,y,batch_size=1,epochs=5000,verbose=0)

print(model.predict(X))

