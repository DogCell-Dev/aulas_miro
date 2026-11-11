#SOMA DE VETORES
import numpy as np

ux = float(input("u(x): "))
uy = float(input("u(y): "))
uz = float(input("u(z): "))

vx = float(input("v(x): "))
vy = float(input("v(y): "))
vz = float(input("v(z): "))

u = np.array([ux, uy, uz])
v = np.array([vx, vy, vz])

resultado = u + v

print("u =", u)
print("v =", v)
print("u + v =", resultado)
