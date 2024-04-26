'''20)Antes de o racionamento de energia ser decretado, quase ninguém falava em
quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário.
Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo, efetue
o recebimento do valor do salário mínimo e a quantidade de quilowatts gasto por uma
residência e calcule. Apresente:
• O valor em reais de cada quilowatt.
• O valor em reais a ser pago.
• O novo valor a ser pago por essa residência com um desconto de 10%.'''

def ObterEntrada():
    try:
        salario_minimo = float(input('Digite o valor do salário mínimo: '))
        quilowatts = float(input('Digite a quantidade de quilowatts gastos: '))
        return salario_minimo, quilowatts
    except ValueError:
        print('Valor inválido.')
        return ObterEntrada()
    
def ValorQuilowatt(salario_minimo):
    return salario_minimo / 700

def ValorPago(salario_minimo, quilowatts):
    return ValorQuilowatt(salario_minimo) * quilowatts

def ValorPagoDesconto(salario_minimo, quilowatts):
    return ValorPago(salario_minimo, quilowatts) * 0.9

def main():
    salario_minimo, quilowatts = ObterEntrada()
    print(f'O valor de cada quilowatt é: R${ValorQuilowatt(salario_minimo):.2f}')
    print(f'O valor a ser pago é: R${ValorPago(salario_minimo, quilowatts):.2f}')
    print(f'O valor a ser pago com desconto de 10% é: R${ValorPagoDesconto(salario_minimo, quilowatts):.2f}')

main()