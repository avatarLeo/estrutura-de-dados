from cliente import Cliente
from lista import Lista
from pedido import Pedido
from cardapio import CARDAPIO
from interface import *

p = Pedido()
# p.add_pedido(2)
# p.add_pedido(4)
# p.add_pedido(1)

print(p.total(CARDAPIO))

cliente1 = Cliente('José', 'Rua da jaca')
cliente2 = Cliente('Miguel', 'Rua da jaca')
cliente3 = Cliente('Paulo', 'Rua da jaca')
cliente4 = Cliente('Roberto', 'Rua da jaca')

lista = Lista()

lista.add_cliente(cliente1) 
lista.add_cliente(cliente2)
lista.add_cliente(cliente3)
lista.add_cliente(cliente4)

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
                    cliente.add_pedido(p)
                else:
                    cliente_nao_encontrado()
            case '3':
                lista.relatorio(CARDAPIO)

