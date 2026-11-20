
# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Recebe dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Recebe a operação matemática
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Realiza a operação matemática
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

# Exibe o resultado
print("Resultado:", resultado)
