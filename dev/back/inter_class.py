class Pessoa: 
    def __init__(self, nome, endereco, telefone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf
    
    def logado():
        print ("Logado com sucesso!")
    def falar():
        print ("Oi, tudo bem?")


class Aluno (Pessoa):
    def __init__(self, nome, endereco, telefone, cpf):
        super().__init__( nome, endereco, telefone, cpf) 
        self.matricula= "Teste_2024"
    pass

class Professor (Pessoa):

    def __init__(self, nome, endereco, telefone, cpf):
        super().__init__( nome, endereco, telefone, cpf) 
        self.funcao= "Docente"
    pass