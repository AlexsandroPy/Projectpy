
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


try:
    peso = float(input('Digite sua peso (Kg): '))
    altura = float(input('Digite seu altura (m): '))

    imc_resultado = calcular_imc(peso, altura)

    print(f'Seu IMC e de {imc_resultado:.1f}')
    if imc_resultado < 18.5:
        print('voce esta ABAIXO DO PESO ideal')
    elif 18.5 <= imc_resultado < 24.9:
        print('voce esta no peso ideal')
    elif 25 <= imc_resultado < 29.9:
        print('Voce esta ACIMA DO PESO ideal')
    elif 30 <= imc_resultado < 34.9:
        print('Voce esta com obecidade tipo I')
    elif 34.9 <= imc_resultado < 39.9:
        print('Voce esta com obesidade tipo II')
    else:
        print('voce esta com obesidade III (Morbida). Cuide da saude')
except:
    print('Digite valores correspondentes a peso e altura')
