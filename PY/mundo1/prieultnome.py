n = str(input('Digite seu nome completo: '))
nome = n.split()

print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[len(nome)-1]}')