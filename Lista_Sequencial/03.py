'''3) Calcule e apresente o produto entre 28 e 43.'''

def obterNumero():
    try:
        numero = int(input('Digite um número: '))
        return numero
    except ValueError:
        print('Valor inválido.')
        return obterNumero()
    
def Produto(numero1, numero2):
    return numero1 * numero2

def main():
    numero1 = 28
    numero2 = 43
    print(f'O produto entre {numero1} e {numero2} é: {Produto(numero1, numero2)}')

main()