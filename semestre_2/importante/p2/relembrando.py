def valorX (x):
    return 3 * x + 1

while True:
    try:
        x = int(input('Digite o valor inteiro de X: '))
        resultado = valorX (x)
        print(f'O valor de x é {x} e o resultado é {resultado}')
        break
    except ValueError:
        print('Digite um número inteiro!')