class ContaBancaria:
    def __init__(self, titular, saldo=0, senha="1234"):
        self.titular = titular
        self.saldo = saldo
        self.senha = senha

    def verificar_senha(self, senha):
        if self.senha == senha:
            return True
        else:
            print("Senha incorreta!")
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor, senha):
        if not self.verificar_senha(senha):
            return
        if valor > self.saldo:
            print("Saldo insuficiente!")
        elif valor > 0:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def transferir(self, valor, outra_conta, senha):
        if not self.verificar_senha(senha):
            return
        if valor > self.saldo:
            print("Transferência falhou: saldo insuficiente!")
        elif valor > 0:
            self.saldo -= valor
            outra_conta.saldo += valor
            print(f"Transferência de R${valor:.2f} realizada com sucesso para {outra_conta.titular}!")
        else:
            print("O valor da transferência deve ser positivo.")



conta1 = ContaBancaria("João Silva", 1000, senha="abcd")
conta2 = ContaBancaria("Maria Souza", 500, senha="1234")

# Testando operações com senha correta e incorreta
conta1.sacar(100, senha="abcd")  
conta1.sacar(100, senha="1234")  
conta1.transferir(200, conta2, senha="abcd") 
conta1.transferir(200, conta2, senha="1234")  
