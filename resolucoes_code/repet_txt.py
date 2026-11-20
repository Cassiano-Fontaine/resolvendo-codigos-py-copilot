# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Recebe uma string do usuário
texto = input("Digite um texto: ")

# Recebe a quantidade de repetições
quantidade = int(input("Quantas vezes deseja repetir? "))

# Repete o texto
resultado = " ".join([texto] * quantidade)

# Exibe o resultado
print(resultado)
