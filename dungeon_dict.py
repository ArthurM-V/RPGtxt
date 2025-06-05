#Dados de masmorras
nomes_masmorras = {
    "dungeon": ["Goudenn", "Endgoun", "Dunegon"],
    "crypt": ["Ptryc", "Tycrp", "Crytp"],
    "vault": ["Altuv", "Tavul", "Lutva"],
    "fortress": ["Frossert", "Resforts", "Torserfs"],
    "tomb": ["Motb", "Btmo", "Tmob"],
    "abyss": ["Sybsa", "Bysas", "Ssyab"],
    "ruins": ["Srinus", "Nisru", "Rusin"]
}


ambiente = {
    "subterrâneo": [
        "Escondida nas profundezas da terra, entre rochas e raízes antigas",
        "Imersa na escuridão total, onde o silêncio é tão denso quanto a pedra",
        "Perdida em túneis cavados por criaturas esquecidas"
    ],

    "ruínas": [
        "Entre colunas tombadas e vestígios de uma era esquecida",
        "Coberta de musgo e estilhaços de uma cidade outrora gloriosa",
        "Com as paredes tomadas por heras e inscrições antigas"
    ],

    "floresta": [
        "Oculta sob a copa densa da mata, onde a luz mal alcança",
        "Protegida por árvores retorcidas e raízes vivas",
        "Entre sons distantes e olhos que espreitam entre os galhos"
    ],

    "montanha": [
        "Cravada em um penhasco íngreme, desafiando os ventos gelados",
        "Esculpida na pedra por mãos ancestrais, isolada do mundo",
        "Escondida entre desfiladeiros onde só águias ousam voar"
    ],

    "céu": [
        "Flutuando entre nuvens etéreas, onde o horizonte toca o firmamento",
        "Em meio a correntes de ar que sussurram antigos encantamentos",
        "Suspensa no azul infinito, além do alcance dos olhos mortais"
    ],

    "lago": [
        "No fundo de um lago sereno, guardado por criaturas silenciosas",
        "Submersa entre algas e colunas corroídas pela água",
        "Oculta sob o espelho d’água que esconde mais do que reflete"
    ],

    "etéreo": [
        "Flutuando entre fragmentos de realidade quebrada",
        "Em um espaço que dobra e gira ao redor de si mesmo",
        "Num vácuo entre dimensões, onde as cores não seguem lógica alguma"
    ]
}

origem = {
        "templo": ["um templo profanado, onde orações viraram gritos",
                   "um templo dos ventos, onde monges desafiaram os deuses",
                   "um templo submerso dedicado a uma deusa esquecida das profundezas"],

        "covil": ["um abrigo escavado por garras famintas, marcado por ossadas recentes",
                  "uma toca escura onde apenas o som de ossos quebrando ecoa",
                  "um buraco sombrio onde cada pedra guarda o eco de gritos passados"],

        "laboratório": ["um laboratório abandonado, com frascos estilhaçados e fórmulas ilegíveis",
                        "uma oficina arcana, onde o conhecimento enlouqueceu o criador",
                        "um centro de experiências proibidas, agora tomado pelo caos"],

        "prisão": ["uma prisão onde os guardas se foram, mas os gritos ficaram",
                   "um castelo antigo esculpido em pedra, destinado a algo que nunca devia ser solto",
                   "um corredor vazio onde o tempo parou e as correntes ainda ecoam memórias"],

        "santuario" : ["um santuário perdido, tomado por forças opostas ao que foi venerado",
                       "um santuário flutuante erguido para tocar os planos celestes", 
                       "um altar antigo, hoje palco de rituais proibidos"]
}

perigo = {
        "fogo": ["paredes chamuscadas e brasas vivas ameaçam cada passo",
                 "o ar é denso de fuligem, e as chamas dançam com vida própria",
                 "tudo cheira a cinzas e carvão, como se tivesse acabado de arder"],

        "gelo": ["o chão escorregadio range sob os pés, coberto por gelo eterno",
                 "estalactites pontiagudas pingam lentamente, como relógios mortais",
                 "o frio corta como lâminas e congela até o silêncio"],

        "maldição": ["sussurros percorrem as paredes, dizendo nomes que você não lembra ter dito",
                     "um peso invisível oprime o peito, como se algo te visse de dentro das sombras",
                     "a realidade parece distorcida, como se o tempo estivesse preso ali"],

        "veneno": ["espinhos brotam das paredes, e o ar tem um leve gosto metálico",
                   "a atmosfera é espessa e oleosa, como um pântano em decomposição",
                   "líquidos verdes gotejam do teto, queimando lentamente onde tocam"],

        "água": ["o piso está sempre alagado, e algo se move sob a superfície",
                 "quedas d’água escondem passagens — e armadilhas",
                 "paredes úmidas ecoam com o som constante de goteiras e redemoinhos"]
}
entradas = {
    "Cripta de Ferro": [
        "descer por um poço selado com runas antigas",
        "remover uma estátua de ferro que cobre uma escada espiral",
        "encontrar uma porta escondida sob os escombros de uma capela abandonada"
    ],
    "Templo do Eclipse": [
        "entrar por um arco que só aparece à meia-noite",
        "seguir a sombra da lua até uma fenda entre pedras",
        "tocar um obelisco durante o eclipse solar"
    ],
    "Raiz do Mundo Velho": [
        "descer por uma fenda coberta de raízes petrificadas, entre musgos que respiram silêncio",
        "atravessar uma ponte de galhos entrelaçados que se forma apenas sob a lua nova",
        "derramar sangue sobre um altar de pedra viva, onde inscrições esquecidas brotam das rachaduras"
    ],
    "Mina da Névoa": [
        "caminhar por uma trilha que desaparece atrás de você",
        "seguir os sussurros na névoa até um buraco oculto",
        "ativar um antigo guindaste de madeira que desce no vazio"
    ],
    "Cidadela Celeste": [
        "subir por uma cachoeira reversa ao entoar um canto ancestral",
        "escalar uma árvore que toca o céu ao pôr do sol",
        "voar nas costas de um pássaro gigante que adormece nas nuvens"
    ],
    "Abismo Escondido do Lago": [
        "caminhar sobre uma ponte de gelo fino que surge ao anoitecer",
        "ser tragado por um peixe-gato dourado e acordar no templo submerso",
        "ganhar a confiança de um jacaré albino que revela uma passagem"
    ],
    "Cubo das Dimensões Partidas": [
        "entrar em uma sala flutuante que aparece ao amanhecer",
        "usar um espelho rachado para ativar um portal interdimensional",
        "arremessar um gancho em uma das faces flutuantes e ser içado"
    ]
}

#Dados de salas
tipo_salas = {
    "vazia": [
        "Uma câmara silenciosa, ecoando apenas os próprios passos",
        "Um salão amplo, sem nada além do eco dos próprios passos",
        "Uma câmara vazia, iluminada apenas por uma luz difusa que filtra do teto",
        "Um espaço amplo e silencioso, onde o tempo parece suspenso",
        "Um salão amplo, sem sinais recentes de presença",
        "Uma sala esquecida, tomada pelo tempo e pelo pó"
    ],
    "loot": [
        "No centro da sala, algo chama atenção imediatamente",
        "Uma estrutura antiga domina o espaço, cercada por sombras",
        "No coração do aposento, uma peça singular atrai o olhar",
        "Um artefato isolado repousa sob uma iluminação tênue",
        "Algo repousa no meio do salão, desafiando a curiosidade",
        "Um objeto antigo ocupa o coração da sala, intacto"
    ],
    "celas": [
        "Grades retorcidas cercam partes da sala",
        "Corredores flanqueados por gaiolas vazias e paredes ásperas",
        "Barreiras de ferro separam compartimentos estreitos e escuros",
        "Várias celas alinham-se às paredes, cada uma com portas enferrujadas",
        "As celas parecem ter sido esvaziadas há muito tempo",
        "Correntes ainda pendem das paredes e do teto"
    ],
    "central" : ["Uma escultura animada parece observar quem entra, embora não se mova",
                 "Um círculo de pedras negras pulsa com uma energia baixa, como um coração adormecido",
                 "Uma chama imóvel flutua sobre um pedestal, sem emitir calor nem consumir combustível",
                 "No meio da sala, um espelho antigo de moldura ornamentada reflete algo diferente da realidade ao redor",
                 "Uma árvore retorcida de cristal se ergue do chão, irradiando uma luz tênue e pulsante",
                 "Uma fonte silenciosa jorra água cristalina no centro, quebrando o silêncio com seu som constante"
                 ],
    "guardião": [
    "Um espaço amplo e ovalado, com pilares quebrados formando um círculo imperfeito",
    "O chão rachado e afundado no centro da sala revela marcas de antigos confrontos",
    "Paredes marcadas por impactos e arranhões, como se algo tentasse escapar dali",
    "Trilhos de sangue seco serpenteiam até o centro, onde pedras negras formam um pequeno altar",
    "Uma iluminação incomum parece se concentrar no centro, onde o ar vibra sutilmente",
    "Restos de armaduras e armas partidas estão espalhados, sinalizando batalhas anteriores"
],
    "chefe": [
        "A arquitetura aqui é grandiosa, feita para impressionar ou intimidar",
        "No coração do espaço, um altar improvisado serve de palco para a batalha",
        "Sombras densas formam um círculo onde um inimigo espera silencioso",
        "Um trono vazio observa o recinto, sinal de uma presença que reina ali",
        "Tudo nesta sala converge para uma única plataforma central",
        "Insígnias e relevos indicam que esta sala era destinada a alguém importante"
    ]
}

aparencia_sala = {
    "templo": [
        "pilares adornados com símbolos religiosos corroídos pelo tempo",
        "altares rachados e tapeçarias desbotadas decoram as paredes",
        "localizações cuidadosamente esculpidas que hoje exibem apenas o esquecimento",
        "as paredes marcadas por cavidades profundas, decorativas ou simbólicas",
        "estruturas simétricas em arco seguem o contorno das paredes laterais",
        "detalhes geométricos vazados criam sombras dançantes sob qualquer luz"
    ],
    "covil": [
        "paredes irregulares com marcas de garras e túneis colapsados",
        "rachaduras e sulcos profundos percorrem as paredes como cicatrizes",
        "chão de terra batida e ossos espalhados por toda parte",
        "poeira e cascalhos cobrem um chão marcado por pegadas deformadas",
        "túneis estreitos e escuros, com rochas soltas pelo chão"
    ],
    "laboratório": [
        "estantes quebradas com frascos antigos e equipamentos enferrujados",
        "suportes de madeira podre exibem vidros estilhaçados e peças oxidadas",
        "paredes de pedra lisa com marcas de fórmulas e diagramas apagados",
        "parede esculpida com inscrições efêmeras, agora quase invisíveis",
        "ares de abandono e experimentos interrompidos no meio",
        "o vazio carrega a sensação de um trabalho interrompido e jamais retomado"
    ],
    "prisão": [
        "paredes cobertas por inscrições de prisioneiros antigos",
        "grafites toscos gravados em silêncio nas paredes frias",
        "grades reforçadas e corredores estreitos marcados pelo tempo",
        "caminhos confinados entre barras gastas e ferrugem persistente",
        "trilhos de ferro e trancas grandes ainda fixadas nas portas",
        "fechos maciços permanecem firmes em portões que raramente se abrem"
    ],
    "santuario": [
        "estátuas cobertas de musgo vigiam silenciosamente os cantos",
        "monumentos ruinosos cobertos por trepadeiras silenciosas",
        "arquitetura imponente, mesmo que em ruínas",
        "colunas partidas sustentam vestígios de uma grandeza perdida",
        "bancos partidos e vitrais despedaçados espalham luzes distorcidas",
        "restos de mobília abandonada se misturam à luz filtrada pelas janelas"
    ]
}
#limita quantas salas podem existir em uma masmorra
limites_tipos = {
    "vazia": (1, 3),      
    "loot": (1, 1),
    "central": (1, 1),
    "celas": (0, 2),
    "guardião": (1, 1),    
    "chefe": (1, 1) 
}


#dados de itens
tesouro_salas = {

   "maçã": {
        "efeito": 8,
        "usos": 1,
        "tipo": "hp"
    },
    "talismã": {
        "efeito": 12,
        "usos": 1,
        "tipo": "ep"
    },
    "ervas secas": {
        "efeito": 12,
        "usos": 1,
        "tipo": "hp"
    },
    "pedaço de cristal bruto": {
        "efeito": 8,
        "usos": 1,
        "tipo": "ep"
    },
    "pedra de defesa": {
        "efeito": 1,
        "usos": 2,
        "tipo": "dfs"
    },
    "amuletinho rachado": {
        "efeito": 1,
        "usos": 1,
        "tipo": "atk"
    },
    "chá reconfortante": {
        "efeito": 12,
        "usos": 1,
        "tipo": "cura" 
    },
    "fruta amarga": {
        "efeito": 1,
        "usos": 1,
        "tipo": "inte"
    }
}

tesouro_inimigos = {
    "poção de ossos rígidos": {
        "efeito": 2,
        "usos": 1,
        "tipo": "dfs"  
    },

    "elixir de essência etérea": {
        "efeito": 2,
        "usos": 1,
        "tipo": "inte"  
    },
    "poção da força implacável": {
        "efeito": 2,
        "usos": 1,
        "tipo": "atk"  
    },
    "elixir vital supremo": {
        "efeito": 15,
        "usos": 1,
        "tipo": "hp"  
    },
    "poção arcana suprema": {
        "efeito": 15,
        "usos": 1,
        "tipo": "ep"  
    }
}

#dados de classes do usuário
classes = {

    "Guerreiro" : {"hp" : 75, "ep" : 12, "atk" : 2, "dfs" : 2, "inte" : 0},
    "Mago" : {"hp" : 60, "ep" : 20, "atk" : 0, "dfs" : 1, "inte" : 3},
    "Arqueiro" : {"hp" : 70, "ep" : 15, "atk" : 3, "dfs" : 0, "inte" : 1}

}

descricoes_classes = {
    "Guerreiro": (
        "Mestre do combate corpo a corpo, o Guerreiro confia em sua força bruta e resistência para dominar o campo de batalha. Usa armaduras pesadas e espadas afiadas para esmagar seus inimigos com precisão e brutalidade."
    ),
    "Mago": (
        "Portador de vasto conhecimento arcano, o Mago manipula as forças ocultas do mundo com maestria. Frágil em combate direto, mas devastador à distância, canaliza seu poder através de cajados encantadoe feitiços destrutivos."
    ),
    "Arqueiro": (
        "Silencioso, ágil e letal, o Arqueiro é um caçador nato. Usa sua destreza para atingir alvos à distância antes que possam reagir. Prefere manter-se em movimento, evitando ataques diretos e eliminando o inimigo com precisão cirúrgica."
    )
}

armas_iniciais = {
    "Guerreiro": {
        "nome": "Espada Curta",
        "efeito": 2,
        "usos": -1,
        "tipo": "atk"
    },
    "Mago": {
        "nome": "Cajado de Carvalho",
        "efeito": 2,
        "usos": -1,
        "tipo": "inte"
    },
    "Arqueiro": {
        "nome": "Arco Simples",
        "efeito": 2,
        "usos": -1,
        "tipo": "atk"
    }
}

habilidades = {
    "Guerreiro": [
        {   
            "num" : 1,
            "nome": "Investida Brutal",
            "descricao": "Um golpe corpo a corpo que quebra defesas inimigas.",
            "tipo": "atk",
            "efeito": 5,
            "custo": 3
        },
        {   
            "num" : 2,
            "nome": "Postura Defensiva",
            "descricao": "Aumenta sua defesa consideravelmente por 1 turno.",
            "tipo": "dfs",
            "efeito": 4,
            "custo": 2
        }
    ],

    "Mago": [
        {
            "num" : 1,
            "nome": "Bola de Fogo",
            "descricao": "Lança uma esfera flamejante que explode em contato com inimigos.",
            "tipo": "inte",
            "efeito": 5,
            "custo": 5
        },
        {
            "num" : 2,
            "nome": "Míssil arcano",
            "descricao": "Lança um projeto feito de energia pura.",
            "tipo": "inte",
            "efeito": 3,
            "custo": 3
        }
    ],
    "Arqueiro": [
        {
            "num" : 1,
            "nome": "Flecha Perfurante",
            "descricao": "Dispara uma flecha precisa que ignora parte da defesa inimiga.",
            "tipo": "atk",
            "efeito": 4,
            "custo": 2
        },
        {
            "num" : 2,
            "nome": "Retirada Rápida",
            "descricao": "Atira 3 flechas rapidamente.",
            "tipo": "inte",
            "efeito": 5,
            "custo": 4
        }
    ]
}
#inimigos
inimigos_base = {
    "esqueleto": {
        "hp": 10,
        "ep" : 0,
        "atk": 2,
        "dfs": 1,
        "inte" : 2,
        "descrição": 
            "Ossos flutuam em um líquido que dá forma humanoide incompleta, com partes faltando, movendo-se de forma estranha."
        
    },
    "duende": {
        "hp": 12,
        "ep" : 0,
        "atk": 3,
        "dfs": 0,
        "inte" : 4,
        "descrição": 
            "Criaturas pequenas e ágeis, com pele esverdeada e orelhas pontudas, muito habilidosas em emboscadas e travessuras."
        
    },
    "espectro": {
        "hp": 9,
        "ep" : 14,
        "atk": 4,
        "dfs": 1,
        "inte" : 5,
        "descrição": 
            "Espírito disforme, vagamente humanoide, parecendo ter apenas uma perna, que se move silenciosamente pela masmorra."
        
    },
    "armadura viva": {
    "hp": 15,
    "ep" : 14,
    "atk": 5,
    "dfs": 4,
    "inte" : 0,
    "descrição": "Peças de armadura que se movem sozinhas, unidas por uma força invisível e maligna."
    }
}

#Guarda os usuários
users = {
    "rodolfo" : {"usuario" : "rodolfo", "email" : "email123@gmail.com", "senha" : "12345"}
}