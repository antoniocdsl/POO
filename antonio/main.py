from conta import Conta
from pessoa import Pessoa

cliente = Pessoa('antonio carlos', '123.456.789-10', 't.s@teste.com', 819 70055100)

conta = Conta('3144', 'poupança', '77', 300, cliente )

conta.exibir_dados_da_conta()
conta.exibir_dados_pessoais()
conta.exibir_saldo()