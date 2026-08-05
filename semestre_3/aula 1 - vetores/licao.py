import matplotlib.pyplot as plt
import numpy as np

v = np.array([3, 9])

# Correção: adicionado o 's' em subplots
fig, ax = plt.subplots(figsize=(6, 6))

plt.quiver(0, 0, 3, 9, angles='xy', scale_units='xy', scale=1)

# Correção: limites aumentados para 10 para o vetor (3,9) caber na tela
plt.xlim(0, 10)
plt.ylim(0, 10)

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
