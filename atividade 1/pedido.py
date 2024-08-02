class Pedido:
    def __init__(self) -> None:
        self.itens = list()


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
