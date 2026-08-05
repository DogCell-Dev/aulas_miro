usuarios = ["Ana", "Bruno", "Carlos", "Daniela"]

grafo = {usuario: [] for usuario in usuarios}

relacionamentos = [
    ("Ana", "Bruno"),
    ("Ana", "Carlos"),
    ("Bruno", "Daniela")
]

for u1, u2 in relacionamentos:
    grafo[u1].append(u2)
    grafo[u2].append(u1)

graus = {}
print("--- Grau de cada usuário ---")
for usuario, conexoes in grafo.items():
    grau = len(conexoes)
    graus[usuario] = grau
    print(f"Grau de {usuario}: {grau}")

print("\n--- Resultado ---")
maior_grau = max(graus.values())
usuarios_mais_conectados = [user for user, grau in graus.items() if grau == maior_grau]

if len(usuarios_mais_conectados) == 1:
    print(f"O usuário com maior número de conexões é: {usuarios_mais_conectados[0]} ({maior_grau} conexões)")
else:
    lista_nomes = ", ".join(usuarios_mais_conectados)
    print(f"Os usuários empatados com maior número de conexões são: {lista_nomes} ({maior_grau} conexões cada)")

