import numpy as np

ux = int(input("Digite o valor de ux: "))
uy = int(input("Digite o valor de uy: "))

vx = int(input("Digite o valor de vx: "))
vy = int(input("Digite o valor de vy: "))

u = np.array ([ux,uy])
v = np.array ([vx,vy])

prodEscalar = np.dot(u,v)

if prodEscalar == 0:
    print(f'90° Ortogonal')

else:
    print(f'Não Ortogonal')