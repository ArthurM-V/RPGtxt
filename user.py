import dungeon_dict as dndata

class User:
    def __init__(self, user, id, email, senha):
        self.user = user
        self.id = id
        self.email = email
        self.senha = senha

    def registrar(self):
        
        usuario = {self.user : {"usuario" : self.user, "id" : self.id, "email" : self.email, "senha" : self.senha}}
        dndata.users.update(usuario)

        return (f"Usuário {self.user} registrado com sucesso.")

    def exibirDados(self):
        return f"Usuário: {self.user}\nE-mail: {self.email}\nID: {self.id}"
    
    def checa_dados(self, x, y):
        if (x == self.user or x == self.email) and y == self.senha:
            correto = True
            return correto
        else:
            correto = False
            return correto