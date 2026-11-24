
# TECHFLOW CORE
# Gerenciador de Demandas em Memoria

demandas = []


def cadastrar_demanda():
    """Cadastra uma nova demanda no sistema."""

    print("\n=== CADASTRAR DEMANDA ===")

    identificador = input("Digite o ID: ").strip()

    if not identificador:
        print("Erro: o ID nao pode ficar vazio.")
        return

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("Erro: este ID ja esta cadastrado.")
            return

    titulo = input("Titulo da demanda: ").strip()
    solicitante = input("Nome do solicitante: ").strip()
    prioridade = input("Prioridade (Alta, Media ou Baixa): ").strip()
    cep = input("CEP: ").strip()
    cidade = input("Cidade: ").strip()

    if not all([titulo, solicitante, prioridade, cep, cidade]):
        print("Erro: todos os campos sao obrigatorios.")
        return

    prioridades_validas = ["alta", "media", "baixa"]

    if prioridade.lower() not in prioridades_validas:
        print("Erro: prioridade invalida.")
        return

    demanda = {
        "id": identificador,
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade.capitalize(),
        "cep": cep,
        "cidade": cidade,
        "status": "Aberto"
    }

    demandas.append(demanda)

    print("\nDemanda cadastrada com sucesso!")


def listar_demandas():
    """Exibe todas as demandas cadastradas."""

    print("\n=== LISTAR DEMANDAS ===")

    if not demandas:
        print("Nenhuma demanda cadastrada.")
        return

    for demanda in demandas:
        print("\n-------------------------")
        for campo, valor in demanda.items():
            print(f"{campo.capitalize()}: {valor}")
        print("-------------------------")


def buscar_demanda():
    """Busca uma demanda pelo ID."""

    print("\n=== BUSCAR DEMANDA ===")

    identificador = input("Digite o ID da demanda: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("\nDemanda encontrada!")

            for campo, valor in demanda.items():
                print(f"{campo.capitalize()}: {valor}")

            return

    print("Demanda nao encontrada.")


def atualizar_status():
    """Atualiza o status de uma demanda."""

    print("\n=== ATUALIZAR STATUS ===")

    identificador = input("Digite o ID da demanda: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("Status atual:", demanda["status"])

            novo_status = input(
                "Digite o novo status: "
            ).strip()

            if not novo_status:
                print("Erro: o status nao pode ficar vazio.")
                return

            demanda["status"] = novo_status.capitalize()

            print("Status atualizado com sucesso!")
            return

    print("Demanda nao encontrada.")


def excluir_demanda():
    """Exclui uma demanda pelo ID."""

    print("\n=== EXCLUIR DEMANDA ===")

    identificador = input("Digite o ID da demanda: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            demandas.remove(demanda)
            print("Demanda excluida com sucesso!")
            return

    print("Demanda nao encontrada.")


def menu():
    """Apresenta o menu principal do sistema."""

    while True:
        print("\n================================")
        print("       TECHFLOW CORE")
        print(" GERENCIAMENTO DE DEMANDAS")
        print("================================")
        print("1 - Cadastrar demanda")
        print("2 - Listar demandas")
        print("3 - Buscar demanda")
        print("4 - Atualizar status")
        print("5 - Excluir demanda")
        print("0 - Sair")
        print("================================")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_demanda()

        elif opcao == "2":
            listar_demandas()

        elif opcao == "3":
            buscar_demanda()

        elif opcao == "4":
            atualizar_status()

        elif opcao == "5":
            excluir_demanda()

        elif opcao == "0":
            print("Encerrando o TechFlow Core...")
            break

        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    menu()
