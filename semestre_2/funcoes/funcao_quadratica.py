def funcao_quadratica(x):
    return x**2 - 4*x + 3

erro = True

while erro:
    try: 
        print("f(x) = x² + 4x + 3 = ?")
        x = int(input("digite o valor de x: "))
        print("f(x) = x² - 4x + 3 =", funcao_quadratica(x))
        erro = False
    except(ValueError):
        print("Insira um numero inteiro")


