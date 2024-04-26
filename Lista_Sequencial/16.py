#16)Entrar com o número e a base em que se deseja calcular o logarítmo desse número e apresenta-lo.

def entrada():
    try:
        num = float(input("Digite o número: "))
        base = float(input("Digite a base: "))
        return num, base
    except ValueError:
        print("Digite apenas números")
        return entrada()
    
def logaritmo(num, base):
    return (num ** (1/base))

def main():
    num, base = entrada()
    print(f"O logaritmo de {num} na base {base} é {logaritmo(num, base)}")
    

main()

