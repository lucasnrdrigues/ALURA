n = int(input('Digite um número: '))
base = int(input('''Para qual base você quer converter?'
[1] - Octal
[2] - Hexadecimal
[3] - Binário \n'''))
if base == 1:
    n = oct(n)
    print(n[2:])
elif base == 2:
    n = hex(n)
    print(n[2:])
elif base == 3:
    n = bin(n)
    print(n)
else:
    print('Comando errado!')