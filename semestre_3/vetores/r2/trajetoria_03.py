import numpy as np
import matplotlib.pyplot as plt

# Pontos da trajetória
A = np.array([1, 1])
B = np.array([1, 7])
C = np.array([6, 7])

# Vetores de deslocamento
AB = B - A
BC = C - B

# Distâncias
dist_AB = np.linalg.norm(AB)
dist_BC = np.linalg.norm(BC)

# Produto escalar
produto_escalar = np.dot(AB, BC)

# Ângulo entre os vetores
cos_theta = produto_escalar / (dist_AB * dist_BC)
theta_rad = np.arccos(cos_theta)
theta_graus = np.degrees(theta_rad)

# Exibição dos resultados
print("Vetor AB =", AB)
print("Vetor BC =", BC)
print(f"Distância AB = {dist_AB:.2f}")
print(f"Distância BC = {dist_BC:.2f}")
print("Produto escalar =", produto_escalar)
print(f"Ângulo = {theta_graus:.2f}°")

# -----------------------------------
# Representação gráfica
# -----------------------------------
# Trajetória A -> B -> C
x = [A[0], B[0], C[0]]
y = [A[1], B[1], C[1]]

plt.plot(x, y, marker='o', label='Trajetória')

# Vetor AB
plt.quiver(
    A[0], A[1],
    AB[0], AB[1],
    angles='xy',    scale_units='xy',    scale=1,    label='Vetor AB')

# Vetor BC
plt.quiver(
    B[0], B[1],
    BC[0], BC[1],
    angles='xy',    scale_units='xy',    scale=1,    label='Vetor BC')

# Identificação dos pontos
plt.text(A[0], A[1], 'A')
plt.text(B[0], B[1], 'B')
plt.text(C[0], C[1], 'C')

plt.title(
    "Exercício 1 | Trajeto retilíneo e curva\n"
    f"Dist AB: {dist_AB:.2f} | "
    f"Dist BC: {dist_BC:.2f} | "
    f"Ângulo: {theta_graus:.1f}°"
)

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True)
plt.legend()
plt.axis('equal')

plt.show()
