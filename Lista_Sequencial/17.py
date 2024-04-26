'''17)Entre com um número e apresentar a seguinte saída:
• Número:
• Quadrado:
• Raiz quadrada:'''

def Entrada():
    try:
        num = float(input('Digite um número: '))
        return num
    except ValueError:
        print('Valor inválido.')
        return Entrada()
    
def Saida(num):
    print(f'Número: {num}')
    print(f'Quadrado: {num ** 2}')
    print(f'Raiz Quadrada: {num ** 0.5}')

def main():
    num = Entrada()
    Saida(num)

main()
