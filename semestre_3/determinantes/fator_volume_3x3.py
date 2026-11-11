import numpy as np
A = np.zeros((3, 3), dtype=float)
for i in range(3):
    for j in range(3):
        A[i, j] = float(input(f"A[{i+1},{j+1}]: "))
det = np.linalg.det(A)
print("Matriz A:", A)
print(f"Determinante: {det:.4f}")
print(f"Fator de volume: {abs(det):.4f}")
if np.isclose(det, 0):
    print("A transformação anula o volume.")
else:
    print("A transformação mantém volume não nulo.")