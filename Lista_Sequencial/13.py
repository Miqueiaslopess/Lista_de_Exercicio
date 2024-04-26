# 13)Entrar com dois números inteiros e imprimir a seguinte saída: Dividendo, Divisor, Quociente, resto
try:
    num1 = int(input('Digite um dividendo inteiro: '))
    num2 = int(input('Digite um divisor inteiro: '))
    quociente = num1 // num2
    resto = num1 % num2
    print(f'Dividendo: {num1}\nDivisor: {num2}\nQuociente: {quociente}\nResto: {resto}')
except ValueError:
    print('ERRO!!! Digite um valor inteiro.')