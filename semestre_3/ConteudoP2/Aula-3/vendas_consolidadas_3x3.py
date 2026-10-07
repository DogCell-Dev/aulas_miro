import numpy as np

print("Digite os 9 valores da matriz A (3 x 3):")
A = np.array([
    [float(input("A[1,1]: ")), float(input("A[1,2]: ")),
float(input("A[1,3]: "))],
    [float(input("A[2,1]: ")), float(input("A[2,2]: ")),
float(input("A[2,3]: "))],
    [float(input("A[3,1]: ")), float(input("A[3,2]: ")),
float(input("A[3,3]: "))]
])

print("\nDigite os 9 valores da matriz B (3 x 3):")
B = np.array([
    [float(input("B[1,1]: ")), float(input("B[1,2]: ")),
float(input("B[1,3]: "))],
    [float(input("B[2,1]: ")), float(input("B[2,2]: ")),
float(input("B[2,3]: "))],
    [float(input("B[3,1]: ")), float(input("B[3,2]: ")),
float(input("B[3,3]: "))]
])

C = A + B

print("\nVendas consolidadas =\n", C)
print("Total geral:", C.sum())
print("Elemento da 2ª linha e 3ª coluna:", C[1, 2])
