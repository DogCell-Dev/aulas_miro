def classificao(x):
    return 10 * x + 5
x = int(input("Digite o valor de X da função: "))
resultado = classificao(x)

if resultado >= 100:
    print("Desempenho Excelente")

elif resultado >= 70 and resultado < 100:
    print("Desempenho Adequado")

else:
    print("Desempenho Baixo")