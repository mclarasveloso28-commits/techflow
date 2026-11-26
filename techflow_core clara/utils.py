import os


def limpar_tela():
    """Limpa o terminal conforme o sistema operacional."""
    os.system("cls" if os.name == "nt" else "clear")


def exibir_cabecalho():
    """Exibe o cabeçalho do TechFlow Core."""
    print("=" * 35)
    print("          TECHFLOW CORE")
    print("    SISTEMA DE GESTAO DE DEMANDAS")
    print("=" * 35)

def validar_texto(texto):
    """Verifica se o texto foi preenchido."""
    return texto.strip() != ""

def validar_prioridade(prioridade):
    """Verifica se a prioridade informada é válida."""
    prioridades_validas = ["Alta", "Media", "Baixa"]
    return prioridade in prioridades_validas

def formatar_cep(cep):
    """Formata o CEP no padrão 00000-000."""
    cep = cep.strip().replace("-", "")

    if len(cep) == 8 and cep.isdigit():
        return cep[:5] + "-" + cep[5:]

    return None