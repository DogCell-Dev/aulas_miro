# Exercício 4 – Trajeto em L
# • Pontos: A(1,1), B(1,7), C(6,7)
#   - Calcule AB e BC.
#   - Determine o ângulo entre os vetores.
#   - Interprete o movimento (curva de 90°).

import numpy as np
import matplotlib.pyplot as plt

# Definir pontos A, B e C do Exercício 3
A = np.array([1, 1])
B = np.array([1, 7])
C = np.array([6, 7])

# Calcular vetores de deslocamento
AB = B - A
BC = C - B

# Calcular distâncias (módulos)
dist_AB = np.linalg.norm(AB)
dist_BC = np.linalg.norm(BC)

# Calcular ângulo entre os vetores (com correção de precisão)
cos_theta = np.dot(AB, BC) / (dist_AB * dist_BC)
cos_theta = np.clip(cos_theta, -1.0, 1.0)
angle_rad = np.arccos(cos_theta)
angle_deg = np.degrees(angle_rad)

# Criar gráfico de deslocamento do Exercício 3
plt.figure(figsize=(8, 6))

# Trajetória
plt.plot([A[0], B[0], C[0]], [A[1], B[1], C[1]], 'bo-', label='Trajetória')

# Vetores com setas (Quiver)
plt.quiver(A[0], A[1], AB[0], AB[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vetor AB')
plt.quiver(B[0], B[1], BC[0], BC[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vetor BC')

# Anotar rótulos dos pontos
plt.text(A[0], A[1], ' A(0,0)', fontsize=12, ha='right', va='bottom')
plt.text(B[0], B[1], ' B(4,8)', fontsize=12, ha='left', va='bottom')
plt.text(C[0], C[1], ' C(1,10)', fontsize=12, ha='left', va='top')

# Configurações visuais do gráfico
plt.title(f"Exercício 3 - Mudança Acentuada de Direção\nDist AB: {dist_AB:.2f}, Dist BC: {dist_BC:.2f}, Ângulo: {angle_deg:.2f}°")
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()