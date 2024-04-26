'''19)Entrar com um número no formato CDU e apresentar invertido: UDC. (Exemplo: 123,
sairá 321). O número deverá ser armazenado em outra variável antes de ser
apresentado.'''

def ObterNumero():
    try:
        numero = int(input('Digite um número: '))
        return numero
    except ValueError:
        print('Valor inválido.')
        return ObterNumero()
    
def InverterNumero(numero):
    numero_invertido = (str(numero)[::-1])
    return numero_invertido 

def main():
    numero = ObterNumero()
    print(f'O número invertido é: {InverterNumero(numero)}')

main()