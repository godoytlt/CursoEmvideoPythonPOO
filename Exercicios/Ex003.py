class ContaBancaria: 
    """
Cria uma conta bancária e permiote fazer saques e depósitos

    """
    def __init__(self, id, nome, saldo = 0): # Metodo de inicialização
        self.id = id
        self.titular = nome  
        self.saldo = saldo
        print(f"A conta número {self.id} foi criada com sucesso. Saldo atual R${self.saldo}")

    def __str__(self): #Dunder method utiliza o valor do objeto para ser referenciado.
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de valor de R${valor:,.2f} autorizado na conta {self.id}.")


    def sacar(self, valor):
        self.saldo -= valor
        if valor > self.saldo:
            print(f"Saque NEGADO de valor {valor:,.2f} na conta {self.saldo}: SALDO INSUFICIENTE")
        else:
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}.")

    
c1 = ContaBancaria(112,"Marcelo", 10000)
print(c1)
c1.depositar(500)
c1.sacar(2000)
print(c1)