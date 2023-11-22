# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# Docente: Luis Germán Toro Pareja
# Número de grupo: 52
# Censo Virtual

def census():  # Función
    # Entradas de datos
    name_boss = input(" Nombre: ")
    last_name_boss = input(" Apellido: ")
    date_of_birth_boss = input(" Fecha de nacimiento [00/00/0000]: ")
    city_of_birt_boss = input(" Ciudad de nacimiento: ")
    address_boss = input(" Dirección de residencia: ")
    # Diccionarios para guardar datos del for
    document = {}
    name = {}
    last_name = {}
    date_of_birth = {}
    kindship = {}

    for i in range(family_members_boss):  # siclo
        print(f"\n {line}INGRESE LOS DATOS DE SUS FAMILIARES{line}\n")
        print(f" {line}FAMILIAR{i+1}{line}\n")

        while True:  # Siclo anidado
            type_document = input(' [CC] o [TI]: ').upper()
            # Las entradas se almacenan en los diccionarios
            document[i] = type_document
            # Condición
            if type_document == "CC" or type_document == "TI":
                name_family = input(' Nombre: ')
                name[i] = name_family  # Pal dicionario
                last_name_family = input(' Apellido: ')
                last_name[i] = last_name_family  # Pal dicionario
                date_of_birth_family = input(
                    """ Fecha de nacimiento [00/00/0000]: """
                )
                date_of_birth[i] = date_of_birth_family  # Pal dicionario
                kindship_family = input(' Parentesco del familiar: ')
                kindship[i] = kindship_family  # Pal dicionario
                break  # Si se cumple la condición se detiene
            else:
                print("\n Ingrese solo [CC o TI]\n")
                continue  # Si se cumple el bucle se repite

    # Salida de datos obtenidos
    print(f"""\n {line}LISTA DEL CENSO{line}
        \n {line}CABEZA DE FAMILIA{line}
        \n Cantidad de familiares: {family_members_boss}
 Nombre: {name_boss}
 Segundo nombre: {last_name_boss}
 Tipo de documento: {type_document}
 Departamento de nacimiento: {department_boss}
 Fecha de nacimiento: {date_of_birth_boss}
 Ciudad de nacimiento: {city_of_birt_boss}
 Dirección: {address_boss}
        """)
    # el siclo recorre los dicionarios y imprime
    for e in range(0, family_members_boss):
        print(f""" {line}FAMILIAR{e+1}{line}
 Nombre: {name[e]}
 Segundo nombre: {last_name[e]}
 Tipo de documento: {document[e]}
 Fecha de nacimiento: {date_of_birth[e]}
 Parentesco del familiar: {kindship[e]}
            """)


if __name__ == "__main__":  # Entry point
    line = "="*10
    print(f"\n {line}BIENVENIDO AL CENSO VIRTUAL{line}\n")
    print(f" {line}JEFE DE HOGAR{line}\n")
    while True:  # Siclo
        try:  # Try except
            family_members_boss = int(input(
                " Cantidad de familiares: "
            ))
            False  # apaga el siclo si se cumple el Try
        except ValueError:
            print(f"""\n {line}ERROR{line}
            \n Ingrese un numero de familiares\n""")
            continue  # continua el siclo si se cumple el execept
        while True:  # Siclo anidado
            type_document = input(" [CC] o [TI]: ").upper()
            if type_document == "CC" or type_document == "TI":
                department_boss = str(input(
                    " Departamento de nacimiento: "
                ))
                census()  # Invoca función si se cumple la condición
                break  # Una vez todo se cumpla descanza el siclo aniado
            else:  # Si no se cumple la condición pasa lo siguiente
                print("\n Ingrese solo [CC] o [TI]\n")
                continue
        break  # Descanza el siclo principal
