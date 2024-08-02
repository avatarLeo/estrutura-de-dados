

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

    def relatorio(self):


        if self.primeiro != None:
    #impressão da lista de pedidos
            aux = self.primeiro
            print('Lista de clientes')
            while aux:
                print(f'{aux}')
                aux = aux.retornaProximo()

    def reverse_relatorio(self):

            print()
            aux = self.ultimo
            print('Lista de pedidos (Z -> A)')

            while aux:
                print(f'{aux}', end='<=>')
                aux = aux.retornaAnterior()