
#elemento.py
class Elemento:
    
    def __init__(self, valor, anterior=None, proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

    def __str__(self):
        return self.valor
    
    def retornaAnterior (self):
        return self.anterior
    
    def retornaProximo (self):
        return self.proximo
    
    def defineAnterior (self, novoAnterior):
        self.anterior = novoAnterior

    def defineProximo (self, novoProximo):
        self.proximo = novoProximo
