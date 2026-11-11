#MULTIPLICAÇÃO DE VETORES
import numpy as np

u = np.array([
    float(input("u(x): ")),
    float(input("u(y): ")),
    float(input("u(z): "))
])

k = float(input("Digite o escalar k: "))

resultado = k * u

print("u =", u)
print("k =", k)
print("k·u =", resultado)
