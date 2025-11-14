# menu de itens
import os

itens = []
pedidos = []

#def criarPedido1():
    #Um item possúi um número(ID), possúi ao menos um item mas pode ter múltiplos
    #O usuário vai escolher a quantidade do item e então o preço vai ser multiplicado proporcionalmente
    #O pedido ao ser criado, irá para a lista de pendentes e receberá um status, 
    #pedidosPendentes = []
    #pedidoItens = []
    #print("[.==  Criar Pedido  ==.]")
    #pedidoID = len(pedidos) + 1
    
    #aberto = True
    #while aberto:
        #itemPedido = int(input("Digite o código do item [Digite 0 para finalizar o pedido]: "))
        #if itemPedido == 0:
        #    aberto = False
        #pedidoItens.append(itens[itemPedido])
        #print(itens[itemPedido])
        #pedidosPendentes.append([pedidoID, pedidoItens])

def criarPedido():
    itensDoPedido = []

    print(".====================.")
    print("|    Abrir Pedido    |")
    print(".====================.")
    IDPedido = len(pedidos) + 1
    aberto = True
    while aberto:
        try:
            consultarItem()
            addPedido = int(input("Código do item [0 para finalizar]: "))


            if addPedido == 0:
                if itensDoPedido:
                    pedidos.append([IDPedido, itensDoPedido, "Pendente"])
                    print("Pedido finalizado com sucesso!")
                aberto = False
                continue

            indexItem = addPedido - 1

            if indexItem < 0 or indexItem >= len(itens):
                print("Valor digitado inválido!")
                print("Pressione qualquer tecla para continuar...")
                os.system('cls')

            quantidade = int(input("Quantidade: "))
            itens[indexItem][4] -= quantidade
            if quantidade < 1 or quantidade > itens[indexItem][4]:
                print("Quantidade inválida!")
                input("Pressione qualquer tecla para continuar...")
                continue

            itensDoPedido.append([indexItem, itens[indexItem][1], quantidade, itens[indexItem][3], itens[indexItem][3] * quantidade]) # aparece na tela
            os.system('cls') # limpa a tela
            print(f"| Número do pedido: {IDPedido} |")

            totalPedido = 0
            for item in itensDoPedido:
                print(f"| Item: {item[1]} | Valor Unitário: R${item[3]:.2f} | Quantidade: {item[2]} | Subtotal: {item[4]:.2f}")
                totalPedido += item[4]
                print(f"Valor total do pedido: R${totalPedido:.2f}")

        except ValueError:
            print("Valor inválido!")
            input("Pressione qualquer tecla para continuar...")
            os.system('cls')

def mostrarPedido():
    for pedido in pedidos:
        print(f"| Número do pedido: {pedido[0]} | Status: {pedido[2]} ")
        print("| Itens do Pedido: ")

        totalPedido = 0
        for item in pedido[1]:
            print(f"| {item[1]} x{item[2]} | Preço unitário: R${item[3]:.2f} | Subtotal: R${item[4]:.2f} |")
            totalPedido += item[4]
    print(f"| Valor total do pedido: R${totalPedido:.2f}")
    input("Pressione qualquer tecla para continuar...")


def cadastrarItem():
    print("[.===== Cadastro =====.]")
    itemID = len(itens) + 1
    itemNome = input("Nome: ")
    itemDescri = input("Detalhes: ")
    itemPreco = float(input("Preço: R$ "))
    itemEstoque = int(input("Quantidade: "))

    itens.append([itemID, itemNome, itemDescri, itemPreco, itemEstoque])
    print("Item cadastrado com sucesso!")

        
def consultarItem():
    print(".====================.")
    print("| Itens disponíveis  |")
    print(".====================.")
    if not itens:
        print("Não há item cadastrado.")
        input("Pressione qualquer tecla para continuar...")
        os.system('cls')
        return
    for item in itens:
        print(f"| ID: {item[0]} | Nome: {item[1]} | Descrição: {item[2]} | Preço: R${item[3]} | Estoque: {item[4]}UN |")

def atualizarItem():
    while True:
        try:
            consultarItem()
            if not itens:
                input("Pressione qualquer tecla para continuar...")
                break
            itemID = int(input("Código do item a ser alterado: "))

            if itemID < 1 or itemID > len(itens):
                print("Valor digitado inválido!")
                input("Pressione qualquer tecla para continuar...")
                os.system('cls')
                continue

            itemNome = input("Novo nome: ")
            itemDescri = input("Nova descrição: ")
            itemPreco = float(input("Novo preço: R$ "))
            itemEstoque = input("Nova quantidade: ")

            itens[itemID-1] = [itemID, itemNome, itemDescri, itemPreco, itemEstoque]
            print(f"Item atualizado: | ID: {itens[itemID-1][0]} | Nome: {itens[itemID-1][1]} | Descrição: {itens[itemID-1][2]} | Preço: R${itens[itemID-1][3]} | Estoque: {itens[itemID-1][4]}UN |")
            break

        except ValueError:
            print("Valor inválido!")
            input("Pressione qualquer tecla para continuar...")
            os.system('cls')



def main():
    os.system('cls')
    funcionando = True
    while funcionando:
        try:
                
            print("[.====================.]")
            print("[.-.-. Menu Itens .-.-.]")
            print("[.====================.]")
            print("1. Cadastrar novo item")
            print("2. Atualizar item existente")
            print("3. Consultar itens")
            print("4. Abrir pedido")
            print("5. Pedidos em aberto")
            print("0. Finalizar aplicação")
            escolha = (input("Opção: "))
            match escolha:
                case "1":
                    os.system('cls')
                    cadastrarItem()
                case "2":
                    os.system('cls')
                    atualizarItem()
                case "3":
                    os.system('cls')
                    consultarItem()
                case "4":
                    os.system('cls')
                    criarPedido()
                case "5":
                    os.system('cls')
                    mostrarPedido()
                case "0":
                    os.system('cls')
                    print("Aplicação finalizada!")
                    funcionando = False
        except ValueError:
            os.system('cls')
            print("Valor inválido!")
        except IndexError:
            os.system('cls')
            print("Código inválido, não registrado no sistema!")
            
main()