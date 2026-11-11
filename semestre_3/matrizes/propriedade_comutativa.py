import numpy as np

print("Digite os dados da matriz A (2 x 2):")
A = np.array([
    [float(input("A: ")), float(input("A: "))],
    [float(input("A: ")), float(input("A: "))]
])

print("\nDigite os dados da matriz B (2 x 2):")
B = np.array([
    [float(input("B: ")), float(input("B: "))],
    [float(input("B: ")), float(input("B: "))]
])

k = float(input("\nDigite o valor do escalar k: "))

soma = A + B
escalar = k * A

print("\nA + B =\n", soma)
print("kA =\n", escalar)

if A.shape == B.shape:
    AB = A @ B
    print("A * B =\n", AB)
else:
    AB = None
    print("A * B não pode ser calculado.")

if B.shape == A.shape:
    BA = B @ A
    print("B * A =\n", BA)
else:
    BA = None
    print("B * A não pode ser calculado.")

if AB is not None and BA is not None:
    if np.array_equal(AB, BA):
        print("Neste caso, A*B = B*A.")
    else:
        print("Neste caso, A*B != B*A.")
