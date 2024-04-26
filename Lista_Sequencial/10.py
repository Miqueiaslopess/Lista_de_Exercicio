# Receba dois números inteiros e apresente o seu produto.
try:
    num1 = int(input('Digite um número inteiro: '))
    num2 = int(input('Digite outo numero inteiro: '))
    produto = num1 * num2
    print(f'O produto de {num1} e {num2} é: {produto}')
except ValueError:
    print('Erro: Digite apenas números inteiros!!!')