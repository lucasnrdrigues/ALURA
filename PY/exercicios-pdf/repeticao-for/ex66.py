n = int(input('Digite um número para mostrar a tabuada: '))
lim = int(input('Até que número você quer a tabuada? '))
for i in range(1, lim + 1):
    print(f'{n} x {i} = {n * i}')