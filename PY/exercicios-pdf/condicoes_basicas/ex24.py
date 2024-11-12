dist_km = float(input('Digite a distância que você deseja percorrer em KM: '))
preco_passagem = 0
if dist_km <= 200:
    preco_passagem = dist_km * 0.5
else:
    preco_passagem = dist_km * 0.45

print(f'Preço da passagem: R${preco_passagem:.2f}')