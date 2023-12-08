import numpy as np
# # t = [[pisos ]habitaciones ] o [[y ] x]
# # t[y][x]

# # z = np.array([[3-i for i in range(3)] for j in range(2)])
# # print(z)

# t = np.array([[3-i for i in range(3)] for j in range(3)])
# print(t)
# s = 0
# x = 0
# for i in range(3):
#     s += t[i][x]
# print(i)
# print(s)


def transport():
    row = []
    column = []
    for i_row in range(row_range):
        route = input("\n Ingrese su ruta: ").upper()
        row.append(route)

        for i_column in range(1):
            people = int(input(
                f" Cantidad de personas de la ruta {route}: ")
            )
            column.append(people)
    matriz = np.array([row, column])
    print(f"\n {matriz}")
    # np.argmax(column) extrae la posicion del maximo elemento de la matriz
    print(f""" 
    \n Ruta: {row[np.argmax(column)]} \n Con: {max(column)} pasajeros
                        """)
    
    
if __name__ == '__main__':
    line = "="*10
    jump = "\n"
    row_range = 3
    welcome = print(
        f"\n {line}Bienvenido al sistema de transporte Tranzit{line}"
    )
    transport()
