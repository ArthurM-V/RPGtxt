from item import Item

class Arma(Item):
    def __init__(self, nome, efeito, usos, tipo, habilidade_primaria, habilidade_secundaria,):
        super().__init__(nome, efeito, usos, tipo)
        self.habilidade_primaria = habilidade_primaria
        self.habilidade_secundaria = habilidade_secundaria
        self.nome = nome

    def usar_primaria(self, atacante, alvo):
        return self.habilidade_primaria.usar_habilidade(atacante, alvo)
    
    def usar_secundaria(self, atacante, alvo):
        return self.habilidade_secundaria.usar_habilidade(atacante, alvo)

    def dados(self):
        return f"Arma: {self.nome} \nHabilidade primária: {self.habilidade_primaria.nome},\nHabilidade secundária: {self.habilidade_secundaria.nome}"
