nome = str(input('Digite o seu nome: '))
salario = float(input('Digite o valor o seu salário: '))
anos_trab = int(input('Digite a quantos anos você trabalha na empresa: '))
novo_sal = 0
if anos_trab < 3:
    novo_sal = salario + (salario * 0.03)
elif anos_trab >= 3 and anos_trab < 10:
    novo_sal = salario + (salario * 0.125)
else:
    novo_sal = salario + (salario * 0.2)
print(f'Nome: {nome}')
print(f'salario: {salario}')
print(f'NOVO salário: {novo_sal}')