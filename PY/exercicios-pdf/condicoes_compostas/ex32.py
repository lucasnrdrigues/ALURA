from random import randint

chute = int(input('Chute um número entre 1 e 5: '))
num_sort = randint(1,5)

if chute == num_sort:
    print('Você ACERTOU!')
else:
    print('Você ERROU!')

