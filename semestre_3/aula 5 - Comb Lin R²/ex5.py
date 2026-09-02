import numpy as np

print("Digite o vetor u:")
ux = float(input("u(x): "))
uy = float(input("u(y): "))

print("\nDigite o vetor v:")
vx = float(input("v(x): "))
vy = float(input("v(y): "))

print("\nDigite o vetor w:")
wx = float(input("w(x): "))
wy = float(input("w(y): "))

u = np.array([ux, uy])
v = np.array([vx, vy])
w = np.array([wx, wy])

A = np.column_stack((u, v))

try:
    a, b = np.linalg.solve(A, w)
    
    print("\nCoeficientes encontrados:")
    print("a =", a)
    print("b =", b)
    
    resultado = a*u + b*v
    print("Verificação =", resultado)
    
except np.linalg.LinAlgError:
    print("\nOs vetores u e v não permitem uma solução única.")
