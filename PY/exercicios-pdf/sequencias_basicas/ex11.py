a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
delta = b**2 - 4 * a * c
x1 = (-b + delta**(1/2))/2*a
x2 = (-b - delta**(1/2))/2*a

print(f'Delta = {delta}')
print(f'X1 = {int(x1)}')
print(f'X2 = {int(x2)}')