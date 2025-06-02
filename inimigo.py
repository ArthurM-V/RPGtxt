from personagem import Personagem
import dungeon_dict as dndata
import random

class Inimigo(Personagem):
    def __init__(self, nome, hp, ep, atk, dfs, int, item, loot, descricao):
        super().__init__(nome, hp, ep, atk, dfs, int, item)
        self.loot = loot
        self.descricao = descricao

    @property
    def inimigo_vivo(self):
        return self._hp > 0

    def gera_hordas(self, num_horda):
        lista_horda = []
        for i in range(num_horda):
            grupos = [] 
            mon_num = random.randint(1, 3)
            for j in range(mon_num):
                monstro = random.choice(list(dndata.inimigos_base))
                grupos.append(monstro)
            lista_horda.append(grupos)
        return lista_horda
    
    def aparece(self):
        return f"{self.descricao}"
    
    def morre(self):
        return f"Ao dar seu último ataque, o corpo danificado do {self.nome} se desfalece e desaparece em uma nuvem de névoa negra."

    def largaLoot(self):
        chance = random.randint(1, 20)
        if chance % 4 == 0:
            print(f"Enquanto a nuvem de névoa se dissipa, você vê o formato de algo em meio à todo o miasma, você observa até conseguir discernir o objeto no chão. Em meio à sala escura você enxerga um {self.loot}")
        return self.loot

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
    print(f"{jogador.nome} recebeu {max(0, dano)} de dano. HP atual: {jogador.hp}")
