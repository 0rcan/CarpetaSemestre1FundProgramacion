# JOSUE JACINTO ZAMBRANO 2380741-3743
# CRUD
# My Project pharmacy
clients = ['Luis', 'Mateo',]  # variable of type string


def create_client(client_name):
    global clients
    if client_name not in clients:  # si no está el nombre, lo añado
        clients.append(client_name)
    else:
        print('\n Client already is in the Client\'s list')


# Devuelve la lista clintes al día.
def list_clients():  # enumerate
    global clients
    print(f"\n {line}List of clients{line}")
    for element, clients in enumerate(clients, 1):
        print("\n", element, clients, "\n")


def read_client(client_name):
    global clients
    while True:
        if client_name in clients:
            print(f"\n {line}Find user{line} \n\n --> {client_name}")
            break
        else:
            print(f"\n {line}Not find user{line}")
            client_name = input("\n Enter your name: ")


def update_client(client_name, update_client_name):
    global clients
    # i = 0
    while True:
        if client_name in clients:
            # Update a client
            index = clients.index(client_name)
            clients[index] = update_client_name
            print(f"""\n {line}Update Client{line}
            \n {client_name} --> {update_client_name}""")
            list_clients()
            break
            # for element in clients:
            #     if element == client_name:
            #         clients[i] = update_client_name
            #         if update_client == clients:
            #             break
            #     else:
            #         i+=1
            #         continue
            # list_clients()
        else:
            print(f"\n {line}Error103{line}\n")
            client_name = input("\n Enter your name: ").capitalize()
            update_client_name = input("""
            \n What is the update client name: """).capitalize()


def delete_client(client_name):
    global clients
    # i = 0
    while True:
        if client_name in clients:
            # Remove the client name and the trailing comma
            index = clients.index(client_name)
            clients.pop(index)
            print(f"""\n {line}Deleted Client{line}
            \n --x {client_name}""")
            list_clients()
            break
            # for element in clients:
            #         if element == client_name:
            #             clients.pop(i)
            #             if update_client == clients:
            #                 break
            #         else:
            #             i+=1
            #             continue
            # list_clients()
        else:
            print(f"\n {line}Client not found{line}\n")
            client_name = input("\n Enter your name: ").capitalize()


def _print_welcome():
    # clearConsole()
    print(f"\n {line}WELCOME TO PHARMACY UNIVALLE TULUÁ{line}")
    print(" What would you like to do today: ")
    print("\n [C]reate client o user")
    print(" [R]ead client o user")
    print(" [U]pdate client o user")
    print(" [D]elete client o user")


# def clearConsole():
#     return print("\n" * 150)


def _get_client_name():
    return input("\n Enter your name: ").capitalize()


if __name__ == '__main__':
    line = "="*10
    while True:
        _print_welcome()
        option = input("\n Type your activity: ").upper()
        if option == 'C':
            # se obtiene el nombre del cliente
            client_name = _get_client_name()
            # se envía el nombre del cliente para crear
            create_client(client_name)
            list_clients()
            break
        elif option == 'R':
            client_name = _get_client_name()
            read_client(client_name)
            # list_clients()
            break
        elif option == 'U':
            client_name = _get_client_name()
            update_client_name = input("""
            \n What is the update client name: """).capitalize()
            update_client(client_name, update_client_name)
            # list_clients()
            break
        elif option == 'D':
            client_name = _get_client_name()
            delete_client(client_name)
            # list_clients()
            break
        else:
            print("\n Invalid command")
