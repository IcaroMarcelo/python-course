alunos = []

while True:
    print(f"====MENU====")
    print(f"1-Cadastrar Aluno")
    print(f"2-Listar Aluno")
    print(f"3-Buscar Aluno")
    print(f"4-Remover Aluno")
    print(f"5-Sair")
    opcao = int(input("Escolha uma das opções: "))

    if opcao == 1:
        print(f"====Cadastrar Aluno====")
        nome = input("Insira seu Nome:")
        idade = int(input("Insira sua Idade:"))
        cidade = input("Insira seu Cidade:")
        
        aluno = {
            "nome" : nome,
            "idade" : idade,
            "cidade" : cidade
            }
        alunos.append(aluno)
        print(f"Aluno cadastrado com sucesso!")
    elif opcao == 2:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        print(f"====Listar Aluno====")
        for indice, valor in enumerate(alunos):
            print(indice,valor)
    elif opcao == 3:
        print(f"====Buscar Aluno====")
        busca = input("Digite o nome do aluno:")
        encontrado = False
        for item in alunos:
            if  item["nome"] == busca:
                encontrado = True
                print("Aluno encontrado!")
                print(item["nome"])
                print(item["idade"])
                print(item["cidade"])
                break
        if not encontrado:
            print("Aluno não encontrado!")
    elif opcao == 4:
        print(f"====Remover Aluno====")
        remover = input("Insira o nome de quem voce quer remover: ")
        encontrado = False
        for item in alunos:
            if item["nome"] == remover:
                encontrado = True
                alunos.remove(item)
                print("Aluno removido com sucesso!")
                break
        if not encontrado:
            print("Aluno não encontrado!")
    elif opcao == 5:
        print(f"Programa encerrado")
        break
    else:
        print(f"Opção inválida")





