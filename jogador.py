import dungeon_dict as dndata
import random
from personagem import Personagem
from habilidade import Habilidade

class Jogador(Personagem):
    def __init__(self, nome, classe, hp, ep, atk, dfs, inte, item, arma, habilidades):
        super().__init__(nome, classe, hp, ep, atk, dfs, inte)
        self.classe = classe
        self.arma = arma
        self.item = item
        self.habilidades = habilidades

    @property
    def jogador_vivo(self):
        return self.hp > 0
    @jogador_vivo.setter
    def jogador_vivo(self, valor):
        pass

    def mostra_equipamento(self, jogador):
         
        if self.item:
            item_info = self.item.item_info()
        else:
            item_info = "Nenhum item equipado"

        if self.arma:
            arma_info = self.arma.dados()
        else:
            arma_info = "Nenhuma arma equipada"

        return f"Classe: {self.classe}\t{jogador.mostra_atributos()}\nHP: {self.hp}\tEP: {self.ep}\nItem: {item_info}\nArma: {arma_info}"

    def equipa_arma(self):
        arma = dndata.armas_iniciais[self.classe]
        self.arma = arma  
        dndata.arma_equipada.append(arma)  
        return f"{self.nome} equipou a arma: {arma['nome']}"

    def guarda_item(self, item):

        if self.item is None:
            self.item = item
            
            return f"Item {item.nome} equipado"
        else:
            return f"Você já tem {self.item.nome} equipado!"

    def usar_item(self):
        if not self.item:
            return "Nenhum item equipado."

        tipo = self.item.tipo
        efeito = self.item.efeito
        hp_max = dndata.classes[self.classe]["hp"]
        ep_max = dndata.classes[self.classe]["ep"]

        if tipo == "hp":
            self.hp = min(hp_max, self.hp + efeito)
            mensagem = f"{self.nome} usou {self.item.nome} e recuperou {efeito} de HP!"
        elif tipo == "ep":
            self.ep = min(ep_max, self.ep + efeito)
            mensagem = f"{self.nome} usou {self.item.nome} e recuperou {efeito} de EP!"
        elif tipo == "cura":
            self.hp = min(hp_max, self.hp + efeito)
            self.ep = min(ep_max, self.ep + efeito)
            mensagem = f"{self.nome} usou {self.item.nome} e recuperou {efeito} de HP e EP!"
        elif tipo == "atk":
            self.atk += efeito
            mensagem = f"{self.nome} usou {self.item.nome} e ganhou {efeito} de ataque!"
        elif tipo == "dfs":
            self.dfs += efeito
            mensagem = f"{self.nome} usou {self.item.nome} e ganhou {efeito} de defesa!"
        elif tipo == "inte":
            self.inte += efeito
            mensagem = f"{self.nome} usou {self.item.nome} e ganhou {efeito} de inteligência!"
        else:
            mensagem = f"O item {self.item.nome} não teve efeito conhecido."

        resultado = self.item.usar()
        if "totalmente consumido" in resultado:
            self.item = None  

        return f"{mensagem}\n{resultado}"

    def largar(self):
        if self.item:
            item_largado = self.item
            self.item = None
            return f"Item {item_largado.nome} largado."
        else:
            return "Nenhum item equipado para largar."
    
    def descreve_habilidades(self):
        for i, habilidade in enumerate(self.habilidades):
            print(f"{i+1}. {habilidade.nome}, {habilidade.descricao}")
        return

    def calcula_dano(self):

        dado = random.randint(1, 6)

        if self.arma.tipo == "atk":
            dano = self.atk * self.arma.efeito + dado
        elif self.arma.tipo == "inte":
            dano = self.inte * self.arma.efeito + dado
        
        return dano

def menu_item(jogador, sala):

    print(f"---------------\n\n{jogador.nome} | HP: {jogador.hp} EP: {jogador.ep}\n")
    if jogador.item:
        print(f"Item equipado atual: {jogador.item.nome}: {jogador.item.tipo} + {jogador.item.efeito}")
    else:
        print("Item equipado atual: Nenhum")
    print(f"{sala.tesouro.nome} | Efeito: {sala.tesouro.tipo} + {sala.tesouro.efeito}\n---------------")
    index = False
    while index == False:
        if jogador.item is not None:
            escolha = input(f"\n===Você já tem um item equipado!===\n\nVocê pode escolher entre:\n1.Consumir o seu item equipado e trocar pelo encontrado. \t2.Ignorar o item encontrado.\n>>")

            if escolha == "1":
                print(f"Você usou {jogador.item.nome} e equipou {sala.tesouro.nome}")
                print(jogador.usar_item())
                jogador.guarda_item(sala.tesouro)
                break
            elif escolha == "2":
                print(f"Você trocou {jogador.item.nome} por {sala.tesouro.nome}")
                jogador.largar()
                jogador.guarda_item(sala.tesouro)
                break
            else:
                print("Escolha inválida")
                continue        
        else:
            escolhe = input("1.Equipar item encontrado \t2.Ignorar item\n>>")
            if escolhe == "1":
                jogador.guarda_item(sala.tesouro)
                input(f"Você equipou {sala.tesouro.nome}")
                break
            elif escolhe == "2":
                input(f"Você ignora {sala.tesouro.nome} e continua sua exploração.")
                break
            else:
                print("Opção inválida!")
                continue

def turno_jogador(jogador, inimigo):

    while True:
        print("\t\t\n=====SEU TURNO=====\n")

        print(f"Hp: {jogador.hp}\nEp: {jogador.ep}\n----------")
        print("Decida a sua ação no turno!")
        print("1.Ataque Básico! \t2.Defender \t3.Esquivar")
        print(f"4.{jogador.arma.habilidade_primaria.nome} | custo: {jogador.arma.habilidade_primaria.custo} \t 5.{jogador.arma.habilidade_secundaria.nome} | custo: {jogador.arma.habilidade_secundaria.custo}")
        escolha = input("Escolha sua ação:\n>> ")

        if escolha == "1":
            dano = jogador.calcula_dano()
            inimigo.hp -= dano
            print(f"Você atacou {inimigo.nome} e causou {dano} de dano!")
            break

        elif escolha == "2":
            jogador.defendendo = True  # um flag para ser usado quando receber ataque
            print("Você se preparou para defender o próximo ataque.")
            break

        elif escolha == "3":
            jogador.tentando_esquivar = True  # outro flag
            print("Você se posicionou para tentar esquivar do próximo ataque.")
            break

        elif escolha == "4":
            print(jogador.arma.usar_primaria(jogador, inimigo))
            break

        elif escolha == "5":
            print(jogador.arma.usar_secundaria(jogador, inimigo))
            break

        else:
            print("Opção inválida. Escolha novamente.")