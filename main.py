def mostrar_menu(qtd_produtos):
   print("\n--- Menu ---")
   print(f"Produtos cadastrados: {qtd_produtos}")
   print("1 - Cadastrar produto")
   print("2 - Consultar produto")
   print("0 - Sair")

def cadastrar_produto(produtos):
   nome = input("Nome do produto: ")
   preco_valido = False
   while not preco_valido:
       preco = float(input("Preço do produto (maior que zero): "))
       if preco > 0:
           preco_valido = True
       else:
           print("Preço inválido. Digite um valor maior que zero.")
   produtos.append((nome, preco))
   print("Produto cadastrado com sucesso!")


def consultar_produto(produtos):
   nome_busca = input("Digite o nome do produto: ")
   encontrado = False
   i = 0
   while i < len(produtos):
       if produtos[i][0] == nome_busca:
           print(
               f"Produto encontrado: "
               f"{produtos[i][0]} - R$ {produtos[i][1]:.2f}"
           )
           encontrado = True
       i += 1
   if not encontrado:
       print("Produto não encontrado.")

produtos = []
continuar = True

while continuar:
   mostrar_menu(len(produtos))
   opcao = input("Escolha uma opção: ")
   if opcao == "1":
       cadastrar_produto(produtos)
   elif opcao == "2":
       consultar_produto(produtos)
   elif opcao == "0":
       continuar = False
   else:
       print("Opção inválida.")
