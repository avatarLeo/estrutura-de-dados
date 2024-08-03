# ix, Dinheiro, Crédito ou Débito
PIX = 1
DINHEIRO = 2
CREDITO = 3
DEBITO = 4



class Pagamento:
    def __init__(self) -> None:
        self.valor = 0
        self.estado = False
        self.forma_pagamento = int()

    def relatorio(self):
        ...

    def pagar(self, forma):
        self.estado = True
        self.forma_pagamento = forma
        
    def checar_pagameto(self):
        return self.estado, self.estado