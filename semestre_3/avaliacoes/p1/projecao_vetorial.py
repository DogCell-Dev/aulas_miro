import numpy as np

print("--- Questão 5: Projeção Vetorial ---")

# Capturando os vetores pelo teclado usando input()
ux = float(input("Digite a componente x do vetor u: "))
uy = float(input("Digite a componente y do vetor u: "))
vx = float(input("Digite a componente x do vetor v: "))
vy = float(input("Digite a componente y do vetor v: "))

# Criando os arrays do NumPy
u = np.array([ux, uy])
v = np.array([vx, vy])

# a) Calcule o produto escalar u . v
produto_escalar = np.dot(u, v)

# b) Calcule ||v||² e o coeficiente k = (u . v) / ||v||²
# A norma ao quadrado de v é simplesmente o produto escalar de v por ele mesmo (v . v)
norma_v_quadrado = np.dot(v, v)
k = produto_escalar / norma_v_quadrado

# c) Calcule e apresente o vetor proj_v(u)
proj_v_u = k * v

# Exibição dos resultados na tela
print(f"a) Produto escalar (u . v) = {produto_escalar:.2f}")
print(f"b) Norma de v ao quadrado (||v||²) = {norma_v_quadrado:.2f}")
print(f"   Coeficiente k = {k:.2f}")
print(f"c) Vetor Projeção proj_v(u) = {proj_v_u}")
