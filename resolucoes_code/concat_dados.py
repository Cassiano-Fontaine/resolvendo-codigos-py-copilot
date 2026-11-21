# Vamos receber dois dados diferentes do usuario e concatena-los em uma unica string.

primeiro_dado = input("Digite o primeiro dado: ")
segundo_dado = input("Digite o segundo dado: ")
separador = input("Digite o separador (Enter para usar espaco): ")

if separador == "":
    separador = " "

resultado = primeiro_dado + separador + segundo_dado
print(resultado)
