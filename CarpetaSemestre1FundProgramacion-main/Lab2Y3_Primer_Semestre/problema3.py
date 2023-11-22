#JOSUE JACINTO ZAMBRANO LOAIZA - 238074-3743

# Docente: Luis Germán Toro Pareja
# Número de grupo: 50
# Laboratorio 2 y 3

def  problem(x):

    if x <= 0:
        result = 8*(x**2)-6
    elif x > 0:
        result = (3*x)+5
        
    return print(f"\n f( {round(x)} ) = {round(result)}\n")


if __name__ == '__main__':
    x = float(input("\n Enter a number for x: "))
    problem(x)