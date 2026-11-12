# Crie a classe Churrasco, onde seja possivel informar quantas pessoas vão participar e mostre quanto de carne dever ser comprado,
# o custo total do churrasco e o preço por pessoa
from rich import print
from rich.panel import Panel
from rich.console  import Group
from rich.text import Text

class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.pessoas = quantidade

    def analisar(self):
        consumo = self.pessoas * 0.4
        preco = 82.4
        total = consumo * preco
        preco_por_pessoa = preco * 0.4

        titulo_txt = Text.from_markup(f"Analisando o [yellow]{self.titulo}[/] com [blue]{self.pessoas}[/] convidados",style="white")
        txt = Text.from_markup("Considerando o valor de 0,4 kg de carne por participante e preço de R$82,40/Kg",style="white")
        consumo_txt = Text.from_markup(f"É recomendado comprar [blue]{consumo:.1f}Kg[/] de carne",style="white")
        preco_txt = Text.from_markup(f"O Custo total será de [red]R${total:.2f}[/]",style="white")
        por_pessoa_txt = Text.from_markup(f"Cada pessoa pagará [red]R${preco_por_pessoa:.2f}[/].",style="white")
        conteudo = Group(titulo_txt, txt, consumo_txt, preco_txt, por_pessoa_txt)
        
        etiqueta = Panel(conteudo, title=self.titulo,style="green", width=70)
        return etiqueta
    
c1 = Churrasco("Churrasco dos Boroca", 4)
print(c1.analisar())
        