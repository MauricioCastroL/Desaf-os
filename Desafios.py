#Autor: Mauricio Castro L.
#Fecha: 28/10/24

def datos():
    peso = float(input('Ingrese su peso(kg): '))
    altura = float(input('Ingrese su altura(cm): '))
    altura = altura / 100
    return peso, altura

def calculo_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def intervalo_imc(imc):
    if (imc < 18.5):
        return 'Bajo peso'
    elif (18.5 <= imc < 24.9):
        return 'Normal'
    elif (25 <= imc < 29.9):
        return 'Sobrepeso'
    elif (imc > 30):
        return 'Obesidad'

def resultado(estado):
    print(f'Su estado es {estado}')

if __name__ == '__main__':
    peso, altura = datos()
    imc = calculo_imc(peso, altura)
    estado = intervalo_imc(imc)
    resultado(estado)
