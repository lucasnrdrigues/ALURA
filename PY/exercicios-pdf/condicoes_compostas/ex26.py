n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print(f'{n1} é MAIOR que {n2}.')
elif n2 > n1:
    print(f'{n2} é MAIOR que {n1}.')
else:
    print('Ambos são IGUAIS.')