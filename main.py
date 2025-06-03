#Importa dicionários com dados das masmorras
import dungeon_dict as dndata
#Importa pacotes e classes
import os
import random
import user as us
import masmorra as ms
import salas as sl
import item as it
import jogador as jg
import personagem as ps
import inimigo as inm
import arma as ar
import habilidade as hb
import random

#Limpa o terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Gera as masmorras automaticamente com parâmetros aleatórios
def gera_masmorra():

    #acessa os dicionários aninhados e faz uma lista de strings com as suas chaves
    chave_nome = random.choice(list(dndata.nomes_masmorras.keys()))
    chave_origem = random.choice(list(dndata.origem.keys()))
    tipo = chave_origem
    chave_ambiente = random.choice(list(dndata.ambiente.keys()))
    chave_perigo = random.choice(list(dndata.perigo.keys()))
    chave_entrada = random.choice(list(dndata.entradas.keys()))    

    #usa a lista de strings para escolher os parâmetros do objeto, removendo os parâmetros escolhidos da lista de string para evitar repetições
    nome = random.choice(dndata.nomes_masmorras[chave_nome])
    dndata.nomes_masmorras[chave_nome].remove(nome)

    origem = random.choice(dndata.origem[chave_origem])
    dndata.origem[chave_origem].remove(origem)
    
    ambiente = random.choice(dndata.ambiente[chave_ambiente])
    dndata.ambiente[chave_ambiente].remove(ambiente)
    
    perigo = random.choice(dndata.perigo[chave_perigo])
    dndata.perigo[chave_perigo].remove(perigo)
    
    entrada = random.choice(dndata.entradas[chave_entrada])
    dndata.entradas[chave_entrada].remove(entrada) 

    #escolhe o número de salas
    num_salas = random.randint(6, 8)

    #retorna um objeto Masmorra
    return ms.Masmorra(nome, tipo, origem, ambiente, perigo, entrada, num_salas, chave_perigo)

#Gera tipos de salas
def gera_tipos_salas(num_salas):
    tipos_final = []

    tipos_final.append("guardião")
    tipos_final.append("loot")
    tipos_final.append("chefe")

    if dndata.limites_tipos["central"][1] >= 1:
        tipos_final.append("central")

    tipos_opcionais = ["vazia", "celas"]

    contador = {"vazia" : 0, "celas" : 0}

    while len(tipos_final) < num_salas:
        tipo = random.choice(tipos_opcionais)
        
        if contador[tipo] < dndata.limites_tipos[tipo][1]:
            tipos_final.append(tipo)
            contador[tipo] += 1
    tipos_sem_chefe = tipos_final[:-1]
    random.shuffle(tipos_sem_chefe)
    tipos_final = tipos_sem_chefe + ["chefe"]

    return tipos_final

#Gera as salas automaticamente de forma aleatória
def gera_sala(x, tipo=None):
    if tipo is None:
        chave_tipo = random.choice(list(dndata.tipo_salas.keys()))
        tipo = random.choice(dndata.tipo_salas[chave_tipo])

    aparencia = random.choice(list(dndata.aparencia_sala[x.tipo]))
    tesouro_escolhido = random.choice(list(dndata.tesouro_salas.items()))
    tesouro_nome, tesouro_info = tesouro_escolhido
    tesouro = it.Item(tesouro_nome, tesouro_info["efeito"], tesouro_info["usos"], tesouro_info["tipo"])

    return sl.Sala(tipo, aparencia, tesouro)

#Gera os inimigos automaticamente
def gera_inimigo(nome):
    nome = nome
    
    hp = dndata.inimigos_base[nome]["hp"]
    ep = dndata.inimigos_base[nome]["ep"]
    atk = dndata.inimigos_base[nome]["atk"]
    dfs = dndata.inimigos_base[nome]["dfs"]
    inte = dndata.inimigos_base[nome]["inte"]
    

    loot = random.choice(list(dndata.tesouro_inimigos.keys()))

    descricao_base = dndata.inimigos_base[nome]["descrição"]
    
    desc = f"{descricao_base}"

    return inm.Inimigo(nome, hp, ep, atk, dfs, inte, item, loot, desc)

#Lida com o combate por turnos
def combate(jogador, horda):
    while jogador.hp > 0 and any(inimigo.hp > 0 for inimigo in horda):

        print("\n==========COMBATE==========\n\n")

        # TURNO DO JOGADOR
        vivos = [inimigo for inimigo in horda if inimigo.hp > 0]

        print("\n=== Inimigos vivos ===")
        for i, inimigo in enumerate(vivos):
            print(f"{i + 1}. {inimigo.nome} (HP: {inimigo.hp}) | {inimigo.descricao}\n")

        # Escolher alvo
        while True:
            try:
                escolha = int(input("Escolha um inimigo para atacar:\n>> ")) - 1
                alvo = vivos[escolha]
                break
            except (ValueError, IndexError):
                print("Escolha inválida.")

        # Turno do jogador
        jg.turno_jogador(jogador, alvo)
        input("Pressione Enter para continuar!")
        # Verifica se todos os inimigos foram derrotados
        if all(inimigo.hp <= 0 for inimigo in horda):
            print("\n\t=====Todos os inimigos foram derrotados!=====\n")
            input("Pressione Enter para continuar!")
            break

        # TURNO DOS INIMIGOS
        for inimigo in horda:
            if inimigo.hp > 0:

                inm.turno_inimigo(inimigo, jogador)
                input("Pressione Enter para continuar!")
                if jogador.hp <= 0:
                    print(f"\n {jogador.nome} foi derrotado...")
                    return False  # derrota

    return True  # vitória


def escolher_alvo(inimigos):
    vivos = [i for i, inimigo in enumerate(inimigos) if inimigo.inimigo_vivo()]
    while True:
        try:
            print("Escolha o alvo:")
            for i in vivos:
                print(f"{i+1}. {inimigos[i].nome} - HP {inimigos[i].hp}")
            escolha = int(input("Número do alvo: ")) - 1
            if escolha in vivos:
                return inimigos[escolha]
            else:
                print("Inimigo inválido.")
        except ValueError:
            print("Entrada inválida.")

#Descreve as salas
def descreve_classe():
    for i, (classe, desc) in enumerate(dndata.descricoes_classes.items(), start=1):
        print("----------\n")
        print(f"{i}. {classe}: {desc}\n=>{dndata.classes[classe]}\n")

#Cria o menu principal
def menu_principal(x):
    print(f"==========Bem-vindo {x.user} à Masmorras e Visagens!==========\n\n")
    print("\t\t1.Começar a jogar!\n")
    print("\t\t2.Sair.\n")

# #loopings para fazer cadastro e login do usuário
cadastro = False
login = False

while not cadastro:
    limpar_terminal()
    print("\t\t==========Bem-vindo ao cadastro de Masmorras e Visagens!==========\n\n")
    user = input("Crie seu usuário!\n>>")
    email = input("Informe seu e-mail!\n>>")
    id = random.randint(1, 1000)
    senha = input("Crie sua senha!\n>>")

    if user in dndata.users.keys():
        input("Usuário já existe! Pressione Enter para tentar novamente!")
        continue
    elif any(info["email"] == email for info in dndata.users.values()):
        input("E-mail já existe! Pressione Enter para tentar novamente!")
        continue
    else:
        usuario = us.User(user, id, email, senha)
        usuario.registrar()
        input("Usuário cadastrado com sucesso! Pressione Enter para prosseguir para ir para tela de login")
        cadastro = True

while login == False:
    limpar_terminal()
    print("\t\t==========Bem-vindo!==========\n\n")
    print("=>Faça seu login para jogar!")

    login_user = input("Informe seu e-mail ou usuário\n>>")
    login_senha = input("Senha\n>>")

    for dados in dndata.users.values():
        if (login_user == dados["usuario"] or login_user == dados["email"]) and login_senha == dados["senha"]:
            print("Login realizado com sucesso!")
            login = True
            break
    else:
            print("Usuário ou senha incorretos.")
            input("Pressione Enter para tentar novamente!")

#Looping de criação de personagens
personagem_criado = False
while not personagem_criado:
    limpar_terminal()
    menu_principal(usuario)
    
    op = input("Digite o número da opção desejada!\n>>")
    if op == "1":
        limpar_terminal()
        print("\t\t==========Menu de criação de personagem==========\n\n")

        print("SELECIONE A SUA CLASSE:\n")

        descreve_classe()

        opcoes = {
        "1": "Guerreiro",
        "2": "Mago",
        "3": "Arqueiro"
        }

        escolha = input("Digite o número da classe desejada:\n>> ")

        if escolha in opcoes:
            nome_classe = opcoes[escolha]
            atributos = dndata.classes[nome_classe]

            # Atributos básicos
            vida = atributos["hp"]
            mana = atributos["ep"]
            ataque = atributos["atk"]
            defesa = atributos["dfs"]
            inteligencia = atributos["inte"]

            # Equipamento e habilidades

            habilidades_classe = [hb.Habilidade(**dados) for dados in dndata.habilidades[nome_classe]]

            arma_nome = dndata.armas_iniciais[nome_classe]["nome"]
            arma_efeito = dndata.armas_iniciais[nome_classe]["efeito"]
            arma_usos = dndata.armas_iniciais[nome_classe]["usos"]
            arma_tipo = dndata.armas_iniciais[nome_classe]["tipo"]
            arma_hab_primaria = habilidades_classe[0]
            arma_hab_secundaria = habilidades_classe[1]

            arma = ar.Arma(arma_nome, arma_efeito, arma_usos, arma_tipo, arma_hab_primaria, arma_hab_secundaria)
            item_escolhido = random.choice(list(dndata.tesouro_salas.items()))
            item_nome, item_info = item_escolhido
            item = it.Item(item_nome, item_info["efeito"], item_info["usos"], item_info["tipo"])

            nome_personagem = input(f"\nDigite o nome do seu personagem {nome_classe}:\n>> ")

            # Criação do objeto Jogador
            jogador = jg.Jogador(
                nome=nome_personagem,
                classe=nome_classe,
                hp=vida,
                ep=mana,
                atk=ataque,
                dfs=defesa,
                inte=inteligencia,
                arma=arma,
                item=item,
                habilidades = habilidades_classe
            )

            personagem_criado = True
            limpar_terminal()
            print("====== Personagem Criado ======\n")
            print(f"Nome: {jogador.nome}")
            print(f"Classe: {jogador.classe}")
            print(f"{jogador.mostra_atributos()}")
            print(f"Arma inicial: {jogador.arma.nome} (Efeito: {jogador.arma.efeito}, Tipo: {jogador.arma.tipo})")
            print(f"Item inicial: {jogador.item.nome} (Efeito: {jogador.item.efeito}, Usos: {jogador.item.usos})")
            print("Habilidades: \n")
            jogador.descreve_habilidades()

            input("\nPressione Enter para iniciar sua jornada...")
            
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
    elif op == "2":
            limpar_terminal()

            print("\t\t\n==========PROGRAMA FINALIZADO==========\n\n")
            break
    else:
        input("Opção inválida! Pressione Enter para tentar novamente")    

#looping de gameplay(gerar masmorra e salas, lidar com o jogador e inimigos)

masmorra = gera_masmorra()
lista_salas = gera_tipos_salas(masmorra.num_salas)
salas = [gera_sala(masmorra, tipo) for tipo in lista_salas]
index = 0
print("\n\n=====")
print(masmorra.narra_masmorra())

sala_final = None
for sala in salas:
    if sala.tipo == "chefe":
        sala_final = sala
        salas.remove(sala)
        break

for i, sala in enumerate(salas):
    index += 1
    print("\n----------")
    print(f"\nMasmorra {masmorra.nome}\nSala: {i+1}\nExplorador: {jogador.nome}\n\n")
    print("----------")

    print(sala.narra_sala(sala.tipo))
    print("Você adentra a sala misteriosa. O que deseja fazer?\n1.Investigar a sala.\n2.Gerenciar o equipamento.\n3.Seguir em frente.\n")
    opcao = input(">>")

    chance = sala.tem_loot()

    if opcao == "1" or opcao == "3":
        if sala.tem_inimigos():
                print("----------\n")
                print(f"Ao adentrar mais a sala você percebe uma movimentação estranha, como se o ambiente estivesse escurecendo, a luz das tochas se tornam mais fraca e o ar mais denso, sombras dançam pela sala. De repente, vultos aparecessem e você se vê cercado por figuras monstruosas. Enquanto algumas delas te observam e se aproximam, você se prepara para o combate.")
                num_onda = sala.calcula_encontros()        # retorna quantas ondas
                lista_nomes = sala.gera_hordas(num_onda)   # retorna nomes dos inimigos por onda
                hordas = []  # cada horda será uma lista de Inimigos reais

                for nomes in lista_nomes:
                    horda = [gera_inimigo(nome, masmorra) for nome in nomes]
                    hordas.append(horda)

                for i, horda in enumerate(hordas):
                    print(f"\n\n{i + 1}º Turno:")
                    resultado = combate(jogador, horda)
                    if not resultado:
                        jogador.hp = 0  
                        break
        elif chance:

            if True:

                    print("\n Você começa a vasculhar a sala em silêncio, atento a qualquer sinal fora do comum. Com passos calculados, toca cada fresta entre as pedras, sentindo desníveis sutis e escutando ecos estranhos ao pressionar certos pontos. Em meio às sombras tremeluzentes, seus olhos captam algo — uma discreta saliência, uma ranhura suspeita no chão, talvez, atrás daquela parede instável ou sob aquela laje solta, esteja exatamente o que você procura...")
                    
                    print(sala.revela_loot(chance))

                    jg.menu_item(jogador, sala)

    elif opcao == "2":
        print("\t\t==========VISUALIZANDO EQUIPAMENTO==========\n\n")
        print("----------")
        print(jogador.mostra_equipamento(jogador))
        print("----------")

    else:
        print("-> Opção inválida!")
        continue

    if jogador.hp <= 0:
        print(f"\n{jogador.nome} caiu em batalha...\n\t==========Game Over.==========")
        break
