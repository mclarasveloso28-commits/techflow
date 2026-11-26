import urllib.request
import urllib.error
import json
def consultar_cep(cep):
    """Consulta um CEP na API ViaCEP."""

    cep = cep.replace("-", "").strip()

    if len(cep) != 8 or not cep.isdigit():
        print("CEP invalido.")
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = urllib.request.urlopen(url, timeout=10)
        dados = json.loads(resposta.read().decode("utf-8"))

        if "erro" in dados:
            print("CEP nao encontrado.")
            return None

        return dados

    except urllib.error.URLError:
        print("Erro de conexao. Verifique sua internet.")
        return None

    except Exception as erro:
        print(f"Erro inesperado: {erro}")
        return None

    finally:
        print("Consulta de CEP finalizada.")

print(consultar_cep("01001000"))
