#PRODUTO ESCALAR EM R3
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

produto = np.dot(u, v)

print("u·v =", produto)

if np.isclose(produto, 0):
    print("Os vetores são ortogonais.")
else:
    print("Os vetores não são ortogonais.")
