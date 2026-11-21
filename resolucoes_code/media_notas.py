
# Vamos calcular a média de três notas fornecidas pelo usuário.

# Recebe as três notas
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
nota3 = float(input("Digite a terceira nota (0 a 10): "))

# Verifica se as notas estão entre 0 e 10
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:

    # Calcula a média das notas
    media = (nota1 + nota2 + nota3) / 3

    # Exibe a média
    print("Média:", round(media, 2))

    # Verifica a situação do aluno
    if media >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")

else:
    print("Erro: as notas devem estar entre 0 e 10.")
