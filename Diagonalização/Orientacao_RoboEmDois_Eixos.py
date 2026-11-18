import numpy as np

print("Informe a matriz de transformação 2x2:")
A = np.zeros((2, 2), dtype=float)

for i in range(2):
    linha = list(map(float, input(f"Linha {i+1}: ").split()))
    if len(linha) != 2:
        raise ValueError("Digite exatamente 2 coeficientes.")
    A[i, :] = linha

valores, vetores = np.linalg.eig(A)
det = np.linalg.det(A)

print("\nA =\n", A)
print("Determinante =", round(det, 6))
print("Inversível:", not np.isclose(det, 0))

for j, lam in enumerate(valores):
    v = vetores[:, j]
    print(f"Autovalor {j+1}: {lam:.6f}")
    print("Autovetor unitário:", np.round(v, 6))
    print("A @ v = lambda * v:", np.allclose(A @ v, lam * v))