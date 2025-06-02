import random

class Personagem:
    def __init__(self, nome, classe, hp, ep, atk, dfs, int, arma):
        self.nome = nome
        self.classe = classe
        self.hp = hp
        self.ep = ep
        self.atk = atk
        self.dfs = dfs
        self.int = int
        self.arma = arma

    def mostra_atributos(self):
        return f"Atributos - ATK: {self.atk}, DFS: {self.dfs}, INT: {self.int}"
    
    def calcula_dano(self):
        return self.atk + self.arma.get("efeito", 0)
    
    def ataca(self, alvo):
        dano = self.calcula_dano()
        return alvo.receber_ataque(dano)

    def defende(self):
        dado = random.randint(1,20)
        if dado < self.dfs * 5:
            print(f"A defesa falhou! (D20: {dado})")
            return 0
        else:
            valor = self.dfs + 5
            print(f"Ataque defendido! {self.dfs + 5} de dano foram anulados!")
            return valor
    
    def esquiva(self):
        dado = random.randint(1, 20)
        print(f"{self.nome} tentou se esquivar do ataque! (d20: {dado})")
        return dado % 6 == 0
    
    def receber_ataque(self, dano):
        dano_final = max(dano, 0)
        self.hp -= dano_final
        return f"{self.nome} recebeu {dano_final} de dano. HP restante: {self.hp}"
    

