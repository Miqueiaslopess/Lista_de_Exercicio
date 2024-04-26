# 11)Leia um número real e imprimir a terça parte deste número.
try:
    num = float(input('Digite um número real: '))
    terca_parte = num / 3
    print(f'A terça parte de {num} é: {terca_parte}')
except ValueError:
    print('Erro: Digite apenas números!!!')