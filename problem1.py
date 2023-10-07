#JOSUE JACINTO ZAMBRANO LOAIZA - 238074-3743

# Docente: Luis Germán Toro Pareja
# Número de grupo: 50
# Laboratorio 2 y 3

def data(weight, height):
    imc = weight / (height**2)
    return print(F"Your name is: {name} and your imc is: {imc}")


if __name__ == '__main__':
    name = input("enter your namer: ")
    weight = float(input("enter your weight in KG: "))
    height = float(input("enter your height in MTS: "))
    data(weight, height)