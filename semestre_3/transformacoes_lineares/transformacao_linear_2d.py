import numpy as np

x = float(input("Digite x: "))
y = float(input("Digite y: "))

v = np.array([x, y])

A = np.array([
    [2, 1],
    [1, 3]
])

resultado = A @ v

novo_x = 2*x + y
novo_y = x + 3*y

print("Vetor original:", v)
print("Matriz da transformação:")
print(A)
print("1ª coordenada = 2*x + y =", novo_x)
print("2ª coordenada = x + 3*y =", novo_y)
print("T(v) =", resultado)
