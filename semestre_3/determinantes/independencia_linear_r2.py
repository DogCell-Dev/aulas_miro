import numpy as np
v1 = np.array([float(input("v1 - x: ")),
               float(input("v1 - y: "))])
v2 = np.array([float(input("v2 - x: ")),
               float(input("v2 - y: "))])
A = np.column_stack((v1, v2))
det = np.linalg.det(A)
print("Matriz com vetores nas colunas:", A)
print(f"Determinante: {det:.4f}")
if np.isclose(det, 0):
    print("Vetores linearmente dependentes.")
else:
    print("Vetores linearmente independentes.")
