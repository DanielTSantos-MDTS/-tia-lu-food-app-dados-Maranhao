# menu de itens
import os
import platform
import json

def carregarItens(): # carrega os itens cadastrados ao inicializar
    try:
        with open('itens.json', 'r', encoding='utf-8') as arqu:
            return json.load(arqu)
    except FileNotFoundError: # caso não exista nenhum item cadastrado
        return [] # ela inicializa como uma lista vazia
    
def carregarPedidos(): # faz o mesmo só que com os pedidos cadastrados
    try:
        with open('pedidos.json', 'r', encoding='utf-8') as arqu:
            return json.load(arqu)
    except FileNotFoundError:
        return []

# atualiza os respectivos arquivos .json conforme alteração
def attItens():
    with open('itens.json', 'w', encoding='utf-8') as arqu:
        json.dump(itens, arqu, indent=4, ensure_ascii=False)

def attPedidos():
    with open('pedidos.json', 'w', encoding='utf-8') as arqu:
        json.dump(pedidos, arqu, indent=4, ensure_ascii=False)


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        print("\033[2J\033[H", end="")
        
itens = carregarItens()
pedidos = carregarPedidos()

pedidos_pendentes = [p for p in pedidos if p["pedidoStatus"] == "PENDENTE"]
pedidos_aceitos = [p for p in pedidos if p["pedidoStatus"] == "ACEITO"]
pedidos_fazendo = [p for p in pedidos if p["pedidoStatus"] == "FAZENDO"]
pedidos_prontos = [p for p in pedidos if p["pedidoStatus"] == "PRONTO"]
esperando_entregador = [p for p in pedidos if p["pedidoStatus"] == "ESPERANDO ENTREGADOR"]
saida_entrega = [p for p in pedidos if p["pedidoStatus"] == "SAIDA PARA ENTREGA"]
pedidos_entregues = [p for p in pedidos if p["pedidoStatus"] == "ENTREGUE"]
pedidos_rejeitados = [p for p in pedidos if p["pedidoStatus"] == "REJEITADO"]

def menu_principal():
    while True:
        clear()
        print("[.=============================================================.]")
        print("[.-.-.   Menu Principal - Sistema de Pedidos FooDDelivery  .-.-.]")
        print("[.-.-.        Desenvolvido pela Equipe Maranhão - UNEX     .-.-.]")
        print("[.=============================================================.]")
        print("[.-.-.                 1 - Menu de Itens                   .-.-.]")
        print("[.-.-.                 2 - Menu de Pedidos                 .-.-.]")
        print("[.-.-.                 3 - Consultas e Relatórios          .-.-.]")
        print("[.-.-.                 0 - Finalizar o Sistema             .-.-.]")
        print("[.=============================================================.]")
        
        menu = input("Escolha uma Opção: ")

        if not menu.isdigit():
            print("Valor inválido, finalizando o sistema!")
            return 

        menu = int(menu) 
         
        match menu:
            case 1:
                menu_itens()
            case 2:
                menu_pedidos()
            case 3:
                menu_consultas()
            case 0:
                print("Finalizando o Sistema!")
                return
            case _:
                print("Opção Inválida! Reiniciando Sistema!")
                input("Pressione ENTER para continuar...")

def menu_itens():
    clear()
    print("[.=============================================================.]")
    print("[.-.-.   Menu de Itens - Sistema de Pedidos FooDDelivery   .-.-.]")
    print("[.=============================================================.]")
    print("[.-.-.             1 - Cadastrar Itens                     .-.-.]")
    print("[.-.-.             2 - Consultar Itens                     .-.-.]")
    print("[.-.-.             3 - Atualizar Itens                     .-.-.]")
    print("[.-.-.             0 - Menu Principal                      .-.-.]")
    print("[.=============================================================.]")

    opcaoItem = input("Escolha uma Opção (Apenas número): ")
    
    if not opcaoItem.isdigit():
            print("Valor inválido, digite apenas números!")
            return  
    opcaoItem = int(opcaoItem)
    
    match opcaoItem:
        case 1:
            clear()
            cadastrarItem()
        case 2:
            clear()
            consultarItem()
        case 3:
            clear()
            atualizarItem()
        case 0:
            print("Voltando para o menu principal")
            input("Pressione ENTER para confirmar")
            clear()
            return
        case _:
            print("Valor Inválido! Voltando ao menu principal!")
            input("Pressione ENTER para continuar")
            
def menu_pedidos():
    clear()
    print("[.=============================================================.]")
    print("[.-.-.  Menu de Pedidos - Sistema de Pedidos FooDDelivery  .-.-.]")
    print("[.=============================================================.]")
    print("[.-.-.             1 - Criar Pedido                        .-.-.]")
    print("[.-.-.             2 - Processar Pedidos                   .-.-.]")
    print("[.-.-.             3 - Atualizar Pedidos                   .-.-.]")
    print("[.-.-.             4 - Cancelar Pedidos                    .-.-.]")
    print("[.-.-.             0 - Menu Principal                      .-.-.]")
    print("[.=============================================================.]")
    
    opcaoPedido = input("Escolha uma Opção: ")
    
    if not opcaoPedido.isdigit():
            print("Valor inválido, digite apenas números!")
            return  
    opcaoPedido = int(opcaoPedido)

    match opcaoPedido:
        case 1:
            clear()
            criarPedido()
        case 2:
            clear()
            processar_pedidos_pendentes()
        case 3:
            clear()
            atualizar_pedido()
        case 4:
            clear()
            cancelar_pedido()
        case 0:
            print("Voltando para o menu principal")
            input("Pressione ENTER para confirmar")
            clear()
            return
        case _:
            print("Valor Invalido! Voltando para o menu principal!")
            input("Pressione ENTER para continuar")
            
def menu_consultas():
    clear()
    print("[.=============================================================.]")
    print("[.-.-.  Menu de Pedidos - Sistema de Pedidos FooDDelivery  .-.-.]")
    print("[.=============================================================.]")
    print("[.-.-.             1 - Exibir Todos Pedidos                .-.-.]")
    print("[.-.-.             2 - Filtrar Pedidos por Status          .-.-.]")
    print("[.-.-.             0 - Menu Principal                      .-.-.]")
    print("[.=============================================================.]")
    
    opcaoConsulta = input("Escolha uma Opção: ")
    
    if not opcaoConsulta.isdigit():
            print("Valor inválido, digite apenas números!")
            return  
    opcaoConsulta = int(opcaoConsulta)

    match opcaoConsulta:
        case 1:
            clear()
            mostrarPedido()
        case 2:
            clear()
            filtrar_pedidos()
        case 0:
            print("Voltando para o menu principal")
            input("Pressione ENTER para confirmar")
            clear()
            return
        case _:
            print("Valor inválido! Voltando ao menu principal!")
            input("Pressione ENTER para continuar")
    
def cadastrarItem():
    print(".====================.")
    print("|  Cadastrar Itens  |")
    print(".====================.")
    item = {
        "itemID": len(itens) + 1,
        "itemNome": input("Nome: "),
        "itemDescri": input("Detalhes: "),
        "itemPreco": float(input("Preço: R$ ")),
        "itemEstoque": int(input("Quantidade: ")),
    }

    itens.append(item)
    # escreve as informações da lista itens dentro de um arquivo json
    attItens()
    print("Item cadastrado com sucesso!")
    input("Pressione ENTER para confirmar")


def consultarItem():
    print(".====================.")
    print("| Itens disponíveis  |")
    print(".====================.")
    if not itens:
        print("Não há item cadastrado.")
        input("Pressione ENTER para continuar...")
        clear()
        return
    for item in itens:
        print(
            f"| ID: {item['itemID']} | Nome: {item['itemNome']} | Descrição: {item['itemDescri']} | Preço: R$ {item['itemPreco']} | Estoque: {item['itemEstoque']} UN |"
        )

    input("Pressione ENTER para continuar")

def atualizarItem():
    while True:
        try:
            consultarItem()
            if not itens:
                input("Pressione ENTER para continuar...")
                break
            itemID = int(input("Código do item a ser alterado (0 para voltar): "))

            if itemID < 1 or itemID > len(itens):
                print("Valor digitado inválido!")
                input("Pressione ENTER para continuar...")
                clear()
                continue

            itemNome = input("Novo nome: ")
            itemDescri = input("Nova descrição: ")
            itemPreco = float(input("Novo preço: R$ "))
            itemEstoque = int(input("Nova quantidade: "))

            itens[itemID - 1] = {
                "itemID": itemID,
                "itemNome": itemNome,
                "itemDescri": itemDescri,
                "itemPreco": itemPreco,
                "itemEstoque": itemEstoque,
            }

            # reescrevendo o item escolhido dentro do itens.json
            # atualizando informações
            attItens()
            
            print(
                f"Item atualizado: | ID: {itens[itemID-1]['itemID']} | Nome: {itens[itemID-1]['itemNome']} | Descrição: {itens[itemID-1]['itemDescri']} | Preço: R${itens[itemID-1]['itemPreco']} | Estoque: {itens[itemID-1]['itemEstoque']}UN |"
            )
            break

        except ValueError:
            print("Valor inválido!")
            input("Pressione ENTER para continuar...")
            clear()



def criarPedido():
    print(".====================.")
    print("|    Abrir Pedido    |")
    print(".====================.")
    aberto = True
    pedido = {
        "idPedido": len(pedidos) + 1,
        "pedidoItens": [],
        "pedidoStatus": "PENDENTE",
        "cupomAplicado": "",
        "pedidoDesconto": 0.0,
        "totalPedido": 0.0
    }
    while aberto:
        try:
            consultarItem()
            addPedido = int(input("Código do item [0 para finalizar]: "))

            if addPedido == 0:
                if pedido["pedidoItens"]:
                    pedidos.append(pedido)
                    attPedidos() # salva os pedidos dentro do .json

                    clear()
                    cupom = input("| Insira o Cupom (OFF5, OFF10, OFF15, ENTER para pular):  ").upper()
                    
                    match cupom:
                        case "OFF5":
                            clear()
                            pedido["pedidoDesconto"] = 0.05
                            pedido["totalPedido"] *= (1 - pedido["pedidoDesconto"])
                            pedido["cupomAplicado"] = cupom
                            
                            print("| Desconto de 5% aplicado! |")
                            print("| Pedido Realizado com Sucesso. |")
                            print(f"| Valor total do pedido: R${pedido['totalPedido']:.2f} |")
                            print("| Aguardando Aprovação |")
                            attPedidos() # salva o desconto
                            input("Pressione ENTER para voltar ao menu principal...")
                            return
                        case "OFF10":
                            clear()
                            pedido["pedidoDesconto"] = 0.10
                            pedido['totalPedido'] *= (1 - pedido["pedidoDesconto"])
                            pedido["cupomAplicado"] = cupom
                            
                            print("| Desconto de 10% aplicado! |")
                            print("| Pedido Realizado com Sucesso. |")
                            print(f"| Valor total do pedido: R${pedido['totalPedido']:.2f} |")
                            print("| Aguardando Aprovação |")
                            attPedidos() # salva o desconto
                            input("Pressione ENTER para voltar ao menu principal...")
                            return
                        case "OFF15":
                            clear()
                            pedido["pedidoDesconto"] = 0.15
                            pedido["totalPedido"] *= (1 - pedido["pedidoDesconto"])
                            pedido["cupomAplicado"] = cupom
                            
                            print("| Desconto de 15% aplicado! |")
                            print("| Pedido Realizado com Sucesso. |")
                            print(f"| Valor total do pedido (com desconto): R${pedido['totalPedido']:.2f} |")
                            print("| Aguardando Aprovação |")
                            input("Pressione ENTER para voltar ao menu principal...")
                            return
                        case "":
                            clear()
                            print("| Nenhum cupom aplicado |")
                            pedido["cupomAplicado"] = "Nenhum cupom aplicado"
                            print("| Pedido Realizado com Sucesso. |")
                            print(f"| Valor total do pedido: R${pedido['totalPedido']:.2f} |")
                            print("| Aguardando Aprovação |")
                            attPedidos() # salva o desconto 
                            input("Pressione ENTER para voltar ao menu principal...")
                            return
                        case _:
                            clear()
                            print("| Cupom inválido ou não existe! Nenhum desconto aplicado. |")
                            pedido["cupomAplicado"] = "Nenhum cupom aplicado"
                            print("| Pedido Realizado com Sucesso. |")
                            print(f"| Valor total do pedido: R${pedido['totalPedido']:.2f} |")
                            print("| Aguardando Aprovação |")
                            attPedidos() # salva o desconto
                            input("Pressione ENTER para voltar ao menu principal...")
                            return
                aberto = False
                continue

            indexItem = addPedido - 1
            if indexItem < 0 or indexItem >= len(itens):
                print("Valor digitado inválido!")
                print("Pressione ENTER para continuar...")
                clear()
                return

            quantidade = int(input("Quantidade: "))
            if quantidade < 1 or quantidade > itens[indexItem]["itemEstoque"]:
                print("Quantidade inválida!")
                input("Pressione tecla para continuar...")
                return
            itens[indexItem]["itemEstoque"] -= quantidade
            # atualiza a quantidade dentro do itens.json
            attItens()

            item = {
                "itemID": itens[indexItem]["itemID"],
                "itemNome": itens[indexItem]["itemNome"],
                "itemQuantidade": quantidade,
                "precoUnitario": itens[indexItem]["itemPreco"],
                "totalItem": itens[indexItem]["itemPreco"] * quantidade,
            }

            pedido["pedidoItens"].append(item)  # aparece na tela
            pedido["totalPedido"] += item["totalItem"]

            clear()  # limpa a tela
            print(f"| Número do pedido: {pedido['idPedido']} |")
            pedidos_pendentes.append(pedido)

            for item in pedido["pedidoItens"]:
                print(
                    f"| Item: {item['itemNome']} | Valor Unitário: R${item['precoUnitario']:.2f} | Quantidade: {item['itemQuantidade']} | Subtotal: {item['totalItem']:.2f}"
                )

            print(f"Valor total do pedido: R${pedido['totalPedido']:.2f}")

        except ValueError:
            print("Valor inválido!")
            input("Pressione ENTER para continuar...")
            clear()
attPedidos() # escreve as informações da lista pedidos dentro de um arquivo json


def mostrarPedido():
    for pedido in pedidos:
        print(
            f"| Número do pedido: {pedido['idPedido']} | Status: {pedido['pedidoStatus']} "
        )

        print("| Itens do Pedido: ")

        for item in pedido["pedidoItens"]:

            print(
                f"| {item['itemNome']} x{item['itemQuantidade']} | Preço unitário: R${item['precoUnitario']:.2f} | Subtotal: R${item['totalItem']:.2f} |"
            )

        print(
            f"| Desconto aplicado no pedido: {pedido["pedidoDesconto"]}"
            f"| Valor total do pedido: R${pedido['totalPedido']:.2f}")

    input("Pressione ENTER para continuar...")

def processar_pedidos_pendentes():
    while True:
        print(".=====================.")
        print("|  Pedidos Pendentes  |")
        print(".=====================.")

        if not pedidos_pendentes:
            print("Nenhum pedido pendente!")
            input("Pressione ENTER para continuar...")
            return

        for pedido in pedidos_pendentes:
            print(
                f"| Número do pedido: {pedido['idPedido']} | Status: {pedido['pedidoStatus']}"
            )
        pedidoProcessar = int(
            input("Digite o número do pedido a ser processado (0 para voltar): ")
        )

        if pedidoProcessar == 0:
            return
        elif pedidoProcessar < 1 or pedidoProcessar > len(pedidos):
            print("Valor digitado inválido!")
            input("Pressione ENTER para continuar...")
            clear()
            continue

        clear()
        pedidoIndex = pedidoProcessar - 1
        print(
            f"| Número do Pedido a Processar: {pedidos[pedidoIndex]['idPedido']} "
            f"| Itens do Pedido: |"
        )
        for item in pedidos[pedidoIndex]["pedidoItens"]:
            print(
                f"| Item: {item['itemNome']} x{item['itemQuantidade']} "
                f"| Preço: R${item['precoUnitario']:.2f} "
                f"| Subtotal: R${item['totalItem']:.2f} |"
            )
        print(f"| Valor Total: R${pedido['totalPedido']:.2f} |")

        action = input("Aceitar Pedido? (S/N): ").upper()

        if action == "S":
            pedidos[pedidoIndex]["pedidoStatus"] = "ACEITO"
            pedidos_aceitos.append(pedidos[pedidoIndex])
            pedidos_pendentes.pop(pedidoIndex)
            attPedidos()
            print("Pedido Aceito e movido para preparo!")
            input("Pressione ENTER para continuar")
        elif action == "N":
            pedidos[pedidoIndex]["pedidoStatus"] = "REJEITADO"
            pedidos_rejeitados.append(pedidos[pedidoIndex])
            pedidos_pendentes.pop(pedidoIndex)
            attPedidos()
            print("Pedido Rejeitado")
            input("Pressione ENTER para continuar")
            
        else:
            print("Valor Inválido")
            input("Pressione ENTER para continuar")

        break
    attPedidos()

def atualizar_pedido():
    print(".======================.")
    print("|   Atualizar Pedido   |")
    print(".======================.")

    if not pedidos:
        print("Nenhum pedido cadastrada!")
        return

    for pedido in pedidos:
        if pedido["pedidoStatus"] != "PENDENTE":
            print(
                f"| Número do pedido: {pedido['idPedido']} | Status: {pedido['pedidoStatus']} |"
            )
            for item in pedido["pedidoItens"]:

                print(
                    f"| {item['itemNome']} x{item['itemQuantidade']} | Preço unitário: R${item['precoUnitario']:.2f} | Subtotal: R${item['totalItem']:.2f} |"
                )

    pedidoAtualizar = int(
        input("Digite número do pedido para atualizar (0 para voltar): ") # se apertar enter com ele vazio, dá erro
    )

    pedido_encontrado = None
    pedidoIndex = None
    
    if pedidoAtualizar == 0:
        clear()
        return
    
    for i, p in enumerate(pedidos):
        if p["idPedido"] == pedidoAtualizar and p["pedidoStatus"] == "ACEITO":
            pedido_encontrado = p
            pedidoIndex = i
            break
    
    if pedido_encontrado is None:
        print("Esse pedido não foi aceito ou não existe!")
        input("Pressione ENTER para continuar...")
        return atualizar_pedido()
    clear()
    print(".===========================.")
    print("|    Status Disponíveis:    |")
    print("|   1 - Em Preparação       |")
    print("|   2 - Preparo Finalizado  |")
    print("|   3 - Esperando Entregador|")
    print("|   4 - Saída para Entrega  |")
    print("|   5 - Entregue            |")
    print(".===========================.")

    action = int(input("Escolha o novo status: "))
    match action:
        case 1:
            pedidos[pedidoIndex]["pedidoStatus"] = "FAZENDO"
            pedidos_fazendo.append(pedidos[pedidoIndex])
            for idx, ped in enumerate(pedidos_aceitos):
                if ped["idPedido"] == pedidoAtualizar:
                    pedidos_aceitos.pop(idx)
                    break
            attPedidos()
            print("Pedido Atualizado com Sucesso!")
            input("Pressione ENTER para continuar...")
            return
        case 2:
            pedidos[pedidoIndex]["pedidoStatus"] = "PRONTO"
            pedidos_prontos.append(pedidos[pedidoIndex])
            for idx, ped in enumerate(pedidos_fazendo):
                if ped["idPedido"] == pedidoAtualizar:
                    pedidos_fazendo.pop(idx)
                    break
            attPedidos()
            print("Pedido Atualizado com Sucesso!")
            input("Pressione ENTER para continuar...")
            return
        case 3:
            pedidos[pedidoIndex]["pedidoStatus"] = "ESPERANDO ENTREGADOR"
            esperando_entregador.append(pedidos[pedidoIndex])
            for idx, ped in enumerate(pedidos_prontos):
                if ped["idPedido"] == pedidoAtualizar:
                    pedidos_prontos.pop(idx)
                    break
            attPedidos()
            print("Pedido Atualizado com Sucesso!")
            input("Pressione ENTER para continuar...")
            return
        case 4:
            pedidos[pedidoIndex]["pedidoStatus"] = "SAIDA PARA ENTREGA"
            saida_entrega.append(pedidos[pedidoIndex])
            for idx, ped in enumerate(esperando_entregador):
                if ped["idPedido"] == pedidoAtualizar:
                    esperando_entregador.pop(idx)
                    break
            attPedidos()
            print("Pedido Atualizado com Sucesso!")
            input("Pressione ENTER para continuar...")
            return
        case 5:
            pedidos[pedidoIndex]["pedidoStatus"] = "ENTREGUE"
            pedidos_entregues.append(pedidos[pedidoIndex])
            for idx, ped in enumerate(saida_entrega):
                if ped["idPedido"] == pedidoAtualizar:
                    saida_entrega.append(idx)
                    break
            attPedidos()
            print("Pedido Atualizado com Sucesso!")
            input("Pressione ENTER para continuar...")
            return
        case _:
            print("Opção inválida!")
            input("Pressione ENTER para continuar...")
            atualizar_pedido()
            attPedidos()
            return
    attPedidos()

def cancelar_pedido():

    print(".=====================.")
    print("|   Cancelar Pedido   |")
    print(".=====================.")

    if not pedidos:
        print("Nenhum Pedido Cadastrado")
        return

    for pedido in pedidos:
        if pedido["pedidoStatus"] == "PENDENTE" or pedido["pedidoStatus"] == "ACEITO":
            print(
                f"| Número do pedido: {pedido['idPedido']} | Status: {pedido['pedidoStatus']} |"
            )
            for item in pedido["pedidoItens"]:

                print(
                    f"| {item['itemNome']} x{item['itemQuantidade']} | Preço unitário: R${item['precoUnitario']:.2f} | Subtotal: R${item['totalItem']:.2f} |"
                )

    pedidoCancelar = int(input("Número do pedido a Cancelar (0 para voltar): ")) # se der enter com valor vazio, dá erro

    if pedidoCancelar == 0:
        clear()
        return
    elif pedidoCancelar < 1 or pedidoCancelar > len(pedidos_aceitos):
        print("Valor Inválido!")
        input("Pressione ENTER para continuar")
        clear()
        cancelar_pedido()

    pedidoIndex = pedidoCancelar - 1
    print(
        f"| Número do Pedido Selecionado: {pedidos[pedidoIndex]['idPedido']} | Status: {pedidos[pedidoIndex]['pedidoStatus']} |"
    )
    action = input("Deseja cancelar este pedido? (S/N): ").upper()
    if action == "S":
        pedidos[pedidoIndex]["pedidoStatus"] = "CANCELADO"
        pedidos.pop(pedidoIndex)
        if pedido[pedidoIndex]["pedidoStatus"] == "PENDENTE":
            pedidos_pendentes.pop(pedidoIndex)
        elif pedido[pedidoIndex]["pedidoStatus"] == "ACEITO":
            pedidos_aceitos.pop(pedidoIndex)
        print("Cancelamento realizado!")
        return
    elif action == "N":
        print("Cancelamento não realizado!")
        return
    else:
        print("Valor Inválido!")
        input("Pressione o ENTER para continuar")
        return



def filtrar_pedidos():
    print(".=============================.")
    print("| Filtrar Pedidos por Status  |")
    print(".=============================.")

    if not pedidos:
        print("Nenhum pedido cadastrado!")
        return
    
    statusFiltrar = input("Digite o status para filtrar: ").upper()
    Localizados = False

    print(f"| Todos os Pedidos com o status: {statusFiltrar} |")
    
    for pedido in pedidos:
        if statusFiltrar == pedido["pedidoStatus"]:
            print(f"| Numero do pedido: {pedido['idPedido']} |"
                  f"\n| Cupom aplicado: {pedido['cupomAplicado']} |"
                  f"\n| Desconto: {pedido['pedidoDesconto']} |"
                  f"\n| Valor total do pedido: {pedido['totalPedido']} |")
            Localizados = True
            input("Pressione ENTER para continuar...")
        
    if not Localizados:
        print(f"| Nenhum pedido com status {statusFiltrar} |")
        input("Pressione ENTER para continuar...")

menu_principal()
