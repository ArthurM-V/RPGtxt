class Masmorra:
    
    def __init__(self, nome, tipo, origem, ambiente, perigo, entrada, num_salas):
        self.nome = nome
        self.tipo = tipo
        self.origem = origem
        self.ambiente = ambiente
        self.perigo = perigo
        self.entrada = entrada
        self.num_salas = num_salas      
    
    def narra_masmorra(self):
        return f"{self.ambiente}, se esconde {self.origem}, {self.perigo}. Ao se aproximar mais da masmorra, você entende, a entrada é revelada ao {self.entrada}. Ao adentrar a construção, você percebe uma fina membrana se formando na entrada por onde veio. Em silêncio, você observa enquanto ela se solidifica lentamente, transformando-se em uma porta que bloqueia qualquer caminho de volta. Assim, você continua seu caminho até o coração da masmorra, se preparando para os perigos que encontrará."
    
    def exibe_dados(self):
        return f"Nome: {self.nome}\nTipo: {self.origem}\nAmbiente: {self.ambiente}\nPerigo: {self.perigo}\nNúmero de salas: {self.num_salas}"
