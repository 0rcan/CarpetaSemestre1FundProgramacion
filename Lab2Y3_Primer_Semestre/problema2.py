#JOSUE JACINTO ZAMBRANO LOAIZA - 238074-3743

# Docente: Luis Germán Toro Pareja
# Número de grupo: 50
# Laboratorio 2 y 3

def data(age, mounths):

    if age < 12 and age > 0:
        category = "infant"
        value_mounth = 43000
    elif age >= 12 and age < 18:
        category = "young"
        value_mounth = 36000
    elif age >= 18 and age < 100:
        category = "senior"
        value_mounth = 32000
    
    return print(f"""
    Name: {name}
    Category: {category}
    Value to pay: {value_mounth * mounths}
    """)    
    
if __name__ == '__main__':
    name = input("\n Enter a name: ")
    age = int(input(" register your age: "))
    mounths = int(input(" Mounts of inscripcion: "))
    data(age, mounths)


