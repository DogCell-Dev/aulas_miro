import numpy as np


A1 = int(input("Digite o valor de A1: "))
A2 = int(input("Digite o valor de A2: "))
A3 = int(input("Digite o valor de A3: "))
A4 = int(input("Digite o valor de A4: "))

B1 = int(input("Digite o valor de B1: "))
B2 = int(input("Digite o valor de B2: "))

A = np.array([
    [A1, A2,],
    [A3, A4]
])

B = np.array([
    [B1],
    [B2]
])

resultado = np.linalg.solve(A, B)

print(f"\nX = R$ {resultado[0,0]:.2f}")
print(f"Y = R$ {resultado[1,0]:.2f}")