import numpy as np


ax = int(input("Digite ax: "))
ay = int(input("Digite ay: "))

bx = int(input("Digite bx: "))
by = int(input("Digite by: "))


A = np.array ([ax,ay])
B = np.array ([bx,by])

matriz = np.column_stack((A,B))

wx = int(input("Digite wx: "))
wy = int(input("Digite wy: "))


w = np.array ([wx,wy])


a,b = np.linalg.solve(matriz,w)

print(f'a e b {a,b}')
print(f'w {(a * A) + (b * B )}')

