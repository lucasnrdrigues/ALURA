sal_atual = float(input('Digite o seu salário atual: '))
genero = str(input('Digite o seu gênero(M/F): ').lower())
anos_trab = int(input('Digite a qnts anos você trab. na empresa: '))

if genero == 'f':
    if anos_trab < 15:
        novo_sal = sal_atual + (0.05 * sal_atual)
        print(f'Novo salário: R${novo_sal:.2f}')
    elif anos_trab >= 15 and anos_trab <= 20:
        novo_sal = sal_atual + (0.12 * sal_atual)
        print(f'Novo salário: R${novo_sal:.2f}')
    else:
        novo_sal = sal_atual + (0.23 * sal_atual)
        print(f'Novo salário: R${novo_sal:.2f}')
elif genero == 'm':
    if anos_trab < 20:
        novo_sal = sal_atual + (0.03 * sal_atual)
        print(f'Novo salário: R${novo_sal:.2f}')
    elif anos_trab >= 20 and anos_trab <= 30:
        novo_sal = sal_atual + (0.13 * sal_atual)
        print(f'Novo salário: R${novo_sal:.2f}')
    else:
        novo_sal = sal_atual + (0.25 * sal_atual)
        print(f'Novo salário: R${novo_sal:.2f}')
else:
    print('[ERRO]Entrada Inválida no Gênero!')
