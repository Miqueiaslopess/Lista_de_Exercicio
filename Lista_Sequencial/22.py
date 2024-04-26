'''22)Entrar com a base e a altura de um retângulo e apresente a seguinte saída:
• Perímetro:
• Área:
• Diagonal:'''

def ObterEntrada():
    try:
        base = float(input('Digite a base do retângulo: '))
        altura = float(input('Digite a altura do retângulo: '))
        return base, altura
    except ValueError:
        print('Valor inválido.')
        return ObterEntrada()
    
def Perimetro(base, altura):
    return 2 * (base + altura)

def Area(base, altura):
    return base * altura

def Diagonal(base, altura):
    return (base ** 2 + altura ** 2) ** 0.5

def main():
    base, altura = ObterEntrada()
    print(f'Perímetro: {Perimetro(base, altura)}')
    print(f'Área: {Area(base, altura)}')
    print(f'Diagonal: {Diagonal(base, altura)}')

main()