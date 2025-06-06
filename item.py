import dungeon_dict as dndata

class Item:
    def __init__(self, nome, efeito, usos, tipo):
        self.nome = nome
        self.efeito = efeito
        self.usos = usos
        self.tipo = tipo
    
    def item_info(self):
        mensagem = f"{self.nome} | Efeito: {self.tipo} + {self.efeito} | Usos: {self.usos}"
        return mensagem

    def usar(self):
        if self.usos > 0:
            self.usos -= 1 
            if self.usos == 0:
                return f"O item {self.nome} foi totalmente consumido!"
            else:
                return f"Você usa o item {self.nome} e o guarda novamente. Usos restantes: {self.usos}"
        else:
            return f"O item {self.nome} já foi totalmente consumido e não pode ser usado."
        
    def largar(self, jogador):
        jogador.item = None
        return f"Você descartou {self.nome}!"