import numpy as np
vetores = []
for i in range(3):
    print(f"Digite as coordenadas do vetor {i+1}: ")
    v = []
    for eixo in ("x", "y", "z"):
        v.append(float(input(f"{eixo}: ")))
    vetores.append(v)
A = np.column_stack(vetores)
det = np.linalg.det(A)
print("Matriz com vetores nas colunas:", A)
print(f"Determinante: {det:.4f}")
if np.isclose(det, 0):
    print("Vetores linearmente dependentes.")
else:
    print("Vetores linearmente independentes.")