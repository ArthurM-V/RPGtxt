class Habilidade:
    def __init__(self, num, nome, descricao, tipo, efeito, custo):
        self.num = num
        self.nome = nome
        self.descricao = descricao
        self.custo = custo
        self.tipo = tipo
        self.efeito = efeito
         
    def usar_habilidade(self, atacante, alvo):
        if atacante.ep < self.custo:
            return f"{atacante.nome} não tem EP suficiente para usar {self.nome}."

        atacante.ep -= self.custo

        atributo = max(atacante.atk, atacante.inte)
        dano = self.efeito + int(atributo * 3)
        dano_final = max(0, dano - alvo.dfs)

        alvo.hp -= dano_final

        return (
            f"{atacante.nome} usou {self.nome} e causou {dano_final} de dano "
            f"a {alvo.nome}! EP restante: {atacante.ep}"
        )
