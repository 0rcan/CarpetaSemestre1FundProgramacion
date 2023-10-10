# CRUD 
# My Project pharmacy
clients = 'Luis, Mateo,' # variable of type string
def create_client(client_name):
    global clients
    if client_name not in clients:# si no está el nombre, lo añado
        clients += client_name
    else:
        print('Client already is in the Client\'s list')

# Devuelve la lista clintes al día.
def list_clients():
    global clients
    print(clients)

def read_client(client_name):
    global clients
    if client_name in clients:
        print("Find user")
    else:
        print("not find user")

def update_client(name, update_name):
    global clients
    if name in clients:
        clients = clients.replace(name + ",",update_name+",")

    else:
        print("Error103")


def delete_client(client_name):
    global clients
    if client_name in clients:
        # Remove the client name and the trailing comma
        clients = clients.replace(client_name + ",", "")
        print(f"Deleted {client_name}")
    else:
        print("Client not found")

def _print_welcome():
    print("WELCOME TO PHARMACY UNIVALLE TULUÁ")
    print("*" * 60)
    print("What would you like to do today:")
    print("[C]reate client o user")
    print("[R]ead client o user")
    print("[U]pdate client o user")
    print("[D]elete client o user")


def _get_client_name():
    return input("Enter your name:")

if __name__ == '__main__':
    _print_welcome()
    option = input("Type your activity: ").upper()
    if option == 'C':
        client_name = _get_client_name() # se obtiene el nombre del cliente
        create_client(client_name) # se envía el nombre del cliente para crear
        list_clients()   
    elif option == 'R':
        client_name = _get_client_name()
        read_client(client_name)  
        list_clients() 
    elif option == 'U':
        client_name = _get_client_name()
        update_client_name = input("What is the update client name:")
        update_client(client_name, update_client_name)
        list_clients() 
        pass
    elif option == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
        pass
    else:
        print("Invalid command")