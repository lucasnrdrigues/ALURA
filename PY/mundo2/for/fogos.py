import time
for c in range(10,0, -1):
    time.sleep(1)
    print(c)
time.sleep(1) # Esse último sleep é para ficar 1s antes de acabar
print('Feliz Ano novo!')