
class Conta:

    def __init__(self, titular, saldo=0):
        self.saldo = saldo
        self.titular = titular
        self.extrato = []

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo-= valor
            self.extrato.append('Saque de: '+ valor)
        else:
            print('Você não tem saldo suficiente para fazer este saque')

    def deposito(self, valor):
        if valor > 0:
            self.saldo+= valor
            # saida=
            self.extrato.append('Deposito de: '+ str(valor)+ ' realizado com sucesso')
        else:
            print('Valor inválido para depósito')

    def transferencia(self, destinatario, valor):
        if self.saldo >= valor and valor > 0:
            self.saldo-=valor
            destinatario.deposito(valor)
            self.extrato.append('Transferência de: '+ str(valor)+ ' para '+ destinatario.titular)
        elif self.valor < valor:
            print('Saldo insuficiente para realizar esta transferencia')
        else:
            print('Valor inválido')

    def verificar_extrato(self):
        print('Extrato do', self.titular)

        for transacao in self.extrato:
            print(transacao)
        
        print('Saldo atual: ', self.saldo)






conta1 = Conta('Renan', 250)

conta2 = Conta('Procopio')

conta2.deposito(500)

conta1.transferencia(conta2, 150)

conta1.verificar_extrato()