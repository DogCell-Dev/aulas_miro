import numpy as np

x = float(input("Digite x: "))
y = float(input("Digite y: "))

v = np.array([x, y])

A = np.array([
    [0, -1]
])

resultado = A @ v

print("Vetor original:", v)
print("Matriz de reflexão:")
print(A)
print("T(v) =", resultado)