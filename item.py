class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

class Arma(Item):
    def __init__(self, nome, tipo, dano):
        super().__init__(nome, tipo)
        self.dano = dano

    def __str__(self):
        return f"Nome: {self.nome}\nDano: {self.dano} de Dano de Ataque"

class Pocao(Item):
    def __init__(self, nome, qtd_cura):
        self.qtd_cura = qtd_cura

