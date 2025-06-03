from personagem import Personagem
import dungeon_dict as dndata
import random

class Inimigo(Personagem):
    def __init__(self, nome, hp, ep, atk, dfs, int, arma, loot, descricao):
        super().__init__(nome, hp, ep, atk, dfs, int, arma)
        self.loot = loot
        self.descricao = descricao

    @property
    def inimigo_vivo(self):
        return self._hp > 0
    
    def aparece(self):
        return f"{self.descricao}"
    
    def morre(self):
        return f"Ao dar seu último ataque, o corpo danificado do {self.nome} se desfalece e desaparece em uma nuvem de névoa negra."

    def larga_loot(self):
        chance = random.randint(1, 20)
        if chance % 4 == 0:
            print(f"Enquanto a nuvem de névoa se dissipa, você vê o formato de algo em meio à todo o miasma, você observa até conseguir discernir o objeto no chão. Em meio à sala escura você enxerga um {self.loot}")
        return True

    def geraDialogo(self):
        return f"{self.nome} ruge ameaçadoramente."
    
def turno_inimigo(inimigo, jogador):
    print(f"\n{inimigo.nome} ataca!")

    dano = inimigo.calcula_dano()

    if hasattr(jogador, 'tentando_esquivar') and jogador.tentando_esquivar:
        jogador.tentando_esquivar = False
        if jogador.esquiva():
            print(f"{jogador.nome} esquivou do ataque!")
            return
        else:
            print(f"{jogador.nome} tentou esquivar, mas falhou!")

    if hasattr(jogador, 'defendendo') and jogador.defendendo:
        jogador.defendendo = False
        defesa = jogador.defende()
        dano -= defesa

    jogador.hp -= max(0, dano)
    if jogador.hp < 0 : jogador.hp = 0
    print(f"{jogador.nome} recebeu {max(0, dano)} de dano. HP atual: {jogador.hp}")
