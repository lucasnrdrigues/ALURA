ano = int(input('Digite o seu ano de nascimento: '))
idade = 2023 - ano

if idade < 18:
    print(f'Faltam {18 - idade} ano(s) para você se alistar!')
elif idade == 18:
    print('Você deve se alistar!')
else:
    print(f'Passou-se {idade - 18} anos desde o alistamento')