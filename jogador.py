import dungeon_dict as dndata
from personagem import Personagem
from habilidade import Habilidade

class Jogador(Personagem):
    def __init__(self, nome, classe, hp, ep, atk, dfs, int, item, arma, habilidades):
        super().__init__(nome, classe, hp, ep, atk, dfs, int, arma)
        self.item = item
        self.habilidades = habilidades

    @property
    def jogador_vivo(self):
        return self.hp > 0

    def equipa_arma(self):
        arma = dndata.armas_iniciais[self.classe]
        self.arma = arma  
        dndata.arma_equipada.append(arma)  
        return f"{self.nome} equipou a arma: {arma['nome']}"

    def guarda_item(self, item):
        self.item = item
        dndata.item_equipado.append(item)
        return f"Item {item.nome} equipado"
    
    def usar_item(self):
        if not self.item:
            return "Nenhum item equipado."

        tipo = self.item.tipo
        efeito = self.item.efeito

        if tipo == "hp":
            self.hp += efeito
            mensagem = f"{self.nome} usou {self.item.nome} e recuperou {efeito} de HP!"
        elif tipo == "ep":
            self.ep += efeito
            mensagem = f"{self.nome} usou {self.item.nome} e recuperou {efeito} de EP!"
        else:
            mensagem = f"O item {self.item.nome} não teve efeito conhecido."

        resultado = self.item.usar()
        if "totalmente consumido" in resultado:
            self.item = None  

        return f"{mensagem}\n{resultado}"

    def largar(self):
        if hasattr(self, 'item') and self.item in dndata.item_equipado:
            dndata.item_equipado.remove(self.item)
            item_largado = self.item
            del self.item  
            return f"Item {item_largado.nome} largado."
        else:
            return "Nenhum item equipado para largar."
    
    def descreve_habilidades(self):
        for i, habilidade in enumerate(self.habilidades):
            print(f"{i+1}. {habilidade.nome}, {habilidade.descricao}")
        return

def turno_jogador(jogador, inimigo):

    while True:
        print("\t\t\n=====SEU TURNO=====\n")

        print(f"Hp: {jogador.hp}\nEp: {jogador.ep}\n----------")
        print("Decida a sua ação no turno!")
        print("1.Ataque Básico! \t2.Defender \t3.Esquivar")
        print(f"4.{jogador.arma.habilidade_primaria.nome} | custo: {jogador.arma.habilidade_primaria.custo_ep} \t 5.{jogador.arma.habilidade_secundaria.nome} | custo: {jogador.arma.habilidade_secundaria.custo_ep}")
        escolha = input("Escolha sua ação:\n>> ")

        if escolha == "1":
            dano = jogador.calcula_dano()
            inimigo.hp -= dano
            print(f"Você atacou {inimigo.nome} e causou {dano} de dano!")
            break

        elif escolha == "2":
            print(jogador.arma.usar_primaria(jogador, inimigo))
            break

        elif escolha == "3":
            print(jogador.arma.usar_secundaria(jogador, inimigo))
            break

        elif escolha == "4":
            jogador.defendendo = True  # um flag para ser usado quando receber ataque
            print("Você se preparou para defender o próximo ataque.")
            break

        elif escolha == "5":
            jogador.tentando_esquivar = True  # outro flag
            print("Você se posicionou para tentar esquivar do próximo ataque.")
            break

        else:
            print("Opção inválida. Escolha novamente.")