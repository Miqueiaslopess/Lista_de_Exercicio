# 15)Entrar com um ângulo em graus e apresentar: seno, co-seno, tangente, secante, cosecante e co-tangente deste ângulo.
import math
try:
    angulo_graus = float(input("Digite o ângulo em graus: "))

    angulo_radianos = math.radians(angulo_graus)

    seno = math.sin(angulo_radianos)
    cosseno = math.cos(angulo_radianos)
    tangente = math.tan(angulo_radianos)
    secante = 1/math.cos(angulo_radianos)
    cosecante = 1/math.sin(angulo_radianos)
    cotangente = 1/math.tan(angulo_radianos)

    print("Seno: ", seno)
    print("Cosseno: ", cosseno)
    print("Tangente: ", tangente)
    print("Secante: ", secante)
    print("Cosecante: ", cosecante)
    print("Cotangente: ", cotangente)
except ValueError:
    print('Por favor, digite um valor númerico válido para o ângulo.')
except ZeroDivisionError:
    print('O ângulo não pode ser 0.')
    
