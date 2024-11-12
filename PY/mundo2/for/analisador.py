somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'----- {p} PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): ')).strip()

    # Fezendo somatório da média:
    somaidade += idade

    # Fazendo o IF para o homem mais velho:
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    # Calculando mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media = somaidade/4
print(f'Média idade = {media} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Existem {totmulher20} mulheres com menos de 20 anos.')





