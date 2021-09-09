from personagem import Player, Mob
from item import Arma
from time import sleep

class Game:
    def __init__(self, nivel=0):
        self._player = None
        self.nivel = nivel

    def _carrega_mobs(self):
        goblin = Mob("Goblin", 1, 10, 5)
        mage_goblin = Mob("Mage Goblin", 5, 15, 5)
        king_goblin = Mob("King Goblin", 10, 20, 5)
        mobs = [goblin, mage_goblin, king_goblin]
        return mobs

    def _carrega_itens(self):
        arma1 = Arma("Espada de madeira", "arma", 10)
        arma2 = Arma("Espada de aço", "arma", 15)
        arma3 = Arma("Ferroada", "arma", 1500)
        armas = [arma1, arma2, arma3]
        return armas

    def _da_itens_iniciais(self, player):
        itens = self._carrega_itens()
        for item in itens:
            player.inventario.append(item)

    def _cria_player(self):
        nome = str(input("Qual vai ser o nome do personagem? "))
        arma_inicial = Arma("Espada de madeira", "arma", 10)

        self._player = Player(nome, arma_inicial)
        self._da_itens_iniciais(self._player)

        return self._player

    def play(self):
        mobs = self._carrega_mobs()
        player = self._cria_player()
        nivel = self.nivel

        while (not player.morte() and nivel <= 2):
            mob = mobs[nivel]
            self._imprime_mensagem(f"Seu inimigo é {mob.nome}", 2, 0, mob)
            rodada = 1

            while (not player.morte() and not mob.morte()):
                print("_________________________________")
                print(f"Rodada {rodada}\n")
                player.vida_atual()
                mob.vida_atual()
                print()

                self._imprime_mensagem("Seu turno", 1, 1)

                player.acao(mob)

                if mob.morte():
                    print(f"Você derrotou {mob.nome}\n")
                    mob.dropar_experiencia(player)
                    break

                self._imprime_mensagem("Turno do adversário", 1, 1)
                mob.ataque(player)

                rodada += 1
                sleep(2)

            nivel += 1

        if (not player.morte()):
            self._imprime_mensagem("Você venceu!!", 2)
        else:
            self._imprime_mensagem("Você perdeu =(", 2)

    def _imprime_mensagem(self, mensagem, tempo=0.5, animation=0, arg1=None):
        if animation == 0:
            print(mensagem)
            sleep(tempo)

        elif animation == 1:
            print(mensagem, end="", flush=True)
            print(".", end="", flush=True)
            sleep(tempo)
            print(".", end="", flush=True)
            sleep(tempo)
            print(".\n", flush=True)
            sleep(tempo)


if __name__ == "__main__":
    game = Game()
    game.play()