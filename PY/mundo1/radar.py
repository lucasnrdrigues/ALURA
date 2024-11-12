vel = int(input("Qual a velocidade(em Km/h)? \n") )
if vel > 80:
    print("Multa!")
    print(f"Sua multa foi de R${((vel - 80) * 7):.2f}!")
else:
    print("Sem multa!")
