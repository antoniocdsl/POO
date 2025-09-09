class Pessoa:
    def __init__(self,nome_completo, cpf, email, telefone):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
    
    def dados_pessoais(self):
        print(f'{self.nome_completo}, {self.cpf}, {self.email}, {self.telefone}')    