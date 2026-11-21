
# Agora vamos solicitar uma string e um número inteiro como entrada.
# Depois teremos que retornar a string repetida o número de vezes informado.

# Recebe uma string do usuário
texto = input("Digite um texto: ")

# Recebe a quantidade de repetições
quantidade = input("Quantas vezes deseja repetir? ")

# Verifica se a quantidade é um número inteiro não negativo
if quantidade.isdigit():
    quantidade = int(quantidade)

    # Verifica se a quantidade é zero
    if quantidade == 0:
        print("O texto não foi repetido, pois a quantidade informada foi 0.")
    else:
        # Repete o texto
        resultado = " ".join([texto] * quantidade)

        # Exibe o resultado
        print("Resultado:", resultado)
else:
    print("Erro: informe um número inteiro válido.")
