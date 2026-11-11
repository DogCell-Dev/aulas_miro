def funcao_afim(x):
    return 3 * x + 2

erro = True

while erro:
    try: 
        print("f(x) = 3x + 2 = ?")
        x = int(input("digite o valor de x: "))
        print("f(x) = 3x + 2 =", funcao_afim(x))
        erro = False
    except(ValueError):
        print("Insira um numero inteiro")


