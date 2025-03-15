# AULA 1 DE FUNÇÕES
# FUNÇÃO BÁSICA
def display_investigation_message():
	print("Insvestigate Ativity")


# OBS: no pycharm, ele irá pedir para pular duas linhas depois de criar uma função !
# Chamando a funcão, sem a chamada ela não roda !!!
display_investigation_message()


# FUNÇÃO COM PARÂMETRO
def titulo(txt):
	print('-' * 30)
	print(txt)
	print('-' * 30)

# Chamando a função
titulo('CURSO EM VIDEO')
titulo('PROFESSOR: GUSTAVO GUANABARA')
titulo('PYTHON - MUNDO 3')


# EXEMPLO 2
def soma(a, b):
	s = a + b
	print(s)

# Chamando a função
soma(2, 8)
# Podemos chamar a função assim também
soma(a=2, b=8)


# EMPACOTANDO PARÂMETROS EM UMA TUPLA - passando quantidades diferentes de parametros em uma funcao
def contador(* num): # O asterisco é o sinal de desempacotar(o python entende que podemos passar diferentes qntd de parâmetros, ou seja, é um "coringa")
	print(num)

contador(2, 3, 4, 5)

# EXEMPLO 2
def contador(* num): # Podemos trabalhar com o FOR dentro de função assim como trabalhamos com as tuplas
    for valor in num: # Desta forma ele mostra os valores pulando as linhas, e não como no ex acima !
	    print(valor)
		
contador(2, 3, 4, 5)

# EXEMPLO 3 - mostrando a quantidade de parâmetros passados
def contador(* num):
    tam = len(num)
    print(f'Quantidade de parâmetros: {tam}')

contador(2, 3, 4, 5)

# EXEMPLO 4 - TRABALHANDO COM LISTA NAS FUNÇÕES
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores) # Chamando a função
print(valores) # Imprimindo o resultado
