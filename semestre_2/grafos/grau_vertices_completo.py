vertices= ["A","B","C","D"]

arestas = [
    ("A","B"),
    ("A","C"),
    ("B","D"),
    ("C","D")
]

def grau_vertice(arestas, vertices):
    grau = 0
    for origem, destino in arestas:
        if origem == vertices or destino == vertices:
            grau += 1
    return grau

for v in vertices:
    print(f"Grau de (v): {grau_vertice(arestas,v)}")
    