import os

gastos = []

try:
    with open("gastos.txt", "r") as arquivo:
        for linha in arquivo:
            nome, valor = linha.strip().split(";")
            gastos.append((nome, float(valor)))
except FileNotFoundError:
    pass

while True:
    os.system("cls")
    print("=" * 30)
    print(" Controle Financeiro ")
    print("=" * 30)

    print("1 - Adicionar gasto")
    print("2 - Listar gastos")
    print("3 - Mostrar total")
    print("4 - Sair")

    print("=" * 30)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do gasto: ")
        valor = float(input("Valor do gasto: R$ "))

        gastos.append((nome, valor))

        with open("gastos.txt", "a") as arquivo:
            arquivo.write(f"{nome};{valor}\n")

        print("Gasto adicionado e salvo com sucesso!")
        input("Pressione ENTER para continuar...")

    elif opcao == "2":
        if len(gastos) == 0:
            print("Nenhum gasto cadastrado ainda.")
        else:
            print("Lista de gastos:")
            for nome, valor in gastos:
                print(f"{nome} - R$ {valor}")

        input("Pressione ENTER para continuar...")

    elif opcao == "3":
        total = sum(valor for nome, valor in gastos)
        print(f"Total gasto: R$ {total}")

        input("Pressione ENTER para continuar...")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, tente novamente.")
        input("Pressione ENTER para continuar...")
