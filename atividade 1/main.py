from cliente import Cliente
from lista import Lista
from pedido import Pedido
from cardapio import CARDAPIO
from interface import *


lista = Lista()

while True:

    op = menu_principal()
    if op.lower() == 'fim' or op.lower() == 'f':
        break
    else:
        match op:
            case '1':
                nome, endereco = cadastrar_cliente()
                cliente = Cliente(nome, endereco)
                lista.add_cliente(cliente)
            case '2':
                nome = encontrar_cliente()
                cliente = lista.buscar_cliente(nome)
                if cliente:
                    p = pedido(cliente.nome)
                    if p:
                        cliente.add_pedido(p)
                else:
                    cliente_nao_encontrado()
            case '3':
                lista.relatorio(CARDAPIO)
            case '4':
                lista.relatorio_por_pagamento_pix(CARDAPIO)
                lista.relatorio_por_pagamento_dinheiro(CARDAPIO)
                lista.relatorio_por_pagamento_debito(CARDAPIO)
                lista.relatorio_por_pagamento_credito(CARDAPIO)
            case '5':
                lista.reverse_relatorio(CARDAPIO)
            case _:
                print('Opção inválida.')