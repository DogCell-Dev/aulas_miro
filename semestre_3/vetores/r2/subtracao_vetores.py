import numpy as np

u1 = int(input("Digite o U1: "))
u2 = int(input("Digite o U2: "))

v1 = int(input("Digite o V1: "))
v2 = int(input("Digite o V2: "))

u = np.array([u1, u2])
v = np.array([v1, v2])

retorno = v - u
print(f'Retorno{retorno}')