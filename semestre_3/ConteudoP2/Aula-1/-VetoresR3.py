#SUBTRAÇÃO DE VETORES
import numpy as np

u = np.array([
    float(input("u(x): ")),
    float(input("u(y): ")),
    float(input("u(z): "))
])

v = np.array([
    float(input("v(x): ")),
    float(input("v(y): ")),
    float(input("v(z): "))
])

print("u - v =", u - v)
print("v - u =", v - u)
