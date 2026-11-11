import numpy as np
A = np.zeros((2, 2), dtype=float)
for i in range(2):
    for j in range(2):
        A[i, j] = float(input(f"A[{i+1},{j+1}]: "))
        
det = np.linalg.det(A)
fator = abs(det)
print("Matriz A:", A)

print(f"Determinante: {det:.4f}")
print(f"Fator de área: {fator:.4f}")

if np.isclose(fator, 0):
    print("A área é anulada.")
elif np.isclose(fator, 1):
    print("A área é preservada.")
elif fator > 1:
    print("A área é ampliada.")
else:
    print("A área é reduzida.")