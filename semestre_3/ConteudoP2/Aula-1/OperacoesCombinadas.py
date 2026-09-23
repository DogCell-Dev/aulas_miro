#Operações Combinadas em R3
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

k = float(input("Digite o escalar k: "))

print("u + v =", u + v)
print("u - v =", u - v)
print("k·u =", k * u)
print("||u|| =", np.linalg.norm(u))
print("||v|| =", np.linalg.norm(v))
print("u·v =", np.dot(u, v))
