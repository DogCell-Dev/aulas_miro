import numpy as np
A = np.zeros((2, 2), dtype=float)
for i in range(2):
    for j in range(2):
        A[i, j] = float(input(f"A[{i+1},{j+1}]: "))
det = np.linalg.det(A)
print("Matriz A: ", A)
print(f"Determinante: {det:.4f}")
if np.isclose(det, 0):
    print("A matriz não é inversível.")
else:
    inversa = np.linalg.inv(A)
    print("A matriz é inversível.")
    print("Matriz inversa: ", inversa)