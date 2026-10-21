import numpy as np

print("Questão 3 - Sistema linear 2x2")
print("Digite os coeficientes de cada equação, linha a linha.")

# Primeira equação: a11*x + a12*y = b1
a11 = float(input("Coeficiente de x (linha 1): "))
a12 = float(input("Coeficiente de y (linha 1): "))
b1 = float(input("Termo independente (linha 1): "))

# Segunda equação: a21*x + a22*y = b2
a21 = float(input("Coeficiente de x (linha 2): "))
a22 = float(input("Coeficiente de y (linha 2): "))
b2 = float(input("Termo independente (linha 2): "))

A = np.array([[a11, a12], [a21, a22]], dtype=float)
b = np.array([b1, b2], dtype=float)

print("\nMatriz A:\n", A)
print("Vetor b:\n", b)
print("Matriz aumentada:\n", np.column_stack((A, b)))

# Os sistemas propostos possuem solução única.
# Para outros dados, o determinante deve ser diferente de zero.
if not np.isclose(np.linalg.det(A), 0.0):
    solucao = np.linalg.solve(A, b)
    print(f"x = {solucao[0]:.6f}")
    print(f"y = {solucao[1]:.6f}")
    print("Verificação A @ solução =", A @ solucao)
else:
    print("A matriz é singular; não há solução única.")
