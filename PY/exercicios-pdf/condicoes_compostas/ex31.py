print('1 - PEDRA')
print('2 - PAPEL')
print('3 - TESOURA')
j1 = int(input('Qual sua jogada j1? '))
j2 = int(input('Qual a sua jogada j2? '))


if (j1 == 1 and j2 == 3) or (j1 == 2 and j2 == 1) or (j1 == 3 and j2 == 2):
    print('Jogador 1 WINS')
elif (j1 == 1 and j2 == 2) or (j1 == 2 and j2 == 3) or (j1 == 3 and j2 == 1):
    print('Jogador 2 WINS')
else:
    print('EMPATE')

