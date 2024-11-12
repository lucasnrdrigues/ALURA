primeiro = int(input("Qual é o primeiro termo? "))
razao = int(input("Qual é a razão? "))
decimo = primeiro + (10 - 1) * razao
somatoria = 0

for c in range(primeiro, decimo + razao, razao):
    print(c, end=' -> ')
    somatoria += c
print("ACABOU!")
print(f"Somatória = {somatoria}")

