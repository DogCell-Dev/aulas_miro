import numpy as np

u = np.array ([1,4])
v = np.array ([2,-1])
w = np.array ([7,3])

A = np.column_stack((u, v))
a,b = np.linalg.solve(A, w)

print(f'a = {a:.2f}')
print(f'b = {b:.2f}')
print(f'Vetor obtido = {a*u + b*v}')

