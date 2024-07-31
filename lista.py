#gerencia.py
from elemento import Elemento

primeiro = ultimo = None




while True:
    v1= input('Pedido ou 1 para encerrar: ')

    if v1 != '1':
        novo = Elemento(v1)

        if primeiro == None:
            primeiro = novo
            ultimo = novo
        else:
            ultimo.defineProximo (novo)
            novo.defineAnterior (ultimo)
            ultimo = novo
    else: #o usuário digitou 1 là nin riba!

        if primeiro != None:
    #impressão da lista de pedidos
            aux = primeiro
            print('Lista de pedidos (A -> Z)')
            while aux:
                print(f'{aux}', end='<=>')
                aux = aux.retornaProximo()

            print()
            aux = ultimo
            print('Lista de pedidos (Z -> A)')

            while aux:
                print(f'{aux}', end='<=>')
                aux = aux.retornaAnterior()

        break
