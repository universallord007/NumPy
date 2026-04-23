import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0,5,10)
# y = np.linspace(0,90,10)

# plt.plot(x,y,'purple')
# plt.plot(x,y,'o')
# plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
plt.show()