import datetime
atual = datetime.date.today().year  # Ou from datetime import date, linha debaixo: atual = date.today().year
maior = 0
menor = 0
for c in range(0,7):
    ano = int(input('Em que ano nasceu a primeira pessoa?: '))
    if atual - ano >= 18:
        maior +=1
    else:
        menor += 1
print(f'Maior idade: {maior}\nMenor idade: {menor}')