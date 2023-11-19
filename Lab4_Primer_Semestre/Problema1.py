# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# Docente: Luis Germán Toro Pareja
# Número de grupo: 52
# Censo Virtual

def census():
    name = input(" Nombre: ")
    last_name = input(" Apellido: ")
    date_of_birth = input(" Fecha de nacimiento [00/00/0000]: ")
    city_of_birt = input(" Ciudad de nacimiento: ")
    address = input(" Dirección de residencia: ")
    kinship = ""

    for i in range(0, family_members):
        print(f"\n {line}Ingrese los datos de sus familiares{line}\n")
        print(f" {line}FAMILIAR{i}{line}\n")
        exec(f"type_document{i} = input(' [CC] o [TI]: ').upper()")
        if "type_document{i} == 'CC'" or "type_document{i} == 'TI'":
            exec(f"name{i} = input(' Nombre: ')")
            exec(f"last_name{i} = input(' Apellido: ')")
            exec(
                f"""date_of_birth{i} = 
                input(' Fecha de nacimiento [00/00/0000]:')
                """)
            exec(f"kindship{i} = input(' Parentesco del familiar ')")
        else:
            print("\n Ingrese solo [CC o TI]\n")


if __name__ == "__main__":
    line = "="*10
    print(f"\n {line}Bienvenido al censo virtual{line}\n")
    print(f" {line}Jefe de hogar{line}\n")
    while True:
        try:
            family_members = int(input(" Cantidad de familiares: "))
        except Exception:
            print(f"""\n {line}ERROR{line}
            \n Ingrese un numero de familiares\n""")
            continue
        while True:
            type_document = input(" [CC] o [TI]: ").upper()
            if type_document == "CC" or type_document == "TI":
                department = str(input(
                " Departamento de nacimiento: "
                ))
                census()
            else:
                print("\n Ingrese solo [CC] o [TI]\n")
                continue
            
    

