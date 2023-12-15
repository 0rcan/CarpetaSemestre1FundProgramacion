import tkinter as tk
from tkinter import ttk


def register_element():
    name = entrada_nombre.get()
    price = entrada_precio.get()
    description = entrada_description.get()
    disponibility = entrada_disponibilidad.get()

    if name and price and description and disponibility:
        new_element = [name, price, description, disponibility]
        table_dishes_update.insert("", tk.END, values=new_element)
        list_elements.append(new_element)  # Agregar el nuevo elemento a la lista
        actualizar_lista()

        # Limpiar las entradas después de registrar
        entrada_nombre.delete(0, tk.END)
        entrada_precio.delete(0, tk.END)
        entrada_description.delete(0, tk.END)
        entrada_disponibilidad.delete(0, tk.END)


lista_resultados = []


def actualizar_elemento():
    seleccion = lista_resultados.selection()
    if seleccion:
        indice = lista_resultados.index(seleccion[0])
        name = entrada_nombre.get()
        price = entrada_precio.get()
        description = entrada_description.get()
        disponibility = entrada_disponibilidad.get()

        if name and price and description and disponibility:
            new_element = [name, price, description, disponibility]
            table_dishes_update.item(indice, values=new_element)
            list_elements[
                indice
            ] = new_element  # Actualizar el elemento en la lista
            actualizar_lista()

def actualizar_lista():
    # Borra todos los elementos actuales en la tabla
    for i in table_dishes_update.get_children():
        table_dishes_update.delete(i)

    # Agrega los elementos actualizados a la tabla
    for elemento in list_elements:
        table_dishes_update.insert("", tk.END, values=elemento)


# Configuración de la window principal
window = tk.Tk()
window.title("Ventana de Registro")

# Lista para almacenar elementos registrados
list_elements = []

# Entradas de texto para ingresar nuevos elementos
entrada_nombre = tk.Entry(window)
entrada_nombre.pack(pady=5)

entrada_precio = tk.Entry(window)
entrada_precio.pack(pady=5)

entrada_description = tk.Entry(window)
entrada_description.pack(pady=5)

entrada_disponibilidad = tk.Entry(window)
entrada_disponibilidad.pack(pady=5)

# Botón para registrar elementos
boton_registrar = tk.Button(window, text="Registrar", command=register_element)
boton_registrar.pack(pady=5)

# Botón para actualizar elementos
boton_actualizar = tk.Button(window, text="Actualizar", command=actualizar_elemento)
boton_actualizar.pack(pady=5)

# Botón para eliminar elementos
boton_eliminar = tk.Button(window, text="Eliminar")
boton_eliminar.pack(pady=5)

# Tabla para mostrar los elementos registrados
table_dishes_update = ttk.Treeview(
    window,
    columns=("name", "price", "description", "disponibility"),
    show="headings",
)
table_dishes_update.heading("name", text="Nombre")
table_dishes_update.heading("price", text="Precio")
table_dishes_update.heading("description", text="Descripción")
table_dishes_update.heading("disponibility", text="Disponibilidad")
table_dishes_update.pack(pady=10)



def update():
    
    button_dishesA.destroy()
    button_dishesB.destroy()
    button_dishesC.destroy() 
    
    # Contenedor principal
    main_container_dishes_update = tk.Frame(window)
    main_container_dishes_update.grid(row=0, column=0,padx=5,pady=20)

    # Titulo y logo
    tittle_dishes_update = tk.Label(
        main_container_dishes_update, text="Mi Restaurante"
    )
    tittle_dishes_update.configure(
        font=("font_bold",20)  # Estilos del texto
        )
    # Imprime el elemento con determinada posición
    tittle_dishes_update.grid(row=0, column=0)

    # Sub contenedor dentro del contenedor principal
    sub_container_dishesB_update = tk.Frame(
        main_container_dishes_update
        )

    sub_container_dishesB_update.grid(row=3, column=0, pady=15)
    sub_container_dishesB_update.configure(bg="#122c4b")

    # titulo de entradas
    text_dishesB_update = tk.Label(
        sub_container_dishesB_update, text="Platos",font=(
            "fuente_negrita",14
            ),bg="#122c4b",fg="#ffffff"
        )
    text_dishesB_update.grid(row=3, columnspan=2, pady=7)

    # Se actualiza el la poscición del Logo
    # Asi no desaparece
    lbl_image_home = tk.Label(
    main_container_dishes_update, image=image_home
    ).grid(
        row=2, column=0,pady=5
    )
    
    # Se crea la tabla y se le asigna el name de la pestaña
    # Tambien le da como especie de identificador a cada columna
    table_dishes_update = ttk.Treeview(sub_container_dishesB_update,
        columns=(
        'Nombre', 'Precio', 'Descripción', 'Disponibilidad'
        ), show='headings'
        )
    # Define el alto de la tabla en filas
    table_dishes_update.config(height=3)

    # Se define el ancho de las columnas y el centrado del contenido
    table_dishes_update.column('Nombre', width=100,anchor='center')
    table_dishes_update.column('Precio', width=100,anchor='center')
    table_dishes_update.column('Descripción', width=170,
        anchor='center')
    table_dishes_update.column('Disponibilidad', 
        width=100,anchor='center')

    # Declara que va a aser el head de la tabla y lo imprime
    table_dishes_update.heading('Nombre', text='Nombre')
    table_dishes_update.heading('Precio', text='Precio')
    table_dishes_update.heading('Descripción', text='Descripción')
    table_dishes_update.heading('Disponibilidad', 
        text='Disponibilidad')

    # Se insertan los datos en la tabla en el orden del teeeview
    table_dishes_update.insert('', 'end', values=(
        'Pollo a la parrilla', 
        '$15.00', 
        """Pollo a la parrilla con una salsa 
        de limón y hierbas frescas. """,
        'Si'))
    table_dishes_update.insert('', 'end', 
        values=('Plato3', '$0.00', '14:20', 'Si')
        )
    table_dishes_update.insert('', 'end', 
        values=('Plato4', '$0.00', '09:00', 'No')
        )
    table_dishes_update.insert('', 'end', 
        values=('Plato5', '$0.00', '17:05', 'Si')
        )
    table_dishes_update.insert('', 'end', 
        values=('Plato6', '$0.00', '21:56', 'Si')
        )
    table_dishes_update.insert('', 'end', 
        values=('Plato6', '$0.00', '21:56', 'Si')
        )

    style_dishes_update = ttk.Style()
    # Cambia el alto de las filas de la tabla
    style_dishes_update.configure("Treeview", rowheight=50)  

    # Se imprime la tabla
    table_dishes_update.grid(row=4, column=0, columnspan=2,padx=10)

    # Elimina la fila seleccionada    
    def delete_selected():
        selected_item = table_dishes_update.selection()
        table_dishes_update.delete(selected_item)
        
    # Se crea el boton de eliminar actualizae
    delete_button_update = tk.Button(sub_container_dishesB_update, 
        text='Eliminar',bg="#cc21cc",
        fg="white",command=delete_selected
        )
    update_button_update = tk.Button(sub_container_dishesB_update, 
        text='Actualizar',bg="#1aaadd", fg="white"
        )

    # Se imprimen los botones
    delete_button_update.grid(row=5, column=0,pady=15,padx=10)
    update_button_update.grid(row=5, column=0,columnspan=2,padx=10)

def add():
        # Lista para almacenar elementos registrados
        list_elements = []
        
        
        button_dishesA.destroy()
        button_dishesB.destroy()
        button_dishesC.destroy()
        
        main_container_dishes_add = tk.Frame(window)
        main_container_dishes_add.grid(row=0, column=0,padx=105,pady=50)

            
        # Titulo y logo
        tittle_dishes_add = tk.Label(
            main_container_dishes_add, text="Mi Restaurante"
        )
        tittle_dishes_add.configure(
            font=("font_bold",20)  # Estilos del texto
            ) 
        # Imprime el elemento con determinada posición
        tittle_dishes_add.grid(row=0, column=0)
        
        # Se actualiza el la poscición del Logo
        # Asi no desaparece
        lbl_image_home = tk.Label(
            main_container_dishes_add, image=image_home
        ).grid(
            row=2, column=0,pady=5
        )
            
            
        # Sub contenedor dentro del contenedor principal
        sub_container_dishesB_add = tk.Frame(main_container_dishes_add)

        sub_container_dishesB_add.grid(row=3, column=0, pady=15)
        sub_container_dishesB_add.configure(bg="#122c4b")

        # titulo de entradas
        text_dishesB_add = tk.Label(
            sub_container_dishesB_add, text="Agregar platos",font=(
                "fuente_negrita",14
                ),bg="#122c4b",fg="#ffffff"
            )
        text_dishesB_add.grid(row=3, columnspan=2, pady=7)

        # Entradas
        # Entrada nombres
        name_dishes_add = tk.Label(
            sub_container_dishesB_add, text="Nombre",bg="#122c4b",
            fg="#ffffff"
            )
        name_dishes_add.grid(row=4, column=0)
        name_entry_dishes_add = tk.Entry(sub_container_dishesB_add)
        name_entry_dishes_add.grid(row=5, column=0, pady=5,padx=15)

        # Entrada precios
        price_dishes_add = tk.Label(
            sub_container_dishesB_add, text="Precio",bg="#122c4b",
            fg="#ffffff"
            )
        price_dishes_add.grid(row=4, column=1)
        price_entry_dishes_add = tk.Entry(sub_container_dishesB_add)
        price_entry_dishes_add.grid(row=5, column=1)

        # Entrada descripción
        description_dishes_add = tk.Label(
            sub_container_dishesB_add, text="Descripción",
            bg="#122c4b",fg="#ffffff"
            )
        description_dishes_add.grid(row=6, column=0,pady=4)
        description_entry_dishes_add = tk.Entry(sub_container_dishesB_add)
        description_entry_dishes_add.grid(row=7, column=0)

        # Entrada disponibility
        availability_dishes_add = tk.Label(
            sub_container_dishesB_add, text="Disponibilidad",
            bg="#122c4b",fg="#ffffff"
            )
        availability_dishes_add.grid(row=6, column=1,pady=4)
        availability_entry_dishes_add = tk.Entry(sub_container_dishesB_add)
        availability_entry_dishes_add.grid(row=7, column=1,padx=10)

        # Ttitulo botón
        button_entry_dishes_add = tk.Button(
            sub_container_dishesB_add, text="Agregar",bg="#1aaadd",
            fg="#ffffff",command=register_element
        )
        # Botón
        button_entry_dishes_add.grid(row=8, columnspan=2, pady=20)


if __name__ == "__main__":

    # ====================================VENTANA #5 Gestión de platos #1====================================
    window = tk.Tk()
    window.title("Mi Restaurante")
    window.geometry("600x600")
    # Contenedor principal
    main_container_dishes = tk.Frame(window)
    main_container_dishes.grid(row=0, column=0,padx=105,pady=50)

    # Titulo y logo
    tittle_dishes = tk.Label(
        main_container_dishes, text="Mi Restaurante"
    )
    tittle_dishes.configure(
        font=("font_bold",20)  # Estilos del texto
        ) 
    # Imprime el elemento con determinada posición
    tittle_dishes.grid(row=0, column=0)
    
    # Imagen/Logo
    image_home = tk.PhotoImage(file="restaurante.png")
    image_home = image_home.subsample(10)  # Tamaño de la imagen
    lbl_image_home = tk.Label(main_container_dishes,image=image_home).grid(
        row=2, column=1,pady=5 # Posicionamiento
    )

    # Sub contenedor dentro del contenedor principal
    sub_container_dishes = tk.Frame(main_container_dishes)

    sub_container_dishes.grid(row=3, column=0, pady=15)
    sub_container_dishes.configure(bg="#122c4b",padx=53)

    # titulo de botones
    text_dishes = tk.Label(
        sub_container_dishes, text="Gestión de platos",font=(
            "font_bold",14
            ),bg="#122c4b",fg="#ffffff"
        )
    text_dishes.grid(row=3, column=0)

    # Botones gestión de platos
    button_dishesA = tk.Button(
        sub_container_dishes, text="Agregar",bg="#1aaadd",
        fg="#ffffff",command=add
    )
    button_dishesA.grid(row=4, column=0,pady=10)
    button_dishesB = tk.Button(
        sub_container_dishes, text="Eliminar",bg="#1aaadd",
        fg="#ffffff"
    )
    button_dishesB.grid(row=5, column=0)
    button_dishesC = tk.Button(
        sub_container_dishes, text="Actualizar",bg="#1aaadd",
        fg="#ffffff",command=update
    )
    button_dishesC.grid(row=6, column=0,pady=10)



# Inicia el bucle principal
window.mainloop()



