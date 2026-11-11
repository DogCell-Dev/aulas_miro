import numpy as np

print("Digite o vetor de movimento u:")
ux = float(input("u(x): "))
uy = float(input("u(y): "))

print("\nDigite o vetor de movimento v:")
vx = float(input("v(x): "))
vy = float(input("v(y): "))

print("\nDigite o vetor destino w:")
wx = float(input("w(x): "))
wy = float(input("w(y): "))

u = np.array([ux, uy])
v = np.array([vx, vy])
w = np.array([wx, wy])

A = np.column_stack((u, v))

det = np.linalg.det(A)
print("\nDeterminante =", det)

if not np.isclose(det, 0):
    a, b = np.linalg.solve(A, w)
    
    print("Destino atingível com solução única.")
    print("a =", a)
    print("b =", b)
    print("Verificação =", a*u + b*v)
else:
    print("Os vetores u e v são linearmente dependentes.")
    print("Não existe uma solução única para os coeficientes.")
