def celsius_para_fahrenheit(c):
    return (9/5)*c + 32

erro = True

while erro:
    try: 
        c = int(input("Qual é a temperatura atual do seu ambiente: "))
        print("convertendo temperatura de",c,"C para",celsius_para_fahrenheit(c),"fahrenheit")
        erro = False
    except(ValueError):
        print("Insira um numero inteiro")
