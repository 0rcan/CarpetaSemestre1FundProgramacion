#JOSUE JACINTO ZAMBRANO LOAIZA - 238074-3743

# Docente: Luis Germán Toro Pareja
# Número de grupo: 50
# Laboratorio 2 y 3

def data(weight, height):
    imc = weight / (height**2)
    
    category = str
    
    if imc< 18.5:
        category = str("Infrapeso")
    elif 18.5<=imc<25.0:
        category = str("Normal")
    elif imc >= 25.0:
        category = str("SobrePeso")
        
    return print(F"""
Your name is: {name} 
and your imc is: {imc} your are in category: {category}
""")


if __name__ == '__main__':
    name = input("enter your namer: ")
    weight = float(input("enter your weight in KG: "))
    height = float(input("enter your height in MTS: "))
    data(weight, height)
    