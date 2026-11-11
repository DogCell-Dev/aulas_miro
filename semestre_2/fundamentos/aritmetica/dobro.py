def dobro(a):
    return(2 * a)

erro = True

while erro:
    try:
        a = int(input("Digite um valor: "))
        print("O dobro desse valor é:",dobro(a))
        erro = False
    except(ValueError):
        print("Insira um numero inteiro")
