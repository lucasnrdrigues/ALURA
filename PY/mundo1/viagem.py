dist = int(input("Qual a distância em Km? \n"))
if dist < 200:
    print(f"Valor passagem: R${(dist * 0.50):.2f}")
else:
    print(f"Valor passagem: R${(dist * 0.45):.2f}")