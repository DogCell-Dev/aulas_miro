import numpy as np

print("Digite o vetor u:")
ux = float(input("u(x): "))
uy = float(input("u(y): "))

print("\nDigite o vetor v:")
vx = float(input("v(x): "))
vy = float(input("v(y): "))

print("\nDigite o vetor w:")
wx = float(input("w(x): "))
wy = float(input("w(y): "))

u = np.array([ux, uy])
v = np.array([vx, vy])
w = np.array([wx, wy])

A = np.column_stack((u, v))

posto_A = np.linalg.matrix_rank(A)
posto_Aw = np.linalg.matrix_rank(np.column_stack((A, w)))

if posto_A == posto_Aw:
    print("\nw é combinação linear de u e v.")
else:
    print("\nw NÃO é combinação linear de u e v.")
