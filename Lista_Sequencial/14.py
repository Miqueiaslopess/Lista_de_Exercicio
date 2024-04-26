# 14)Entrar com quatro números e imprimir a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.

#Entrar Com os quatros Números
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
num4 = float(input('Digite o quarto número: '))
# Definir os pesos
peso1 = 1
peso2 = 2
peso3 = 3
peso4 = 4

# Calcular a média ponderada
soma_de_pesos = (peso1 + peso2 + peso3 + peso4)
mediaPonderada = (num1 * peso1 + num2 * peso2 + num3 * peso3 + num4 * peso4) / soma_de_pesos

# Imprimir a média ponderada
print(f'A média ponderada de {num1}, {num2}, {num3} e {num4} é: {mediaPonderada}')


