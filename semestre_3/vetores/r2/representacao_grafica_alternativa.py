from matplotlib import pyplot as plt

plt.quiver(0, 0, 3, 2, angles='xy', scale_units='xy', scale=1)
plt.xlim(0, 4)
plt.ylim(0, 4) # Define o limite do eixo Y de 0 a 4
plt.grid(True) # Opcional: adiciona a grade para facilitar a visualização
plt.show()     # Essencial para abrir a janela do gráfico
