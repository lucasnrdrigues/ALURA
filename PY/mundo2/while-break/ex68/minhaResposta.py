from random import randint

# Contadores de vitória
# OBSERVAÇÃO: Se o contador ficasse dentro do loop,sempre que o loop fosse reinciado, elas iriam zerar !
v_jogador = 0
v_pc = 0

while True:
    print(f'-' * 20)
    print(f'VAMOS JOGAR PAR OU ÍMPAR')
    print(f'-' * 20)

    # Fazendo as escolhas de impar ou par
    escolha_jogador = str(input('Você escolhe par ou impar ? ')).strip().lower()
    if escolha_jogador == 'par':
        escolha_pc = 'impar'
    else:
        escolha_pc = 'par'

    # Fazendo as jogadas
    jogada_jogador = input('Faça a sua jogada entre 0 e 10: ')

    while not jogada_jogador.isdigit():
        print("Entrada inválida! Digite um número inteiro.")
        jogada_jogador = input('Faça a sua jogada entre 0 e 10: ')

    jogada_pc = randint(0, 10)

    # Realizando a soma das jogadas
    soma = int(jogada_jogador) + jogada_pc

    # Mostrando as jogadas
    print(f'-' * 10)
    print(f'Sua jogada: {jogada_jogador}\nJogada do pc: {jogada_pc}\nSoma das jogadas: {soma}')
    print(f'-' * 10)

    # Lógica para ver quem venceu
    if soma % 2 == 0:
        if escolha_jogador == 'par':
            v_jogador += 1
            vencedor = "JOGADOR"
        else:
            v_pc += 1
            vencedor = "COMPUTADOR"
    if soma % 2 != 0:
        if escolha_jogador == 'impar':
            v_jogador += 1
            vencedor = 'JOGADOR'
        else:
            v_pc += 1
            vencedor = 'COMPUTADOR'

    # Mostrando quem venceu
    print(f'#' * 20 )
    print(f'VENCEDOR: {vencedor}')
    print(f'#' * 20 )
    # Mostrando o número de vitórias de cada um
    print(f'Vitórias do jogador: {v_jogador}')
    print(f'Vitórias do computador: {v_pc}')

    # Verificando se quer jogar novamente
    r = str(input('Quer jogar outra (sim ou nao) ? ')).strip().lower()
    if r == 'nao':
        break