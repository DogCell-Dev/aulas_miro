import matplotlib.pyplot as plt

plt.quiver(0, 0, 3, 4, angles='xy', scale_units='xy', scale=1)
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
