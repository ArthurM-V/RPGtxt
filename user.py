import dungeon_dict as dndata

class User:
    def __init__(self, user, id, email, senha):
        self._user = user
        self._id = id
        self._email = email
        self._senha = senha

    @property
    def user(self):
        return self._user

    @property
    def id(self):
        return self._id

    @property
    def email(self):
        return self._email

    @property
    def senha(self):
        return self._senha

    def registrar(self):
        usuario = {
            self._user: {
                "usuario": self._user,
                "id": self._id,
                "email": self._email,
                "senha": self._senha
            }
        }
        dndata.users.update(usuario)
        return f"Usuário {self._user} registrado com sucesso."

    def exibirDados(self):
        return f"Usuário: {self._user}\nE-mail: {self._email}\nID: {self._id}"

    def checa_dados(self, entrada, senha):
        return (entrada == self._user or entrada == self._email) and senha == self._senha
