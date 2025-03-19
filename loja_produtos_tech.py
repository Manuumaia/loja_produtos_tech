Clientes = {
    1: {"nome": "Olivia Rodrigo", "usuario": "olivia123", "senha": "senhaolivia"},
    2: {"nome": "Demétrius de Castro", "usuario": "demetrius456", "senha": "senhademetrius"},
    3: {"nome": "Billie Eilish", "usuario": "billie789", "senha": "senhabillie"},
    4: {"nome": "Sabrina Carpenter", "usuario": "sabrina123", "senha": "senhasabrina"},
    5: {"nome": "Justin Bieber", "usuario": "justin94", "senha": "senhajustin"},
    6: {"nome": "Harry Styles", "usuario": "harrys82", "senha": "senhaharry"},
}
Produtos = {
    1: {"produto": "Computador", "preço": 10000, "estoque": 10},
    2: {"produto": "Tablet", "preço": 5000, "estoque": 10},
    3: {"produto": "Smartphone", "preço": 7000, "estoque": 10},
    4: {"produto": "Smartwatch", "preço": 3000, "estoque": 10},
    5: {"produto": "Fone sem fio", "preço": 300, "estoque": 10},
    6: {"produto": "E-reader", "preço": 700, "estoque": 10},
    7: {"produto": "Smartspeaker", "preço": 269, "estoque": 10},
    8: {"produto": "Smartdisplay", "preço": 620, "estoque": 10},
    9: {"produto": "Mouse", "preço": 99, "estoque": 10},
    10: {"produto": "Carregador portátil", "preço": 149, "estoque": 10},
    11: {"produto": "XboxOne", "preço": 2650, "estoque": 10},
    12: {"produto": "PlayStation5", "preço": 3533, "estoque": 10}
}

Vendedores = {
    "Leticia Moura": {"usuario": "leticia123", "senha": "senha123"},
    "Manuella Maia": {"usuario": "manuella123", "senha": "senha123"},
    "Mill Luna": {"usuario": "mill123", "senha": "senha123"},
    "Natalia Clavijo": {"usuario": "natalia123", "senha": "senha123"}
}

Vendas_realizadas = []
Carrinho_cliente = {}

def cadastrar_cliente():
    print("--- Cadastro de Novo Cliente ---")
    nome = input("Nome completo: ")
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    for cliente in Clientes.values():
        if cliente["usuario"] == usuario:
            print("-"*30)
            print("Esse nome de usuário já está em uso. Escolha outro.")
            print("-"*30)
            return None

    novo_id = max(Clientes.keys()) + 1 if Clientes else 1
    Clientes[novo_id] = {"nome": nome, "usuario": usuario, "senha": senha}
    print("-"*30)
    print(f"Cliente {nome} cadastrado com sucesso!")
    print("-"*30)
    return novo_id

def autenticar_cliente():
    print("--- Login ---")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    for id_cliente, dados in Clientes.items():
        if dados["usuario"] == usuario and dados["senha"] == senha:
            print("-"*30)
            print(f"Bem-vindo(a), {dados['nome']}!")
            print("-"*30)
            return id_cliente
    print("-"*30)
    print("Usuário ou senha incorretos. Tente novamente.")
    print("-"*30)
    return None

def autenticar_vendedor():
    print("--- Login de Vendedor ---")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    for vendedor, credenciais in Vendedores.items():
        if credenciais["usuario"] == usuario and credenciais["senha"] == senha:
            print("-"*30)
            print(f"Bem-vindo, Vendedor {vendedor.capitalize()}!")
            print("-"*30)
            return vendedor
    
    print("Usuário ou senha incorretos. Tente novamente.")
    return None

def realizar_compra(cliente_id):
    carrinho = []
    total_venda = 0  
    vendedor = ""
    
    print("-"*30)
    print("Escolha um vendedor:")
    for idx, vendedor_nome in enumerate(Vendedores, start=1):
        print(f"{idx}. {vendedor_nome}")
    while True:
        try:
            vendedor_escolhido = int(input("Digite o número do vendedor escolhido: "))
            print("-"*30)
            if vendedor_escolhido < 1 or vendedor_escolhido > len(Vendedores):
                raise ValueError
            vendedor = list(Vendedores)[vendedor_escolhido - 1]  
            break
        except ValueError:
            print("-"*30)
            print("Opção inválida. Tente novamente.")
            print("-"*30)

    carrinho = Carrinho_cliente.get(cliente_id, [])
    while True:
        print("--- Produtos Disponíveis ---")
        for id_produto, detalhes in Produtos.items():
            print(f"ID: {id_produto} | Produto: {detalhes['produto']} | Preço: R${detalhes['preço']}")
        print("-"*30)

        produto_id = int(input("Digite o ID do produto que deseja comprar (ou 0 para finalizar): "))

        if produto_id == 0:
            break

        if produto_id not in Produtos:
            print("Produto inválido.")
            continue

        produto = Produtos[produto_id]
        print("-"*30)
        quantidade = int(input(f"Quantas unidades de {produto['produto']} deseja comprar? "))

        if produto["estoque"] < quantidade:
            print("Estoque insuficiente.")
            continue

        produto["estoque"] -= quantidade
        carrinho.append({"produto": produto["produto"], "preço": produto["preço"], "quantidade": quantidade})

    Carrinho_cliente[cliente_id] = carrinho

    nome_cliente = Clientes[cliente_id]["nome"]

    for item in carrinho:
        subtotal = item["preço"] * item["quantidade"]
        total_venda += subtotal  

    comissao_vendedor = total_venda * 0.05  
    imposto = total_venda * 0.25  
    total_final = total_venda + imposto  

    venda = {
        "cliente": nome_cliente,
        "vendedor": vendedor,
        "produtos": carrinho,
        "total": total_venda,
        "comissao_vendedor": comissao_vendedor,
        "imposto": imposto,
        "total_final": total_final
    }
    Vendas_realizadas.append(venda)

    print("-"*30)
    print("Compra finalizada!")
    print("-"*30)
    print("--- Nota Fiscal da Compra ---")
    print(f"Cliente: {nome_cliente}")
    print(f"Vendedor: {vendedor}")
    print("Produtos comprados:")
    for item in carrinho:
        subtotal = item["preço"] * item["quantidade"]
        print(f"{item['quantidade']}x {item['produto']} | Preço Unitário: R${item['preço']} | Subtotal: R${subtotal}")

    print(f"Total da venda: R${total_venda}")
    print("-"*30)

def relatorio_vendas():
    if not Vendas_realizadas:
        print("-"*30)
        print("Nenhuma venda realizada ainda.")
        print("-"*30)
        return

    print("-"*30)
    print("--- Relatório de Vendas ---")
    print("-"*30)
    for venda in Vendas_realizadas:
        print(f"Cliente: {venda['cliente']}")
        print(f"Vendedor: {venda['vendedor']}")
        print("-"*30)
        print("Produtos vendidos:")

        for produto in venda["produtos"]:
            subtotal_produto = produto['quantidade'] * produto['preço']
            print(f"- {produto['quantidade']}x {produto['produto']} | Valor: R${produto['preço']:.2f} | Subtotal: R${subtotal_produto:.2f}")
        print("-"*30)
        print(f"Total da venda: R${venda['total']:.2f}")
        print(f"Imposto: R${venda['imposto']:.2f}")
        print(f"Comissão do vendedor: R${venda['comissao_vendedor']:.2f}")
        print(f"Total final (com imposto): R${venda['total_final']:.2f}")
        print("-" * 30)

def ver_carrinho(cliente_id):
    carrinho = Carrinho_cliente.get(cliente_id, [])
    if not carrinho:
        print("Carrinho vazio.")
        return

    print("--- Seu Carrinho ---")
    for item in carrinho:
        print(f"{item['quantidade']}x {item['produto']} - R${item['preço']}")
    print("-"*30)

def ver_estoque():
    print("-"*30)
    print("--- Estoque de Produtos ---")
    print("-"*30)
    for id_produto, detalhes in Produtos.items():
        print(f"Produto: {detalhes['produto']} | Estoque: {detalhes['estoque']} unidades")

def cadastrar_produto():
    nome_produto = input("Nome do produto: ")
    preco_produto = float(input("Preço do produto: "))
    estoque_produto = int(input("Quantidade em estoque: "))
    id_produto = max(Produtos.keys()) + 1 if Produtos else 1

    Produtos[id_produto] = {"produto": nome_produto, "preço": preco_produto, "estoque": estoque_produto}
    print("-"*30)
    print(f"Produto {nome_produto} cadastrado com sucesso!")
    print("-"*30)

def menu():
    while True:
        print("--- TechLadies - Produtos Tech ---")
        print("1. Login de Cliente")
        print("2. Login de Vendedor")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("1. Já sou cliente")
            print("2. Quero me cadastrar")
            escolha_cliente = input("Escolha uma opção: ")

            if escolha_cliente == "1":
                cliente_id = autenticar_cliente()
                if cliente_id:
                    while True:
                        print("1. Realizar Compra")
                        print("2. Ver Carrinho")
                        print("3. Sair")
                        opcao_cliente = input("Escolha uma opção: ")

                        if opcao_cliente == "1":
                            realizar_compra(cliente_id)
                        elif opcao_cliente == "2":
                            ver_carrinho(cliente_id)
                        elif opcao_cliente == "3":
                            break
                        else:
                            print("Opção inválida.")
            elif escolha_cliente == "2":
                cliente_id = cadastrar_cliente()
                if cliente_id:
                    print("Faça o login para continuar.")
                    print("-"*30)

        elif opcao == "2":
            vendedor = autenticar_vendedor()
            if vendedor:
                while True:
                    print("1. Ver Estoque")
                    print("2. Relatório de Vendas")
                    print("3. Cadastrar Produto")
                    print("4. Sair")
                    opcao_vendedor = input("Escolha uma opção: ")

                    if opcao_vendedor == "1":
                        ver_estoque()
                    elif opcao_vendedor == "2":
                        relatorio_vendas()
                    elif opcao_vendedor == "3":
                        cadastrar_produto()
                    elif opcao_vendedor == "4":
                        break
                    else:
                        print("Opção inválida.")
        elif opcao == "3":
            print("-"*30)
            print("Finalizando sistema... Volte Sempre!")
            print("-"*30)
            break
        else:
            print("Opção inválida.")

menu()
