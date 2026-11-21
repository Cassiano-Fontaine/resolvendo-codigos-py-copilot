# Vamos calcular a media de tres notas fornecidas pelo usuario.

nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
nota3 = float(input("Digite a terceira nota (0 a 10): "))

# Verifica se as notas estao entre 0 e 10
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
    media = (nota1 + nota2 + nota3) / 3
    print("Media:", round(media, 2))

    if media >= 7:
        print("Situacao: Aprovado")
    else:
        print("Situacao: Reprovado")
else:
    print("Erro: as notas devem estar entre 0 e 10.")
