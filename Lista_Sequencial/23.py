'''23)Entrar com o raio de um círculo e apresente a seguinte saída:
• Perímetro:
• Área:'''

def ObterRaio():
    try:
        raio = float(input('Digite o raio do círculo: '))
        return raio
    except ValueError:
        print('Valor inválido.')
        return ObterRaio()
    
def Perimetro(raio):
    return 2 * 3.14 * raio

def Area(raio):
    return 3.14 * raio ** 2

def main():
    raio = ObterRaio()
    print(f'Perímetro: {Perimetro(raio)}')
    print(f'Área: {Area(raio)}')

main()