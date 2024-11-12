ano = int(input("Digite o valor de um ano: "))
ano_str = str(ano)

# Essa ano_str[] só funciona se for com string!
if (ano % 4 == 0) and not(ano_str[2:] == "00"):
    print('BISSEXTO!')
else:
    print('NÃO É BISSEXTO!')