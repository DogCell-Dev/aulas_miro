#Modulo de um Vetor
import numpy as np

v = np.array([
    float(input("v(x): ")),
    float(input("v(y): ")),
    float(input("v(z): "))
])

modulo = np.linalg.norm(v)

print("v =", v)
print("||v|| =", modulo)
