ano_nasc = int(input('Digite o seu ano de nascimento: '))
idade = 2023 - ano_nasc
if idade >= 16:
    print('Você PODE votar!')
else:
    print('Voce NÃO PODE votar!')