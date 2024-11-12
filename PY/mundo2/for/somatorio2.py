# Somatório mostrando as operações
s = 0
for c in range(0,6):
    n = int(input('Digite um número para somarmos: '))
    s += n
    print(f'{s - n} + {n} = {s}')
print(f'{s}')
print('FIM !')