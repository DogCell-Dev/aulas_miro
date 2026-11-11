import numpy as np

x = float(input("Digite x: "))
y = float(input("Digite y: "))
z = float(input("Digite z: "))

v = np.array([x, y, z])

A = np.array([
    [2, 0,0 ],
    [0, 0, 3],
    [0, 0, 3]
])

resultado = A @ v

print("Vetor original:", v)
print("Matriz da transformação:")
print(A)
print("2*x =", 2*x)
print("y =", y)
print("3*z =", 3*z)
print("T(v) =", resultado)
