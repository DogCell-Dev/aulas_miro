#Vetor de Deslocamento entre Dois Pontos
import numpy as np

A = np.array([
    float(input("A(x): ")),
    float(input("A(y): ")),
    float(input("A(z): "))
])

B = np.array([
    float(input("B(x): ")),
    float(input("B(y): ")),
    float(input("B(z): "))
])

AB = B - A
distancia = np.linalg.norm(AB)

print("AB =", AB)
print("Distância =", distancia)
