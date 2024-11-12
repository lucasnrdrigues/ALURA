# Soma entre números ímpares que são multiplos de 3:
s = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print(f'Somatória = {s}')

# Solução GPT:
s = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s += c
print(f'Somatória = {s}')

# Solução Curso em vídeo:
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c # Acumulador
        contador += 1 # Quantidade de números multiplos de 3, ele conta
print(f'A soma de todos os {contador} = {soma}')

