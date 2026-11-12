# Crie a classe funcionário, onde podemos cadastrar nome, sertor e cargo.
# Crie também um método que permita ao funcionário se apresentar.
from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo, empresa = "Curso em Vídeo"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def apresentacao(self):
        return f":waving_hand: Olá! Meu nome é {self.nome}, sou {self.cargo} no setor de {self.setor} da empresa {self.empresa}"

c1 = Funcionario("Marcelo", "TI", "Estagiário")
print(c1.apresentacao())

c2 = Funcionario("Vanessa", "TI", "Coordenadora", "Jaguar Land Rover")
print(c2.apresentacao())