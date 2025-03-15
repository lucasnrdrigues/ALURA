# inicializando as variáveis
n = s = q = 0

# Enquanto for TRUE
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    q += 1 # A cada número lido, ele soma +1

print(f'A soma dos números: {s}') # Mostrando a soma dos números
print(f'A quantidade inserida de números: {q}') # Mostrando a quantidade inserida