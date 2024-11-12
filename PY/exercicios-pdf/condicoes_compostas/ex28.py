largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
m2 = largura * altura

if m2 < 100:
    print('TERRENO POPULAR')
elif m2 >= 100 and m2 < 500:
    print('TERRENO MASTER')
else:
    print('TERRENO VIP')
