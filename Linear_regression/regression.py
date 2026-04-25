import numpy as np
import matplotlib.pyplot as plt
# Initialized random value to two arrays
x = np.array([1,2,3,4,5])
y = np.array([3,5,7,9,11])
# y = np.array([1,2,3,4,5])
m = 0
b = 0
lr = 0.030
epochs = 1000
for epoch in range(epochs):
    y_pred = m*x + b
    error = y_pred - y 
    loss = np.mean(error**2)
    n = len(x)
    db = (2/n)*np.sum(error)
    dm = (2/n)*np.sum(error*x)
    m = m - lr*dm
    b = b - lr*db
print("Final m :", m)
print("Final b :", b)
print("loss :", loss)
plt.scatter(x,y,color='red')
plt.plot(x,x*m+b,color='blue')
plt.show()