import random
import dungeon_dict as dndata

class Sala:
    def __init__(self, tipo, aparencia, tesouro):
        self.tipo = tipo
        self.aparencia = aparencia
        self.tesouro = tesouro

    def narra_sala(self, tipo):
        return f"Ao adentrar a masmorra, atravessando corredores ameaçadores, você finalmente encontra uma porta. Ao se aproximar, nota que é possível enxergar algo além dela, uma sala silenciosa, envolta em mistério, esperando para ser revelada. {random.choice(list(dndata.tipo_salas[tipo]))}, com {self.aparencia}."

    def tem_inimigos(self):
        chance = random.randint(1, 20)
        if chance % 5 == 0:
            return True
        else:
            return False
    
    def calcula_encontros(self):
        
        num_horda = random.randint(1, 3)
        
        return num_horda

    def revelaLoot(self, chance, jogador):

        loot_chance = chance + jogador.int

        if(loot_chance % 2 == 0):
            loot_encontrado = random.choice(list(dndata.tesouro_salas.keys()))
            return f"Ao investigar a sala, você achou {loot_encontrado}!"
        else:
            return f"Ao investigar a sala, você não encontrou nada!"
    

