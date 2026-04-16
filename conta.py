class ContaBancaria: 
    #construtor da classe
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado.')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return valor
            print(f'Saque de R${valor} realizado.')
        else:
            print('Saldo insuficente para realizar o saque.')

    def exibir(self):
        print(f'Titular: {self.titular}, Saldo: R${self.saldo}')


