import random  # Para generar numero aleatorio en un rango (-5, 15)


def successmultiplication():  # Función
    # dicionarios de almacenamiento
    question_numberA = {}
    question_numberB = {}
    answer_question = {}
    question = {}
    # for que sicla hasta el 12
    for i in range(12):
        # Generación de numeros aleatorios
        numberA = random.randrange(-5, 15)
        numberB = random.randrange(-5, 15)
        question_numberA[i] = numberA  # Se guarda
        question_numberB[i] = numberB  # Se guarda
        question[i] = numberA * numberB  # Se guarda

        while True:  # While dentro de for pora siclar los try excepts

            print(f"\n {line}Problema {i+1} {line}")
            print(f"\n Resuelva {numberA} * {numberB}")

            try:  # Si es diferente a un numero int sicla
                answer_number = int(
                    input("\n Ingrese su respuesta al problema: ")
                )
                answer_question[i] = answer_number
                False
                break
            except ValueError:
                print(f"""\n {line}Error{line}
                    *Ingrese solo numeros enteros, no decimales
                    *Tampoco debe ingresar letras""")
                continue
    # Salida de datos
    print(f"\n {line}Resuelto por: {name} {line}")
    for j in range(12):
        if question[j] == answer_question[j]:
            print(f"""\n {line}Solución {j+1} {line}\n
 {question_numberA[j]} * {question_numberB[j]} = {answer_question[j]} 
 {line}Correcto{line}
                """)
        else:
            print(f"""\n {line}Solución {j+1} {line}\n
 {question_numberA[j]} * {question_numberB[j]} = {answer_question[j]} 
 {line}Incorrecto{line}
                """)


if __name__ == '__main__':  # Entrey point
    line = "="*15
    # Bienvenida
    print(f"\n {line}Bienvenido a Multiplicacion verdadera{line} ")
    # Entrada del nombre
    name = input("\n Ingrese su nombre: ")
    successmultiplication()
