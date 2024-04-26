# Calcule e apresente a média entre os números 8, 9 e 7.

def obterNumero():
    try:
        numero = int(input('Digite um número: '))
        return numero
    except ValueError:
        print('Valor inválido.')
        return obterNumero()
    
def Media(numero1, numero2, numero3):
    return (numero1 + numero2 + numero3) / 3

def main():
    numero1 = 8
    numero2 = 9
    numero3 = 7
    print(f'A média entre {numero1}, {numero2} e {numero3} é: {Media(numero1, numero2, numero3)}')

main()