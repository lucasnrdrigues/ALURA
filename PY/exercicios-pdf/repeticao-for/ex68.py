mulheres = 0
homens_peso_cem = 0
peso_mulheres = 0
maior_peso_homem = 0

for p in range(1, 5):
    sexo = str(input('Digite o seu sexo(m/f): ').lower())
    peso = float(input('Digite o seu peso: '))
    if sexo == 'f':
        peso_mulheres += peso
        mulheres += 1

    if sexo == 'm' and peso > 100:
        homens_peso_cem += 1

    if sexo == 'm' and peso > maior_peso_homem:
        maior_peso_homem = peso

print(f'Quantas mulheres foi cadastrada: {mulheres}')
print(f'Quantos homens tem mais de 100KG: {homens_peso_cem}')
if mulheres == 0:
    print(f'Média peso mulheres = 0')
else:
    print(f'Média peso mulheres = {peso_mulheres/mulheres}')
print(f'Maior peso entre os homens: {maior_peso_homem}')