#JOSUE JACINTO ZAMBRANO LOAIZA - 238074-3743

# Docente: Luis Germán Toro Pareja
# Número de grupo: 50
# Laboratorio 2 y 3

def data(age, mounths):
    category = str
    value_mounth = int
    if age < 12 and age > 0:
        category = str("infant")
        value_mounth = int(43000)
    elif age >= 12 and age < 18:
        category = str("young")
        value_mounth = int(36000)
    elif age >= 18 and age < 100:
        category = str("senior")
        value_mounth = int(32000)
    
    return print(f"""
    Name: {name}
    Category: {category}
    Value to pay: {value_mounth * mounths}
    """)    
    
if __name__ == '__main__':
    name = input("Enter a name: ")
    age = int(input("register your age: "))
    mounths = int(input("Mounts of inscripcion: "))
    data(age, mounths)


