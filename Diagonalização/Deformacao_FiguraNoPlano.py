import numpy as np

A = np.zeros((2, 2), dtype=float)

for i in range(2):
    linha = list(map(float, input(f"Linha {i+1} da matriz A: ").split()))
    if len(linha) != 2:
        raise ValueError("Digite 2 valores por linha.")
    A[i] = linha

traco = np.trace(A)
det = np.linalg.det(A)
valores, vetores = np.linalg.eig(A)

print("\nMatriz A:\n", A)
print(f"Equação característica: λ² - ({traco:.4f})λ + ({det:.4f}) = 0")

for j, lam in enumerate(valores):
    print(f"Autovalor {j+1}: {lam:.6f}")
    print("Autovetor:", np.round(vetores[:, j], 6))
    print("Verificação:", np.allclose(A @ vetores[:, j], lam * vetores[:, j]))