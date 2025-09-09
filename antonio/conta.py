class Conta:
    def __init__(self,agencia, tipo_da_conta, numero_da_conta, saldo, pessoa):
        self.agencia = agencia
        self.tipo_da_conta = tipo_da_conta
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo
        self.pessoa = pessoa
        
        
    def exibir_dados_da_conta(self):
        print(f'a conta bancaria de agencia {self.agencia} de seu tipo de conta {self.tipo_da_conta} e numero de conta {self.numero_da_conta} tem seu saldo{self.saldo}')    

    def exibir_saldo(self):
        print(f'{self.saldo}')
        
    def exibir_dados_pessoais(self):
       self.pessoa.dados_pessoais()