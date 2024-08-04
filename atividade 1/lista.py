PIX = 1
DINHEIRO = 2
CREDITO = 3
DEBITO = 4

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
            print('|===========================================|')
            print('| Relatorio                                 |') 
            print('|===========================================|')
            print() 
            valor_total_de_todos_os_pedidos = 0
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
                valor_total_de_todos_os_pedidos += total
                print(f'Valor total deste cliente: R$ {total}')
                print()
                print(f'Valor total de todos os pedidos {valor_total_de_todos_os_pedidos}')
                print()
                aux = aux.retornaProximo()
            input('Enter para continuar...')

    def reverse_relatorio(self, cardapio):

            print()
            aux = self.ultimo
            print('|===========================================|')
            print('| Relatorio do ultimo ao primeiro           |') 
            print('|===========================================|')
            print()
            valor_total_de_todos_os_pedidos = 0
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
                valor_total_de_todos_os_pedidos += total
                print(f'Valor total deste cliente: R$ {total}')
                print()
                print(f'Valor total de todos os pedidos {valor_total_de_todos_os_pedidos}')
                print()
                aux = aux.retornaAnterior()
            input('Enter para continuar...')

    def buscar_cliente(self, nome):
        if self.primeiro != None:
            aux = self.primeiro
            while aux:
                if aux.nome == nome:
                    return aux
                aux = aux.retornaProximo()

    def relatorio_por_pagamento_dinheiro(self, cardapio):
        if self.primeiro != None:
            aux = self.primeiro
            print('|===========================================|')
            print('| Relatorio por Dinheiro                    |') 
            print('|===========================================|')
            print()
            total_de_todos_os_pedidos = 0
            while aux:
                total = 0
                for n, pedidos in enumerate(aux.pedido):
                    pagamento, _ = pedidos.forma_de_pagamento()
                    if pagamento == DINHEIRO:
                        if n == 0:
                            print(f'Os pedidos de {aux.nome}')
                        print()
                        print(f'O {n+1}° de {aux.nome}')
                        print()
                        pedidos.lista_de_pedidos(cardapio)
                        print(f'O total deste pedido R$ {pedidos.total(cardapio)}')
                        total += pedidos.total(cardapio)
                        if len(aux.pedido) == n + 1:    
                            print(f'Valor total dos pedidos de {aux.nome} R$ {total}')
                            print()

                aux = aux.retornaProximo()
                total_de_todos_os_pedidos += total
            
            print('|===========================================|')
            print('| Total de todos os pedidos por Dinheiro    |') 
            print('|===========================================|')
            print(f'R$ {total_de_todos_os_pedidos}')
            input('Enter para continuar...')


    def relatorio_por_pagamento_debito(self, cardapio):
        if self.primeiro != None:
            aux = self.primeiro
            print('|===========================================|')
            print('| Relatorio por Débito                      |') 
            print('|===========================================|')
            print()
            total_de_todos_os_pedidos = 0
            while aux:
                total = 0
                for n, pedidos in enumerate(aux.pedido):
                    pagamento, _ = pedidos.forma_de_pagamento()
                    if pagamento == DEBITO:
                        if n == 0:
                            print(f'Os pedidos de {aux.nome}')
                        print()
                        print(f'O {n+1}° de {aux.nome}')
                        print()
                        pedidos.lista_de_pedidos(cardapio)
                        print(f'O total deste pedido R$ {pedidos.total(cardapio)}')
                        total += pedidos.total(cardapio)
                        if len(aux.pedido) == n + 1:    
                            print(f'Valor total dos pedidos de {aux.nome} R$ {total}')
                            print()

                aux = aux.retornaProximo()
                total_de_todos_os_pedidos += total
            
            print('|===========================================|')
            print('| Total de todos os pedidos por Debito      |') 
            print('|===========================================|')
            print(f'R$ {total_de_todos_os_pedidos}')
            input('Enter para continuar...')

    def relatorio_por_pagamento_credito(self, cardapio):
        if self.primeiro != None:
            aux = self.primeiro
            print('|===========================================|')
            print('| Relatorio por Crédito                     |') 
            print('|===========================================|')
            print()
            total_de_todos_os_pedidos = 0
            while aux:
                total = 0
                for n, pedidos in enumerate(aux.pedido):
                    pagamento, _ = pedidos.forma_de_pagamento()
                    if pagamento == CREDITO:
                        if n == 0:
                            print(f'Os pedidos de {aux.nome}')
                        print()
                        print(f'O {n+1}° de {aux.nome}')
                        print()
                        pedidos.lista_de_pedidos(cardapio)
                        print(f'O total deste pedido R$ {pedidos.total(cardapio)}')
                        total += pedidos.total(cardapio)
                        if len(aux.pedido) == n + 1:    
                            print(f'Valor total dos pedidos de {aux.nome} R$ {total}')
                            print()

                aux = aux.retornaProximo()
                total_de_todos_os_pedidos += total
            
            print('|===========================================|')
            print('| Total de todos os pedidos por Crédito     |') 
            print('|===========================================|')
            print(f'R$ {total_de_todos_os_pedidos}')
            input('Enter para continuar...')

    def relatorio_por_pagamento_pix(self, cardapio):
        if self.primeiro != None:
            aux = self.primeiro
            print('|===========================================|')
            print('| Relatorio por Pix                         |') 
            print('|===========================================|')
            print()
            total_de_todos_os_pedidos = 0
            while aux:
                total = 0
                for n, pedidos in enumerate(aux.pedido):
                    pagamento, _ = pedidos.forma_de_pagamento()
                    if pagamento == PIX:
                        if n == 0:
                            print(f'Os pedidos de {aux.nome}')
                        print()
                        print(f'O {n+1}° de {aux.nome}')
                        print()
                        pedidos.lista_de_pedidos(cardapio)
                        print(f'O total deste pedido R$ {pedidos.total(cardapio)}')
                        total += pedidos.total(cardapio)
                        if len(aux.pedido) == n + 1:    
                            print(f'Valor total dos pedidos de {aux.nome} R$ {total}')
                            print()

                aux = aux.retornaProximo()
                total_de_todos_os_pedidos += total
            
            print('|===========================================|')
            print('| Total de todos os pedidos por Pix         |') 
            print('|===========================================|')
            print(f'R$ {total_de_todos_os_pedidos}')
            input('Enter para continuar...')

   
