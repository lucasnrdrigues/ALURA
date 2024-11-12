nome = input('Digite seu nome completo: ')

print(f' Nome maiúsculo: {nome.upper()}')

print(f'Nome minúsculo: {nome.lower()}')


div = nome.split()
nome_jun = ''.join(div)
print(f'Qntd. letras do nome completo sem espaços: {len(nome_jun)}')

# Também poderia fazer somente:
print(f'Qntd. letras do nome completo sem espaços: {len(nome)-nome.count(" ")}')

print(f'Qntd. de letras do primeiro nome: {len(div[0])}')

print(f'Qntd. de letras do nome com espaços: {len(nome)}')