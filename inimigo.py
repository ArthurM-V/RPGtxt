from personagem import Personagem
import dungeon_dict as dndata
import random

class Inimigo(Personagem):
    def __init__(self, nome, classe, hp, ep, atk, dfs, inte, item, loot, descricao):
        super().__init__(nome, classe, hp, ep, atk, dfs, inte)
        self.item = item
        self.loot = loot
        self.descricao = descricao

    def inimigo_vivo(self):
        return self.hp > 0

    def morre(self):
        return f"Ao dar seu último ataque, você vê o corpo danificado do {self.nome} se desfalecendo e desaparecendo em uma nuvem de névoa negra."

    def larga_loot(self):
        chance = random.randint(1, 20)
        if chance % 4 == 0:
            print(f"Enquanto o corpo do monstro se dissipa, você vê o formato de algo em meio à toda a névoa negra, você observa até conseguir discernir o objeto no chão. Em meio à sala escura você enxerga um {self.loot}")
            return True
        else:
            return False

    def gera_dialogo(self):
        return f"{self.nome} ruge ameaçadoramente."
    
def turno_inimigo(inimigo, jogador):
    fala = random.randint(0, 10)
    if fala % 2 == 0:
        print(inimigo.gera_dialogo())
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
    if jogador.hp < 0 : jogador.hp = 0
    print(f"{jogador.nome} recebeu {max(0, dano)} de dano. HP atual: {jogador.hp}")

def menu_loot(jogador, inimigo):
    print(f"---------------\n\n{jogador.nome} | HP: {jogador.hp} EP: {jogador.ep}\n")
    if jogador.item:
        print(f"Item equipado atual: {jogador.item.nome}: {jogador.item.tipo} + {jogador.item.efeito}")
    else:
        print("Item equipado atual: Nenhum")
    print(f"Item encontrado:{inimigo.item.nome} | Efeito: {inimigo.item.tipo} + {inimigo.item.efeito}\n---------------")
    index = False
    while index == False:
        if jogador.item is not None:
            escolha = input(f"\n===Você já tem um item equipado!===\n\nVocê pode escolher entre:\n1.Consumir o seu item equipado e trocar pelo encontrado. \t2.Ignorar o item encontrado.\n>>")

            if escolha == "1":
                print(f"Você usou {jogador.item.nome} e equipou {inimigo.item.nome}")
                print(jogador.usar_item())
                jogador.guarda_item(inimigo.item)
                break
            elif escolha == "2":
                print(f"Você ignora {inimigo.item.nome}.")
                break
            else:
                print("Escolha inválida")
                continue        
        else:
            escolhe = input("1.Equipar item encontrado \t2.Ignorar item\n>>")
            if escolhe == "1":
                jogador.guarda_item(inimigo.item)
                input(f"Você equipou {inimigo.item.nome}!")
                break
            elif escolhe == "2":
                input(f"Você ignora {inimigo.item.nome}.")
                break
            else:
                print("Opção inválida!")
                continue
