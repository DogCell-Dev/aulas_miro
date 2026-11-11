import numpy as np

x = float(input("Digite x: "))
y = float(input("Digite y: "))

v = np.array([x, y])

A = np.array([
    [0, -1],
    [1, 0]
])

resultado = A @ v

print("Vetor original:", v)
print("T(v) =", resultado)
print("Módulo de v =", np.linalg.norm(v))
print("Módulo de T(v) =", np.linalg.norm(resultado))