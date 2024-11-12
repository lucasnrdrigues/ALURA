km = float(input('Digite o valor de Km percorridos: '))
dias = int(input('Digite a quantidade de dias alugados: '))
preco = (90 * dias) + (0.20 * km)
print(f'Preço Total: R${preco:.2f} ')