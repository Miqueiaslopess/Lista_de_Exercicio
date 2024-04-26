# Leia e apresente dois números inteiros
try:
    num1 = int(input('Digite um Numero Inteiro:'))
    num2 = int(input('Digite outo Numero Inteiro:'))
    print(f'O primeiro numero digitado foi {num1} e o segundo foi {num2}')
except ValueError:
    print('Você digitou um valor inválido.')
    print('Tente novamente.')
