import numpy as np

print("Digite as notas da matriz N (3 alunos x 3 atividades):")
N = np.array([
    [float(input("Aluno 1 - Atividade 1: ")),
     float(input("Aluno 1 - Atividade 2: ")),
     float(input("Aluno 1 - Atividade 3: "))],
    
    [float(input("Aluno 2 - Atividade 1: ")),
     float(input("Aluno 2 - Atividade 2: ")),
     float(input("Aluno 2 - Atividade 3: "))],
    
    [float(input("Aluno 3 - Atividade 1: ")),
     float(input("Aluno 3 - Atividade 2: ")),
     float(input("Aluno 3 - Atividade 3: "))]
])

print("\nDigite os pesos das 3 atividades:")
P = np.array([
    [float(input("Peso da atividade 1: "))],
    [float(input("Peso da atividade 2: "))],
    [float(input("Peso da atividade 3: "))]
])

M = N @ P

print("\nMédias ponderadas -\n", M)

indice = np.argmax(M)
print("Aluno com maior média:", indice + 1)
print("Maior média:", M[indice, 0])
