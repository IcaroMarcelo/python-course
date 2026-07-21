livros = []
def cadastrar_livro(livros):
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    pagina = input("Página: ")
    livro = {
        "titulo" : titulo,
        "autor" : autor,
        "pagina" : pagina
        }
    livros.append(livro)
    print(f"Livro cadastrado com sucesso!")
def listar_livros(livros):
    print("2 - Listar livro")
    if not livros:
        print("nenhum livro cadastrado!")
    for indice,valor in enumerate(livros, start=1):
        print(indice, valor)
def atualizar_livros(livros):
    print("3 - Atualizar livro")
    busca = input(("Qual livro deseja atualizar?")) 
    encontrado = False
    for item in livros:
        if item["titulo"] == busca:
            encontrado = True
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            pagina = input("Página: ")
            item["titulo"] = titulo
            item["autor"] = autor
            item["pagina"] = pagina
            print(f"Livro atualizado com sucesso!")
            break
    if not encontrado:
        print("certo livro nao existe!")
def remover_livro(livros):
    print("4 - Remover livro")
    busca = input("Qual livro deseja remover?")
    encontrado = False
    for indice,item in enumerate(livros, start=1):
        if item["titulo"]== busca:
            encontrado = True
            livros.pop(indice)
            print("Livro removido com sucesso!")
            break
    if not encontrado:
        print("Nenhum livro encontrado!")
        
                
while True:
    
    
       
    print("===== MENU =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livro")
    print("3 - Atualizar livro")
    print("4 - Remover livro")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada."))
    
    if opcao == 1:
        cadastrar_livro(livros)
    elif opcao == 2:
        listar_livros(livros)
    elif opcao == 3:
        atualizar_livros(livros)
    elif opcao == 4:
        remover_livro(livros)
    elif opcao == 5:
        break
    else:
        print("opção inválida!")      