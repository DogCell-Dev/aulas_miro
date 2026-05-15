vertices = ["A","B","C","D","E"]

arestas = [
    ("A","B"),
    ("A","C"),
    ("B","D"),
    ("C","D"),
    ("E","D")
]

matriz = []

for i in vertices: 
    linha = []
    for j in vertices:
        if (i, j) in arestas or (j, i) in arestas:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
print("matriz de adjacência: ")
print(" ", vertices)

for i in range(len(vertices)):
    print(vertices[i], matriz[i])

