import numpy as np

a11 = int(input("Digite o valor de a11: "))
a12 = int(input("Digite o valor de a12: "))
a21 = int(input("Digite o valor de a21: "))
a22 = int(input("Digite o valor de a22: "))

b11 = int(input("Digite o valor de b11: "))
b12 = int(input("Digite o valor de b12: "))
b21 = int(input("Digite o valor de b21: "))
b22 = int(input("Digite o valor de b22: "))

A = np.array([
    [a11, a12,],
    [a21, a22]
])

B = np.array([
    [b11, b12],
    [b21, b22]
])

C = A + B

print(f"\n Estoque final: \n{C}")

K = int(input("Para continuar, por favor, digite o valor de K: "))
resultado = K * C

print(f"\n Nova meta de estoque: \n{resultado}")