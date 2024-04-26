''' 18)Informe o saldo de uma aplicação e apresente o novo saldo, considerando o reajuste
de 1%. '''

def ObterSaldo():
    try:
        saldo = float(input('Digite o saldo da aplicação: '))
        return saldo
    except ValueError:
        print('Valor inválido.')
        return ObterSaldo()

def SaldoAjustado(saldo):
    return saldo * 1.01

def main():
    saldo = ObterSaldo()
    print(f'O novo saldo é: {SaldoAjustado(saldo)}')

main()