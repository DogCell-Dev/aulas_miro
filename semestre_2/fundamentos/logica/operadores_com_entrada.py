a = input("O servidor está online? ").strip().lower() == 'v'
b = input("O banco de dados está respondendo? ").strip().lower() == 'v'

e = a and b
ou = a or b
negacao = not a
seEntao = (not a) or b

print(f"Resultado operador AND = {e}")
print(f"Resultado operador OR = {ou}")
print(f"Resultado operador NOT = {negacao}")
print(f"Resultado operador -> = {seEntao}")