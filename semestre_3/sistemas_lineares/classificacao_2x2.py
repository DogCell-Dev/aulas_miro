import numpy as np

n = 2
A = np.zeros((n, n), dtype=float)
b = np.zeros(n, dtype=float)

print("Digite os coeficientes e os termos independentes:")
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"Coeficiente A[{i+1},{j+1}]: "))
    b[i] = float(input(f"Termo independente b[{i+1}]: "))

print("\nMatriz dos coeficientes A:\n", A)
print("Vetor dos termos independentes b:\n", b)
print("Matriz aumentada [A | b]:\n", np.column_stack((A, b)))

posto_A = np.linalg.matrix_rank(A)
posto_ampliada = np.linalg.matrix_rank(np.column_stack((A, b)))
print("Posto(A):", posto_A)
print("Posto([A|b]):", posto_ampliada)

if posto_A < posto_ampliada:
    print("SI: sistema impossível (sem solução).")
elif posto_A < n:
    print("SPI: sistema possível e indeterminado (infinitas soluções).")
else:
    solucao = np.linalg.solve(A, b)
    print("SPD: sistema possível e determinado.")
    for i, valor in enumerate(solucao):
        print(f"Incógnita {i+1} = {valor:.6f}")
    print("Verificação A @ x =", A @ solucao)
