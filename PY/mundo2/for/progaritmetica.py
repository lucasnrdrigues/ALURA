primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao): # decimo + razao para ele ir pro próximo, lembre-se que o python ele não conta o último número!
    print(f'{c}', end=' -> ')
print('ACABOU !')