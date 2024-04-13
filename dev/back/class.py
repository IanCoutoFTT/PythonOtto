#criando class e colocando conteudo
class Pessoas:
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("Fala muito!")

pessoa1 = Pessoas("Pedrin", 52)

print(pessoa1.nome)
print(pessoa1.idade)

print(pessoa1.falar())