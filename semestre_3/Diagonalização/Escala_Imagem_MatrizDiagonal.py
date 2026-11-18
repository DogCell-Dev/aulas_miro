# Os presentes exercícios são baseados na diagonalização
import numpy as np

print("Digite os coeficientes da matriz 2x2:")
linhas = []
for i in range(2):
    linha = list(map(float, input(f"Linha {i+1} (2 valores): ").split()))
    if len(linha) != 2:
        raise ValueError("Cada linha deve conter 2 valores.")
    linhas.append(linha)

A = np.array(linhas, dtype=float)
valores, vetores = np.linalg.eig(A)
print("\nMatriz A:\n", A)

for j in range(2):
    lam = valores[j]
    v = vetores[:, j]
    print(f"\nAutovalor {j+1}: {lam:.6f}")
    print("Autovetor:", np.round(v, 6))
    print("A @ v =", np.round(A @ v, 6))
    print("lambda * v =", np.round(lam * v, 6))
    print("Verificado:", np.allclose(A @ v, lam * v))