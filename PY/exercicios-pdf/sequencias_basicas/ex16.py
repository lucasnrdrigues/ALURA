cigarros = int(input('Digite a quantidade de cigarros fumados por dias: '))
anos = int(input('Digite a quantidade de anos que já fumou: '))

minutos_perdidos_dia = cigarros * 10
total_minutos = minutos_perdidos_dia * (365 * anos)
total_dias = total_minutos / 1440

print(f'Voce perdeu {int(total_dias)} dias de vida !')