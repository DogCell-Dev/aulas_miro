vertices = ['A', 'B', 'C', 'D']
arestas = [('A','B'),('A','C'),('B','D')]

for v in vertices:
    grau = sum(1 for v1, v2 in arestas if v1 == v)
    print(f'O grau de {v} é {grau}')

print(f'Quantidade de Vertices {len(vertices)}')
print(f'Quantidade de Arestas {len(arestas)}')

