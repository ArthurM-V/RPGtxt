from inimigo import Inimigo

class Chefe(Inimigo):
    def __init__(self, nome, hp, ep, inventario, loot, bonus, equipamento):
        super().__init__(nome, hp, ep, inventario, loot)
        self.bonus = bonus
        self.equipamento = equipamento

    def calculaBonus(self):
        return self.bonus

    def deixaArma(self):
        return self.equipamento
