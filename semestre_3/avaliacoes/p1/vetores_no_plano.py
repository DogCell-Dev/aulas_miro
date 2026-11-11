#Vetores no Plano R²

import numpy as np

ax = int(input("Digite Ax: "))
ay = int(input("Digite Ay: "))

bx = int(input("Digite bx: "))
by = int(input("Digite by: "))

a = np.array([ax, ay])
b = np.array([bx, by])

ab = b - a

dist = np.linalg.norm(ab) 

print (f'O valor dos vetores é = {ab}\n A distância percorrida pelo robô é {dist}')