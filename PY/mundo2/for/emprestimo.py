casa = int(input('Qual o valor da casa? '))
sal = int(input('Quanto é o seu salário? '))
anos = int(input('Em quantos anos você vai pagar? '))

prest = casa / (anos * 12)
cond = sal * (30/100)

print(f"Valor da prestação: R${prest:.2f}")
print(f'Valor de 30% do salário: R${cond:.2f}')

if prest > cond:
    print("Empréstimo negado!")
else:
    print("Empréstimo aprovado!")
