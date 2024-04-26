'''25)Entrar com os informacoes a, b e c de um paralelepípedo. Calcular e apresentar a diagonal.'''

def ObterEntrada():
    try:
        comprimento = float(input('Digite o comprimento do paralelepípedo: '))
        largura = float(input('Digite a largura do paralelepípedo: '))
        altura = float(input('Digite a altura do paralelepípedo: '))
        return comprimento, largura, altura
    except ValueError:
        print('Valor inválido, digite apenas números.')
        return ObterEntrada()
    
def Diagonal(comprimento, largura, altura):
    return (comprimento ** 2 + largura ** 2 + altura ** 2) ** 0.5

def main():
    comprimento, largura, altura = ObterEntrada()
    print(f'A diagonal do paralelepípedo é: {Diagonal(comprimento, largura, altura)}')

main()
