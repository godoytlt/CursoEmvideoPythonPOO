# Crie uma classe Produto, onde podemos cadastrar nome e preço. Crie também um método que mostre uma etiqueta de preço do produto
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich.console import Group

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        txt_nome = Text(self.nome, justify="center", style = "bold green")
        linha = Rule(style="white")
        txt_preco = Text(f"R${self.preco}", justify="center",style="bold yellow")
        conteudo = Group(linha,txt_nome, linha, txt_preco, linha)
        etiqueta = Panel(conteudo, title = "Produtos", style = "green", width=30)
        return etiqueta
    
p1 = Produto("Mouse Gamer", "249,99")
print(p1.etiqueta())
p2 = Produto("Geladeira", "3000,00")
print(p2.etiqueta())