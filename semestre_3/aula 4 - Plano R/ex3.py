import numpy as np

f1 = int(input("Digite F1: "))
f2 = int(input("Digite F2: "))

escalar = int(input("Digite o valor escalar: "))

f = np.array([f1, f2])
f = escalar * f

print (f'Produto{f}')