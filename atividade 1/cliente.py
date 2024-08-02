class Cliente:
    def __init__(self, nome:str, endere:str, anterior=None, proximo=None) -> None:
        self.nome = nome
        self.endereco = endere
        self.pedido = None


        self.anterior = anterior
        self.proximo = proximo


    def __str__(self):
        return self.nome
    
    def retornaAnterior (self):
        return self.anterior
    
    def retornaProximo (self):
        return self.proximo
    
    def defineAnterior (self, novoAnterior):
        self.anterior = novoAnterior

    def defineProximo (self, novoProximo):
        self.proximo = novoProximo