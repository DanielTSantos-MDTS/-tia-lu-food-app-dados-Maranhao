# menu de itens
import os

itens = []
pedidos = []
fila_pendentes = []
fila_aceitos = []
fila_prontos = []

# simular pull request

# def criarPedido1():
# Um item possúi um número(ID), possúi ao menos um item mas pode ter múltiplos
# O usuário vai escolher a quantidade do item e então o preço vai ser multiplicado proporcionalmente
# O pedido ao ser criado, irá para a lista de pendentes e receberá um status,
# pedidosPendentes = []
# pedidoItens = []
# print("[.==  Criar Pedido  ==.]")
# pedidoID = len(pedidos) + 1

# aberto = True
# while aberto:
# itemPedido = int(input("Digite o código do item [Digite 0 para finalizar o pedido]: "))
# if itemPedido == 0:
#    aberto = False
# pedidoItens.append(itens[itemPedido])
# print(itens[itemPedido])
# pedidosPendentes.append([pedidoID, pedidoItens])


def criarPedido():
    print(".====================.")
    print("|    Abrir Pedido    |")
    print(".====================.")
    aberto = True
    pedido = {
        "idPedido": len(pedidos) + 1,
        "pedidoQuantidade": 0,
        "pedidoItens": [],
        "pedidoStatus": "Pendente",
        "totalPedido": 0.0
    }
    while aberto:
        try:
            consultarItem()
            addPedido = int(input("Código do item [0 para finalizar]: "))

            if addPedido == 0:
                if pedido["pedidoItens"]:
                    pedidos.append(pedido)
                    print("Pedido finalizado com sucesso!")
                aberto = False
                continue

            indexItem = addPedido - 1
            if indexItem < 0 or indexItem >= len(itens):
                print("Valor digitado inválido!")
                print("Pressione qualquer tecla para continuar...")
                os.system("cls")

            quantidade = int(input("Quantidade: "))
            if (
                quantidade < 1
                or quantidade > itens[indexItem]["itemEstoque"]
            ):
                print("Quantidade inválida!")
                input("Pressione qualquer tecla para continuar...")
                continue
            itens[indexItem]["itemEstoque"] -= quantidade

            item = {
                "itemID": itens[indexItem]["itemID"],
                "itemNome": itens[indexItem]["itemNome"],
                "itemQuantidade": quantidade,
                "precoUnitario": itens[indexItem]["itemPreco"],
                "totalItem": itens[indexItem]["itemPreco"] * quantidade,
            }

            pedido["pedidoItens"].append(item)  # aparece na tela
            pedido["totalPedido"] += item["totalItem"]

            os.system("cls")  # limpa a tela
            print(f"| Número do pedido: {pedido['idPedido']} |")
            

            for item in pedido["pedidoItens"]:
                print(
                    f"| Item: {item['itemNome']} | Valor Unitário: R${item['precoUnitario']:.2f} | Quantidade: {item['itemQuantidade']} | Subtotal: {item['totalItem']:.2f}"
                )

            print(f"Valor total do pedido: R${pedido['totalPedido']:.2f}")

        except ValueError:
            print("Valor inválido!")
            input("Pressione qualquer tecla para continuar...")
            os.system("cls")


def mostrarPedido():
    for pedido in pedidos:
        print(
            f"| Número do pedido: {pedido['idPedido']} | Status: {pedido['pedidoStatus']} "
        )
        #        print(f"| Número do pedido: {pedido[0]} | Status: {pedido[2]} ")

        print("| Itens do Pedido: ")

        for item in pedido["pedidoItens"]:
            #        for item in pedido[1]:

            print(
                f"| {item['itemNome']} x{item['itemQuantidade']} | Preço unitário: R${item['precoUnitario']:.2f} | Subtotal: R${item['totalItem']:.2f} |"
            )

        print(f"| Valor total do pedido: R${pedido['totalPedido']:.2f}")
    #    print(f"| Valor total do pedido: R${totalPedido:.2f}")

    input("Pressione qualquer tecla para continuar...")


def cadastrarItem():
    print("[.===== Cadastro =====.]")
    item = {
        "itemID": len(itens) + 1,
        "itemNome": input("Nome: "),
        "itemDescri": input("Detalhes: "),
        "itemPreco": float(input("Preço: R$ ")),
        "itemEstoque": int(input("Quantidade: ")),
    }
    
    itens.append(item)
    print("Item cadastrado com sucesso!")


def consultarItem():
    print(".====================.")
    print("| Itens disponíveis  |")
    print(".====================.")
    if not itens:
        print("Não há item cadastrado.")
        input("Pressione qualquer tecla para continuar...")
        os.system("cls")
        return
    for item in itens:
        print(item, type(item))
        print(
            f"| ID: {item['itemID']} | Nome: {item['itemNome']} | Descrição: {item['itemDescri']} | Preço: R$ {item['itemPreco']} | Estoque: {item['itemEstoque']} UN |"
        )


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
                os.system("cls")
                continue

            itemNome = input("Novo nome: ")
            itemDescri = input("Nova descrição: ")
            itemPreco = float(input("Novo preço: R$ "))
            itemEstoque = input("Nova quantidade: ")

            # itens[itemID]["itemNome"] = input("Novo nome: ")
            # itens[itemID]["itemDescri"] = input("Nova descrição: ")
            # itens[itemID]["itemPreco"] = float(input("Novo preço: R$ "))
            # itens[itemID]["itemEstoque"] = input("Nova quantidade: ")

            itens[itemID - 1] = {
                "itemID" : itemID,
                "itemNome": itemNome,
                "itemDescri": itemDescri,
                "itemPreco": itemPreco,
                "itemEstoque": itemEstoque
            }
            print(
                f"Item atualizado: | ID: {itens[itemID-1]['itemID']} | Nome: {itens[itemID-1]['itemNome']} | Descrição: {itens[itemID-1]['itemDescri']} | Preço: R${itens[itemID-1]['itemPreco']} | Estoque: {itens[itemID-1]['itemEstoque']}UN |"
            )
            break

        except ValueError:
            print("Valor inválido!")
            input("Pressione qualquer tecla para continuar...")
            os.system("cls")

def processar_pedidos_pendentes():
    while True:
        mostrarPedido()
        print(".====================.")
        print("| Pedidos Pendentes  |")
        print(".====================.")
# def processar_pedidos_pendentes():
#     print("\n⚡ --- Processar Pedidos Pendentes ---")
    
#     if not fila_pendentes:
#         print("✅ Nenhum pedido pendente!")
#         return
    
#     pedido = fila_pendentes[0]
    
#     print(f"\n📄 Pedido #{pedido.numero}")
#     print("🛒 Itens do pedido:")
#     for item, quantidade in pedido.itens:
#         print(f"  - {item.nome} x{quantidade}")
#     print(f"💵 Valor total: R$ {pedido.valor_total:.2f}")
    
#     acao = input("\n✅ Aceitar pedido? (S/N): ").upper()
    
#     if acao == "S":
#         pedido.status = "ACEITO"
#         fila_aceitos.append(pedido)
#         print("✅ Pedido aceito e movido para preparo!")
#     else:
#         pedido.status = "REJEITADO"
#         print("❌ Pedido rejeitado!")
    
#     fila_pendentes.pop(0)


def main():
    os.system("cls")
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
            escolha = input("Opção: ")
            match escolha:
                case "1":
                    os.system("cls")
                    cadastrarItem()
                case "2":
                    os.system("cls")
                    atualizarItem()
                case "3":
                    os.system("cls")
                    consultarItem()
                case "4":
                    os.system("cls")
                    criarPedido()
                case "5":
                    os.system("cls")
                    mostrarPedido()
                case "0":
                    os.system("cls")
                    print("Aplicação finalizada!")
                    funcionando = False
        except ValueError:
            os.system("cls")
            print("Valor inválido!")
        except IndexError:
            os.system("cls")
            print("Código inválido, não registrado no sistema!")


main()
