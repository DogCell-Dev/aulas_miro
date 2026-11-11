import numpy as np

ux = int(input("Digite o valor de ux: "))
uy = int(input("Digite o valor de uy: "))

vx = int(input("Digite o valor de vx: "))
vy = int(input("Digite o valor de vy: "))

u = np.array ([ux,uy])
v = np.array ([vx,vy])

print(f'u * v = {u * v}')