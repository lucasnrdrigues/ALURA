import random
n = int(input("Tente advinhar um número de 0 a 5: "))

if n == random.randint(0,5):
    print("Parabéns!")
else:
    print("Você perdeu!")