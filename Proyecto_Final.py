# CRUD 
# My Project pharmacy
clients = ['Luis', 'Mateo',] # variable of type string
def create_client(client_name):
    global clients
    if client_name not in clients:# si no está el nombre, lo añado
        clients.append(client_name)
    else:
        print('\n Client already is in the Client\'s list')

# Devuelve la lista clintes al día.
def list_clients(): #enumerate
    global clients
    for element,clients in enumerate(clients,1):
        print("\n",element, clients,"\n")

def read_client(client_name):
    global clients
    for element in clients:
        if client_name == element:
            print(f"\n Find user \n {element}")
            break
        else:
            print(f"\n {line}Not find user{line}")
            break

def update_client(client_name, update_client_name):
    global clients
    i = 0
    if client_name in clients:
            for element in clients:
                if element == client_name:
                    clients[i] = update_client_name
                    if update_client == clients:
                        break
                else:
                    i+=1
                    continue
            list_clients()
    else:
        
        print(f"\n {line}Error103{line}\n")

def delete_client(client_name): ############
    global clients
    i = 0
    if client_name in clients:
        # Remove the client name and the trailing comma
        for element in clients:
                if element == client_name:
                    clients.pop(i)
                    if update_client == clients:
                        break
                else:
                    i+=1
                    continue
        list_clients()
    else:
        print(f"\n {line}Client not found{line}\n")

def _print_welcome():
    print("\n WELCOME TO PHARMACY UNIVALLE TULUÁ")
    print("*" * 60)
    print(" What would you like to do today: ")
    print("\n [C]reate client o user")
    print(" [R]ead client o user")
    print(" [U]pdate client o user")
    print(" [D]elete client o user")


def _get_client_name():
    return input("\n Enter your name: ")

if __name__ == '__main__':
    line = "="*10
    _print_welcome()
    option = input("\n Type your activity: ").upper()
    if option == 'C':
        client_name = _get_client_name() # se obtiene el nombre del cliente
        create_client(client_name) # se envía el nombre del cliente para crear
        list_clients()   
    elif option == 'R':
        client_name = _get_client_name()
        read_client(client_name)  
        #list_clients() 
    elif option == 'U':
        client_name = _get_client_name()
        update_client_name = input("\n What is the update client name: ")
        update_client(client_name, update_client_name)
        #list_clients()
        pass
    elif option == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        #list_clients()
        pass
    else:
        print("\n Invalid command")