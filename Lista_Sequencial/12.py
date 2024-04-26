#12)Entrar com dois números reais e imprimir a média aritmética com a mensagem “Média” antes do resultado.
try:
    num1 = float(input('Digite um número Real: '))
    num2 = float(input('Digite outo número Real: '))
    media = (num1 + num2)/2
    print(f'A média aritmética de {num1} e {num2} é: {media}')
except ValueError:
    print('Erro: Digite apenas números reais!!!')
