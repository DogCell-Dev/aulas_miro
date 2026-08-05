def bonus(x):
    return 200 + 50*x

erro = True

while erro:
    try: 
        print("f(x) = 200 + 50x = ?")
        x = int(input("digite o valor de x: "))
        print("f(x) = 200 + 50x =", bonus(x))
        erro = False
    except(ValueError):
        print("Insira um numero inteiro")

