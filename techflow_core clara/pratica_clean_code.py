
from datetime import date, timedelta


# Constantes de prazo
PRAZO_ALTA = 1
PRAZO_MEDIA = 3
PRAZO_BAIXA = 5


def normalizar_prioridade(prioridade):
    """Padroniza a prioridade informada pelo usuario."""
    return prioridade.strip().lower().replace("é", "e")


def classificar_chamado(prioridade):
    """Retorna a classificacao do chamado."""
    if prioridade == "alta":
        return "Urgente"
    elif prioridade == "media":
        return "Normal"
    elif prioridade == "baixa":
        return "Baixa"
    else:
        return None


def calcular_prazo(prioridade):
    """Calcula a data limite para resolver o chamado."""
    if prioridade == "alta":
        dias_prazo = PRAZO_ALTA
    elif prioridade == "media":
        dias_prazo = PRAZO_MEDIA
    elif prioridade == "baixa":
        dias_prazo = PRAZO_BAIXA
    else:
        return None

    data_limite = date.today() + timedelta(days=dias_prazo)

    return data_limite


def main():
    """Executa o programa principal."""
    print("=== TECHFLOW CORE ===")

    while True:
        prioridade = input(
            "Digite a prioridade (Alta, Media ou Baixa): "
        )

        prioridade = normalizar_prioridade(prioridade)

        classificacao = classificar_chamado(prioridade)

        if classificacao is not None:
            break

        print("Prioridade invalida! Tente novamente.")

    data_limite = calcular_prazo(prioridade)

    print("\n=== RESULTADO DO CHAMADO ===")
    print("Prioridade:", prioridade.capitalize())
    print("Classificacao:", classificacao)
    print("Prazo:", data_limite.strftime("%d/%m/%Y"))


if __name__ == "__main__":
    main()
