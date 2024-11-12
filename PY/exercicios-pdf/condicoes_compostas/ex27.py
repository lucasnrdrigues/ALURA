n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
media = (n1 + n2)/2

if media < 5:
    print('REPROVADO!')
elif media >= 5  and media < 7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')