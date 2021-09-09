from random import randint
from time import sleep

class Personagem:
    def __init__(self, nome, nivel, vida_total, qtd_ataque):
        self.nome = nome
        self.nivel = nivel
        self.qtd_ataque = qtd_ataque
        self.vida_total = vida_total
        self.qtd_vida = vida_total

    def __str__(self):
        return f"Nome: {self.nome}\nNivel: {self.nivel}\nVida: {self.vida_total}\nAtaque: {self.qtd_ataque}"

    def vida_atual(self):
        print(f"Vida atual de {self.nome}: {self.qtd_vida} de {self.vida_total}")

    def ataque(self, alvo):
        dano = randint(0, self.qtd_ataque)
        alvo.qtd_vida -= dano
        print(f"{alvo.nome} recebeu {dano} de dano de {self.nome}\n")

    def morte(self):
        return self.qtd_vida <= 0

class Player(Personagem):
    def __init__(self, nome, arma_incial, nivel=1, vida_total=50, qtd_ataque=10):
        super().__init__(nome, nivel, vida_total, qtd_ataque)
        self.experiencia_atual = 0
        self.experiencia_prox_nivel = 20
        self.inventario = []
        self.arma_atual = arma_incial
        self.equipar_arma(arma_incial)

    def __str__(self):
        return f"****** Status ******\nNome: {self.nome}\nNivel: {self.nivel}\nVida: {self.vida_total}\nAtaque: {self.qtd_ataque}\nArma atual: {self.arma_atual.nome}\n"

    def acao(self, alvo):
        while True:
            print("Ações:\n1)Atacar\n2)Inventário\n3)Status")
            acao = int(input("Escolha sua ação: "))
            print()

            if (acao == 1):
                self.ataque(alvo)
                break

            elif acao == 2:
                self.abrir_invetario()

            elif acao == 3:
                print(self)
                sleep(1)

    def equipar_arma(self, arma):
        self.arma_atual = arma
        self.qtd_ataque += arma.dano

    def retirar_arma_atual(self):
        dano = self.arma_atual.dano
        self.qtd_ataque -= dano

    def abrir_invetario(self):
        print("****** Inventário ******")
        ind = 0
        for item in self.inventario:
            print(f"{ind}. {item.nome}")
            ind += 1

        escolha = int(input("Selecionar item: "))
        item_escolhido = self.inventario[escolha]

        if item_escolhido.tipo == 'arma':
            self.retirar_arma_atual()
            self.equipar_arma(item_escolhido)
            print(f"Você equipou {item_escolhido.nome}\n")
            sleep(1.5)

    def recebe_experiencia(self, experiencia):
        print(f"Você ganhou {experiencia} de experiência.")
        self.experiencia_atual += experiencia
        self.evoluir()

    def evoluir(self):
        if self.experiencia_atual >= self.experiencia_prox_nivel:
            print("Você subiu de nível!")
            self.nivel += 1
            self.experiencia_prox_nivel *= 2
            self.qtd_ataque += 10
            self.vida_total += 25


class Mob(Personagem):
    def dropar_experiencia(self, player):
        experiencia = randint(self.nivel * 2, self.nivel * 4)
        player.recebe_experiencia(experiencia)



