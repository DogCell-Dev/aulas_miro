import numpy as np

a1 = int(input("Digite A1 = "))
a2 = int(input("Digite A2 = "))

b1 = int(input("Digite B1 = "))
b2 = int(input("Digite B1 = "))

a = np.array([a1,a2])
b = np.array([b1,b2])

ab = b - a

dist = np.linalg.norm(ab) 

if dist == 0.0:
    print(f'Distância {dist} Ortogonal')

else:
    print(f'Distancia {dist:.1f} Paralelo')

