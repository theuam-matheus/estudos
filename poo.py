class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."    
        
#objetos
pessoa1 = Pessoa ("Alice", 30)
mensagem = pessoa1.sudacao()
print(mensagem)

pessoa2 = Pessoa ("Rodrigo", 32)
mensagem = pessoa2.sudacao()
print(mensagem)