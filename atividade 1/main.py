from cliente import Cliente
from lista import Lista

cliente1 = Cliente('José', 'Rua da jaca')
cliente2 = Cliente('Miguel', 'Rua da jaca')
cliente3 = Cliente('Paulo', 'Rua da jaca')
cliente4 = Cliente('Roberto', 'Rua da jaca')

lista = Lista()

lista.add_cliente(cliente1)
lista.add_cliente(cliente2)
lista.add_cliente(cliente3)
lista.add_cliente(cliente4)

lista.relatorio()