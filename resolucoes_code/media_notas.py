"""Desafio 5: calcular a média de três notas e informar a situação."""


def calcular_media(nota1: float, nota2: float, nota3: float) -> float:
    for nota in (nota1, nota2, nota3):
        if not 0 <= nota <= 10:
            raise ValueError("As notas devem estar entre 0 e 10.")
    return (nota1 + nota2 + nota3) / 3


def verificar_situacao(media: float, media_minima: float = 7.0) -> str:
    return "Aprovado" if media >= media_minima else "Reprovado"


def main() -> None:
    try:
        nota1 = float(input("Digite a primeira nota (0 a 10): "))
        nota2 = float(input("Digite a segunda nota (0 a 10): "))
        nota3 = float(input("Digite a terceira nota (0 a 10): "))
        media = calcular_media(nota1, nota2, nota3)
        print(f"Média: {media:.2f}")
        print(f"Situação: {verificar_situacao(media)}")
    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
