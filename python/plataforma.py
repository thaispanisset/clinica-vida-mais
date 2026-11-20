pacientes = []

while True:
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do paciente: ").strip()

        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("A idade não pode ser negativa.")
                continue
        except ValueError:
            print("Digite uma idade válida.")
            continue

        telefone = input("Telefone: ").strip()

        paciente = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        }
        pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!")

    elif opcao == "2":
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            idades = [p["idade"] for p in pacientes]
            media = sum(idades) / len(idades)
            mais_novo = min(pacientes, key=lambda p: p["idade"])
            mais_velho = max(pacientes, key=lambda p: p["idade"])

            print("Total de pacientes:", len(pacientes))
            print("Idade média:", round(media, 2))
            print("Paciente mais novo:", mais_novo["nome"])
            print("Paciente mais velho:", mais_velho["nome"])

    elif opcao == "3":
        busca = input("Digite o nome para buscar: ").strip().lower()
        encontrados = [
            p for p in pacientes
            if busca in p["nome"].lower()
        ]

        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("Paciente não encontrado.")

    elif opcao == "4":
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            for p in pacientes:
                print(
                    "Nome:", p["nome"],
                    "| Idade:", p["idade"],
                    "| Telefone:", p["telefone"]
                )

    elif opcao == "5":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
