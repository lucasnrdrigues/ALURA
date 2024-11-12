import random

a1 = str(input('Qual o primeiro aluno?'))
a2 = str(input('Qual o segundo aluno?'))
a3 = str(input('Qual o terceiro aluno?'))

lista = [a1, a2, a3]
sorteio = random.choice(lista)

print(f'Aluno sorteado: {sorteio}')