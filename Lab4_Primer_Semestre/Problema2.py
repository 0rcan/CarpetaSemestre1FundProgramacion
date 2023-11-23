def pay():  # Función
    # Siclo for en el rango de la cantidad de empleados ingresados
    for i in range(employee):
        # Dicionarios que almacenan las entradas
        identity = {}
        name = {}
        salary = {}

        name_employee = input("\n Ingrese nombre: ")  # Entrada
        name[i] = name_employee  # Se envia la entrada al dicionario
        # Siclo para los try excepts
        while True:
            try:
                identity_employee = int(input(
                    "\n Ingrese documento de identidad: "  # Entrada
                ))
                identity[i] = identity_employee

                while True:
                    # Siclo anidado para tener
                    # try excepts independientes
                    try:
                        False
                        salary_employee = float(input(
                            " Ingrese el salario basico: "  # Entrada
                        ))
                        # Se envia la entrada al dicionario
                        salary[i] = salary_employee
                        False
                        break  # Detiene el siclo mas anidado
                    except ValueError:
                        print(f"\n {line}ERROR, USE NUMEROS{line}")
                        continue
                break  # Detiene el siclo while principal
            except ValueError:
                print(f"\n {line}ERROR, USE NUMEROS{line}")
                continue
    # Se imprime la salida con un for para pasar por cada dato
    # de las listas en orden
    for e in range(employee):
        # Variables para resumir operaciones
        total_pay = salary[e]+salary[e]*0.10+salary[e]*0.20
        total_discount = salary[e]*0.04+salary[e]*0.04+salary[e]*0.05
        # Salida final
        print(f"""\n {line}DATOS DEL EMPLEADO{line}
 Nombre: {name[e]}
 Documento: {identity[e]}
 
 {line}PAGOS{line}           
 salario: {salary[e]}
 Bonificación de servicios: {salary[e]*0.10}
 Subcidio transporte: {salary[e]*0.20}
 
 {line}DESCUENTOS{line}  
 Salud: {salary[e]*0.04}
 Pensión: {salary[e]*0.04}
 Retefuente: {salary[e]*0.05}
 
 {line}TOTALES{line}  
 Total pagos: {total_pay}
 Total descuento: {total_discount}
 Neto a pagar: {total_pay - total_discount}
            """)


if __name__ == '__main__':  # Entry point
    line = "=" * 20
    print(f"\n {line}Bienvenid@ a la calculadora de pago neto{line}")
    # Siclo con try except si se cumple, para y ejecuta la función
    while True:
        try:
            employee = int(input(  # Pide la cantidad de empleados
                "\n Ingrese el numero de empleados: "
            ))
            pay()
            False
            break
        # Si no ingresa un numero se ejecuta el execpt
        except ValueError:
            print(f"\n {line}ERROR, USE NUMEROS{line}")
            True
