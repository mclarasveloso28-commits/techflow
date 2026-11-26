from utils import validar_texto, validar_prioridade, formatar_cep

print(validar_texto("TechFlow"))
print(validar_texto(""))

print(validar_prioridade("Alta"))
print(validar_prioridade("Urgente"))

print(formatar_cep("12345678"))
print(formatar_cep("123"))