from inimigo import Inimigo
import random

class Chefe(Inimigo):
    def __init__(self, nome, hp, ep, atk, dfs, inte, item, arma, loot, descricao, bonus, equipamento):
        super().__init__(nome, hp, ep, atk, dfs, inte, item, arma, loot, descricao)
        self.bonus = bonus
        self.equipamento = equipamento

    def chefe_aparece(self):
        return f"{self.descricao}"

    def chefe_morre(self):
        return f"As paredes da masmorra estremecem com um rugido profundo enquanto o Guardião {self.nome} cai derrotado. Sua forma monstruosa contorce-se uma última vez antes de se desfazer em névoa sombria, como se nunca tivesse existido. No centro da sala silenciosa, o chão se abre suavemente, revelando um antigo altar de pedra. Sobre ele repousa uma relíquia envolta em luz pulsante, como se respirasse magia pura. A energia que emana do objeto parece reconhecer sua vitória, e te chama silenciosamente para empunhá-la."
    
    def calcula_bonus(self):
        dado = random.randint(1, 6)
        return self.bonus + dado

def turno_chefe(chefe, jogador):
    import random

    print(f"\n{chefe.nome} encara você com olhos flamejantes...")
    fala = random.randint(1, 10)
    if fala % 2 == 0:
        print(chefe.gera_dialogo())

    print(f"\n{chefe.nome} prepara um ataque poderoso!")

    dano = chefe.calcula_dano() + chefe.calculaBonus() 

    if hasattr(jogador, 'tentando_esquivar') and jogador.tentando_esquivar:
        jogador.tentando_esquivar = False
        if jogador.esquiva():
            print(f"{jogador.nome} esquivou do ataque do chefe!")
            return
        else:
            print(f"{jogador.nome} tentou esquivar, mas falhou!")

    if hasattr(jogador, 'defendendo') and jogador.defendendo:
        jogador.defendendo = False
        defesa = jogador.defende()
        dano -= defesa

    jogador.hp -= max(0, dano)
    if jogador.hp < 0:
        jogador.hp = 0

    print(f"{jogador.nome} recebeu {max(0, dano)} de dano do chefe. HP atual: {jogador.hp}")
