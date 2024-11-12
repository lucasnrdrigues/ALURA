num = int(input('Digite um número: '))
n = str(num)
print(f'Analisando o número: {n}')
print(f'Unidade: {n[3]}')
print(f'Unidade: {n[2]}')
print(f'Unidade: {n[1]}')
print(f'Unidade: {n[0]}')

# Resolvendo matematicamente:
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número: {num}')
print(f'Unidade: {u}')
print(f'Unidade: {d}')
print(f'Unidade: {c}')
print(f'Unidade: {m}')