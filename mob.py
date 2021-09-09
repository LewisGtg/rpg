from random import randint
class Mob:

    def __init__(self, nome, nivel, vida_total, qtd_ataque):
        self.nome = nome
        self.nivel = nivel
        self.qtd_ataque = qtd_ataque
        self.vida_total = vida_total
        self.qtd_vida = vida_total

    def vida_atual(self):
        print(f"Vida atual de {self.nome}: {self.qtd_vida} de {self.vida_total}")

    def ataque(self, alvo):
        dano = randint(0, self.qtd_ataque)
        alvo.qtd_vida -= dano
        print(f"Você sofreu {dano} de dano de {self.nome}")

    def morte(self):
        return self.qtd_vida <= 0