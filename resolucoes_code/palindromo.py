# Verifique se uma palavra ou frase e um palindromo.

texto = input("Digite uma palavra ou frase: ")
texto = texto.lower().replace(" ", "")

if texto == texto[::-1]:
    print("E um palindromo.")
else:
    print("Nao e um palindromo.")
