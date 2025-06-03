import random
import dungeon_dict as dndata

class Sala:
    def __init__(self, tipo, aparencia, tesouro):
        self.tipo = tipo
        self.aparencia = aparencia
        self.tesouro = tesouro

    def narra_sala(self, tipo):
        return f"Ao atravessar a porta, nota que é possível enxergar algo além dela, uma sala silenciosa, envolta em mistério, esperando para ser revelada. {random.choice(list(dndata.tipo_salas[tipo]))}, com {self.aparencia}."

    def tem_inimigos(self):
        chance = random.randint(1, 20)
        if chance % 2 == 0:
            return True
        else:
            return False
    
    def calcula_encontros(self):
        
        num_horda = random.randint(1, 3)
        
        return num_horda
    
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

    def tem_loot(self):
        
        chance = random.randint(1, 6)

        if chance % 2 == 0:
            return True
        else:
            return False
        
    def revela_loot(self, chance):

        if chance:
            return f"\n\t========== Você encontrou {self.tesouro.nome}!==========\n"
        else:
            return f"Ao investigar a sala, você não encontrou nada!"


