

class Lista:
    def __init__(self) -> None:
        self.primeiro = self.ultimo = None

    def add_cliente(self, cliente):
        

        while True:
            novo = cliente

            if self.primeiro == None:
                self.primeiro = novo
                self.ultimo = novo
            else:
                self.ultimo.defineProximo (novo)
                novo.defineAnterior (self.ultimo)
                self.ultimo = novo


            break

    def relatorio(self, cardapio):


        if self.primeiro != None:
    #impressão da lista de pedidos
            aux = self.primeiro
            print('Lista de clientes')
            print()
            while aux:
                total = 0
                print(f'Os pedidos de {aux.nome}')
                print()
                for n, pedidos in enumerate(aux.pedido):
                    print(f'{n+1}º pedido')
                    pedidos.lista_de_pedidos(cardapio)
                    print()
                    match pedidos.pagamento.forma_pagamento:
                        case 1:
                            print('forma de pagamento Pix')
                        case 2:
                            print('forma de pagamento Dinheiro')
                        case 3:
                            print('forma de pagamento Credito')
                        case 4:
                            print('forma de pagamento Debito')
                    total += pedidos.total(cardapio)
                    print(f'Total deste pedido: {pedidos.total(cardapio)}')
                    print(f'Endereço: {aux.endereco}')
                    print()
                print(f'Valor total de todos os pedidos: {total}')
                print()
                aux = aux.retornaProximo()

    def reverse_relatorio(self):

            print()
            aux = self.ultimo
            print('Lista de pedidos (Z -> A)')

            while aux:
                print(f'{aux}', end='<=>')
                for pedidos in aux.pedido:
                    pedidos.lista_de_pedidos()
                aux = aux.retornaAnterior()

    def buscar_cliente(self, nome):
        if self.primeiro != None:
            aux = self.primeiro
            while aux:
                if aux.nome == nome:
                    return aux
                aux = aux.retornaProximo()


