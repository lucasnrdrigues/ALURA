nome = str(input("Digite o seu nome: "))
n1 = float(input("Digite a sua primeria nota: "))
n2 = float(input("Digite a sua segunda nota: "))
media = (n1 + n2)/2

print(f"Sua Média: {media}")

if media >= 7:
    print("Você PASSOU!")
else:
    print("Você NÃO PASSOU!")

