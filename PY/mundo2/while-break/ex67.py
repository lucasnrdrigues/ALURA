# Exercício 67 - Faça um programa que mostre a tabuada de vários núemros, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    # Enquanto for True, ele irá lêr um número, em seguida irá verificar se negativo(menor que 0), caso não for negativo, ira usar um for com o contador i para fazer a tabuada do número de entrada
    n = int(input('Digite um número para ver a tabuada: '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')


