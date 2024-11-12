vel = float(input("Digite o valor da velocidade do carro: "))
if vel > 80:
    multa = (vel - 80) * 5
    print("MULTADO!")
    print(f"VALOR: R${multa:.2f}")
else:
    print("SEM MULTA!")