# • Pontos: A(0,0), B(6,8), C(10,3)
#   - Calcule os vetores de deslocamento AB e BC.
#   - Determine as distâncias percorridas.
#   - Encontre o ângulo entre os vetores (mudança de direção).

# • Fórmulas:
#   - AB = B - A
#   - BC = C - B
#   - |AB| = √((x₂-x₁)² + (y₂-y₁)²)
#   - cos(θ) = (AB·BC)/(|AB| × |BC|)

import numpy as np
import matplotlib.pyplot as plt

# Definir pontos A, B e C
A = np.array([0, 0])
B = np.array([6, 8])
C = np.array([10, 3])

# Calcular vetores de deslocamento
AB = B - A
BC = C - B

# Calcular distâncias (módulos)
dist_AB = np.linalg.norm(AB)
dist_BC = np.linalg.norm(BC)

# Calcular ângulo entre os vetores
cos_theta = np.dot(AB, BC) / (dist_AB * dist_BC)
cos_theta = np.clip(cos_theta, -1.0, 1.0) # Evita erros matemáticos de precisão
angle_rad = np.arccos(cos_theta)
angle_deg = np.degrees(angle_rad)

# Criar gráfico de deslocamento
plt.figure(figsize=(8, 6))

# Trajetória (Pontos X, depois Pontos Y)
plt.plot([A[0], B[0], C[0]], [A[1], B[1], C[1]], 'bo-', label='Trajetória')

# Vetores com setas (Quiver)
plt.quiver(A[0], A[1], AB[0], AB[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vetor AB')
plt.quiver(B[0], B[1], BC[0], BC[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vetor BC')

# Anotar rótulos dos pontos
plt.text(A[0], A[1], ' A', fontsize=12, ha='right', va='bottom')
plt.text(B[0], B[1], ' B', fontsize=12, ha='left', va='bottom')
plt.text(C[0], C[1], ' C', fontsize=12, ha='left', va='top')

# Configurações visuais do gráfico
plt.title(f"Deslocamento do Drone\nDist AB: {dist_AB:.2f}, Dist BC: {dist_BC:.2f}, Ângulo: {angle_deg:.2f}°")
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
