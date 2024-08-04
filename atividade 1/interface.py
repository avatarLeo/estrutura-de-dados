from cardapio import CARDAPIO
from pedido import Pedido


def menu_principal():
    print('|===========================================|')
    print('| Olá seja bem vindo(a) como posso ajudar   |')
    print('| Escolha uma opção                         |')
    print('|===========================================|')
    print('| Cadastrar um cliente [1]                  |')
    print('| Adicionar pedido [2]                      |')
    print('| Mostrar pedidos [3]                       |')
    print('| Mostrar pedidos por forma de pagamento[4] |')
    print('| Mostrar relatório do ultimo ao primeiro [5]')
    print('| Para sair [FIM]                           |')
    print('|===========================================|')

    op = input('>')

    return op

def cadastrar_cliente():
    print()
    nome = input('Informe o seu nome: ')
    endereco = input('Informe o seu endereço: ')

    return nome, endereco

def pedido(nome):

    pedidos = Pedido()
    print(f'Seja bem vindo {nome}:')
    print('Esse é o nosso cardapio:')
    print()
    while True:
        for item in CARDAPIO:
            print(f"{' '*3}{item.get('nome', 'n')} valor: R$ {item.get('valor')}.00 nuḿero do pedido: [{item.get('id')}]")
            print()
        pe = input('Número do pedido ou F pra sair: ')
        if pe.upper() == 'F':
            if pedidos.itens:
                print()
                print('Confira o pedido')
                pedidos.lista_de_pedidos(CARDAPIO)
                con = input('Confirma o pedido? [S | N] ')
                if con.lower() == 's':
                    print('Forma de pagamento: ')
                    print('Pix [1]')
                    print('Dinheiro [2]')
                    print('Credito [3]')
                    print('Debito [4]')

                    try:
                        forma = int(input('Digite o número da forma de pagamento: '))
                        if forma < 5 or forma > 0:
                            pedidos.confirma_pedido(forma)
                            print('Pedido Realzado com sucesso!')
                            input()
                            
                    except Exception as erro:
                        print('Numero invalido')
                else:
                    pedidos = None
                    print('Ó que pena que nada lhe agradou, volte sempre')
                    print()

            break
        else:
            try:
                pe = int(pe)
                if len(CARDAPIO) < pe or pe < 1:
                    print('Número do pidido inválido, tente novamente')
                for item in CARDAPIO:
                    for k, v in item.items():
                        if k == 'id' and v == pe:
                            print('Adicionado...')
                            pedidos.add_pedido(pe)
            except:
                print('Numero do pedido é inválido!')

    return pedidos

def encontrar_cliente():
    nome = input('Nome do cliente: ')
    return nome

def cliente_nao_encontrado():
    print()
    print('Ops')
    print('Cliente não encontrado tente novamente')

if __name__ == '__main__':
    pedido('jao')