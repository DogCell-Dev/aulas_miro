import numpy as np

x = float(input("Digite x: "))
y = float(input("Digite y: "))
k = float(input("Digite o fator de escala: "))

v = np.array([x, y])

A = np.array([
    [k, 0],
    [0, k]
])

resultado = A @ v

print("Vetor original:", v)
print("Matriz de escala:")
print(A)
print("T(v) =", resultado)
