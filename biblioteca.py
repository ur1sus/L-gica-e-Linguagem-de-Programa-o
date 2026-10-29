biblioteca = []

def menu():
  print("\n1 - Cadastrar Lirvro")
  print("2 - Buscar livro por ID")
  print("3 - Listar todos os livros")
  print("4 - Sair do programa")

def cadastro_livro():
  id = int(input("Digite o id: "))
  nome = input("Digite o nome do livro: ")
  autor = input("Digite o nome do autor: ")
  editora = input("Digite o nome da editora: ")
  livro = {
      "id": id,
      "nome": nome,
      "autor": autor,
      "editora": editora
  }
  biblioteca.append(livro)
  print("\nLivro cadastrado com sucesso!")
  
def menu_escolha(escolha):
  match escolha
      case "1":
        cadastro_livro()
      case "2":
        buscar_id()
      case "3":
        listar_livro()

def menu_principal():
  while True:
    menu()
    escolha = input("Digite a escolha [1-4]")
    menu_escolha(escolha)
    if escolha == "4"
      break

menu_principal()    
