print('Números pares de 1 a 50: ')
for c in range(0, 51, 2): # Até 51, assim ele pega até o 50!
    print(c)
print('FIM !')

# Segunda forma de fazer isso:
for c in range(1,51):
    if c % 2 == 0:
        print(c)
print("FIM !")