'''24)Entrar com o lado de um quadrado e apresente:
• Perímetro:
• Área:
• Diagonal:'''

def ObterLado():
    try:
        lado = float(input('Digite o lado do quadrado: '))
        return lado
    except ValueError:
        print('Valor inválido.')
        return ObterLado()
    
def Perimetro(lado):
    return 4 * lado

def Area(lado):
    return lado ** 2

def Diagonal(lado):
    return lado * 2 ** 0.5

def main():
    lado = ObterLado()
    print(f'Perímetro: {Perimetro(lado)}')
    print(f'Área: {Area(lado)}')
    print(f'Diagonal: {Diagonal(lado)}')

main()