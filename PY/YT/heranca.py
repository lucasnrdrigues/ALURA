# Polimorfismo(muitas formas) é a capacidade de diferentes classes responderem de maneira diferente a uma mesma mensagem (ou método). Em outras palavras, o mesmo nome de método pode ter comportamentos diferentes dependendo do objeto que o invoca.
# No exemplo abaixo, preste atenção no método defender da classe mãe, se ele for usado na subclasse Jogador_Goleiro ele terá uma reação e se ele for usado na subclasse Jogador_Linha ele terá outra reação
class Jogador:
    def __init__(self, altura, velocidade, passe, drible, precisao):
        self.altura = altura
        self.velocidade = velocidade
        self.passe = passe
        self.drible = drible
        self.precisao = precisao

    def passar(self):
        print('Mirar')
        print('Encostar na bola com a força de passe do jogador')

    def chutar(self):
        print('Mirar')
        print('Encostar na bola com 2x a força de passe do jogador')

    def defender(self):
        # Por padrão vamos deixar o print abaixo, porque caso a subclasse não identifique o que o método defender irá fazer, ele terá o print abaixo por padrão, mas caso contrário, podíamos usar somente a palavra "pass" para não termos que colocar algum código dentro para que especificassemos depois
        print('Tentar tirar a bola do adversário')

class Jogador_Goleiro(Jogador):
    def agarrar(self):
        print('Pular')
        print('Se esticar para pegar a bola')

    def defender(self):
        esta_fora_area = False
        if esta_fora_area:
            print('Usar apenas os pés, cabeça, ombro')
        else:
            print('Usar qualquer parte do corpo')
        print('Tentar tirar a bola do adversário')

class Jogador_Linha(Jogador):
    def defender(self):
        print('Usar apenas os pés, cabeça, ombro')
        print('Tentar tirar a bola do adversário')

jogador1 = Jogador_Goleiro(180, 60, 60, 50, 70)
jogador2 = Jogador_Linha(179, 90, 80, 85, 90)

jogador1.defender()
jogador2.defender()

# Exemplo 2 
class Cachorro:
    def fazer_som(self):
        return "Au au!"

class Gato:
    def fazer_som(self):
        return "Miau!"

# Função que usa polimorfismo
def emitir_som(animal):
    print(animal.fazer_som())

c = Cachorro()
g = Gato()

emitir_som(c)  # Saída: Au au!
emitir_som(g)  # Saída: Miau!

