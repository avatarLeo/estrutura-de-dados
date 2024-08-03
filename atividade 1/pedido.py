from pagamento import Pagamento


class Pedido:
    def __init__(self) -> None:
        self.itens = list()
        self.pagamento = Pagamento()


    def add_pedido(self, id):
        self.itens.append(id)

    def total(self, cardapio):
        valor_total = 0
        for id in self.itens:
            for item in cardapio:
                for k,  v in item.items():
                    if k == 'id' and v == id:
                        valor_total += item.get('valor')
        
        return valor_total
    
    def lista_de_pedidos(self, cardapio):
        for id in self.itens:
            for item in cardapio:
                for k,  v in item.items():
                    if k == 'id' and v == id:
                        print(f"{item.get('nome')} valor: {item.get('valor')}")

    def confirma_pedido(self, forma_de_pagamneto):
        self.pagamento.pagar(forma_de_pagamneto)


