## Como melhorar a classe da aula anterior?
```python
# Declaração de classe
class Gafanhoto:
# Como documentar uma classe?
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade
    Para criar uma nova pessoa use:
    variavel = Gafanhoto(nome,idade)

    """
    def __init__(self, nome = "vazio" , idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome         
        self.idade = idade
    # Métodos de instância
    def aniversario(self):
        self.idade += 1
    
    def __str__(self): # Dunder Method
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
    
# Declaração de objetos
g1 = Gafanhoto("Marcelo", 26)
g1.aniversario()
# print(g1)
# print(g1.__doc__) # Dunder Attribute

# Como obter o estado de um objeto?
print(g1.__dict__) # Attibute
print(g1.__getstate__()) # Method
# Como descobrir a classe de um objeto?
print(g1.__class__) # Dunder attribute

``` 
# Me mostra um exemplo mais útil?
EX003