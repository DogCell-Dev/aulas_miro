import numpy as np

print("Digite os dados da matriz A (2 x 2):")
A = np.array([
    [float(input("A: ")), float(input("A: "))],
    [float(input("A: ")), float(input("A: "))]
])

print("\nDigite os dados do vetor coluna B (2 x 1):")
B = np.array([
    [float(input("B: "))],
    [float(input("B: "))]
])

print("\nDimensão de A:", A.shape)
print("Dimensão de B:", B.shape)

if A.shape[1] == B.shape[0]:
    C = A @ B
    print("A * B =\n", C)
else:
    print("As dimensões são incompatíveis para multiplicação.")
