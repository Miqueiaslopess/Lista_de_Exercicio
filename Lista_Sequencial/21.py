'''21)Entrar com um nome e apresente:
• Todo nome:
• Primeiro caractere:
• Último caractere:
• Do primeiro até o terceiro:
• Quarto caractere:
• Todos menos o primeiro:
• Os dois últimos:'''

def ObterEntrada():
    try:
        nome = input('Digite um nome: ')
        return nome
    except ValueError:
        print('Valor inválido.')
        return ObterEntrada()
    
def PrimeiroCaractere(nome):
    return nome[0]

def UltimoCaractere(nome):
    return nome[-1]

def DoPrimeiroAoTerceiro(nome):
    return nome[:3]

def QuartoCaractere(nome):
    return nome[3]

def TodosMenosPrimeiro(nome):
    return nome[1:]

def DoisUltimos(nome):
    return nome[-2:]

def main():
    nome = ObterEntrada()
    print(f'Todo nome: {nome}')
    print(f'Primeiro caractere: {PrimeiroCaractere(nome)}')
    print(f'Último caractere: {UltimoCaractere(nome)}')
    print(f'Do primeiro ao terceiro: {DoPrimeiroAoTerceiro(nome)}')
    print(f'Quarto caractere: {QuartoCaractere(nome)}')
    print(f'Todos menos o primeiro: {TodosMenosPrimeiro(nome)}')
    print(f'Os dois últimos: {DoisUltimos(nome)}')

main()