muito_abaixo = 17
abaixo = 18.5
normal = 25
acima = 30
grauI = 35
grauII = 40

def classificar(imc):
    if imc < muito_abaixo:
        print('muito_abaixo')
    elif imc < abaixo:
        print('abaixo')
    elif imc < normal:
        print('normal')
    elif imc < acima:
        print('acima')
    elif imc < grauI:
        print('grauI')
    elif imc < grauII:
        print('grauII')
    else:
        print('grauIII')

def result(peso, alt):
    imc = peso / (alt * alt)
    print(f'Seu IMC foi de: {imc}')
    classificar(imc)