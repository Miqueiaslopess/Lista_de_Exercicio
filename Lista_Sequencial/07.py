# Receba um número inteiro e apresente seu sucessor e seu antecessor.
try:
    num1 = int(input('Digite um número inteiro para saber o seu antecessor e o seu sucessor: '))
    antecessor = num1 - 1
    sucessor = num1 + 1
    print(f'O antecessor de {num1} é {antecessor} e o sucessor é {sucessor}')
except ValueError:
    print('Você digitou um valor inválido.Tente novamente.')
