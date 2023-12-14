# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# JESUS ALERTO TUNUBALA DAGUA 2379924-3743
# DIEGO ANDRES BOLAÑOS 2379918-3743
#
# Docente: Luis Germán Toro Pareja
# Número de grupo: 52
# Proyecto Final restaurante

import tkinter as tk  # Importamos la libreria
from tkinter import ttk
from PIL import Image, ImageTk



    # ====================================VENTANA #2====================================
def register():
    # Enlazar pestañas a la pestañas base
    eyelashes_registerB = ttk.Frame(eyelashes_registerA)
    # Asignarle un nombre a cada pestaña
    eyelashes_registerA.add(eyelashes_registerB,text="Registro")
    
    # Contenedor principal
    main_container_register = tk.Frame(eyelashes_registerB)
    main_container_register.grid(row=1, column=1,padx=125,pady=50)

    # Titulo y logo

    tittle_register = tk.Label(
        main_container_register, text="Mi Restaurante"
    )

    tittle_register.configure(
        font=("font_bold",20) # Estilos del texto
    ) 
    # Imprime el elemento con determinada posición
    tittle_register.grid(row=0, column=0)

    lbl_image_home = tk.Label(
        main_container_register, image=image_home
    ).grid(
        row=1, column=0,pady=5
    )

    # Sub contenedor dentro del contenedor principal
    sub_container_register = tk.Frame(main_container_register)

    sub_container_register.grid(row=2, column=0, pady=15)
    sub_container_register.configure(bg="#122c4b",padx=50)

    # Titulo registrarse
    text_register = tk.Label(
        sub_container_register, text="Registrarse", font=(
            "font_bold",16
        ),bg="#122c4b",fg="#ffffff"
        )
    text_register.grid(row=1,column=0)

    # Entradas de inicio de sesión
    # Registrarse
    email_register = tk.Label(sub_container_register, text="Email")
    email_register.configure(
        bg="#122c4b",fg="#ffffff",font=("font_bold",12)
        )
    email_register.grid(row=2, column=0, pady=3)

    email_entry_register = tk.Entry(sub_container_register)
    email_entry_register.grid(row=3, column=0)

    password_register = tk.Label(
        sub_container_register, text="Contraseña"
        )
    password_register.configure(
        bg="#122c4b", fg="#ffffff",font=("font_bold",12)
        )
    password_register.grid(row=4, column=0)

    password_entry_register = tk.Entry(sub_container_register, show="*")
    password_entry_register.grid(row=5, column=0)

    confirm_register = tk.Label(
        sub_container_register, text="Confirmar Contraseña"
        )
    confirm_register.configure(
        bg="#122c4b", fg="#ffffff", font=("font_bold",12)
        )
    confirm_register.grid(row=6, column=0)

    confirm_entry_register = tk.Entry(sub_container_register, show="*")
    confirm_entry_register.grid(row=7, column=0)

    # Boton registrar
    button_register = tk.Button(
        sub_container_register, text="Registrar",bg="#1aaadd",
        fg="#ffffff",command=log_in
    )
    button_register.grid(row=8, column=0,pady=10)


    #====================================VENTANA #3====================================
def log_in():
    # Enlazar pestañas a la pestañas base
    eyelashes_log_in = ttk.Frame(eyelashes_registerA,)
    # Asignarle un nombre a cada pestaña
    eyelashes_registerA.add(eyelashes_log_in,text="Inicio sesión")
    
    # Se enlaza el reguistro a la pestaña
    frame1 = tk.Frame(eyelashes_log_in)
    frame1.grid(row=1, column=1,padx=125,pady=50)

    frame_gray = tk.Frame(frame1)

    frame_gray.grid(row=2, column=0, pady=15)
    source_in = ("Arial", 13, "bold")

    frame_gray.configure(bg="#122c4b", padx=11)
    textA = tk.Label(frame1, text="Mi Restaurante")
    textA.configure(font=("font_bold", 20))  # Estilos del texto
    textA.grid(row=0, column=0)  # Imprime el elemento con determinada posición
    lbl_image_home = tk.Label(frame1, image=image_home).grid(
        row=1, column=0, pady=5
    )  # Posicionamiento

    # Entradas de inicio de sesión

    texiz = tk.Label(frame_gray, text="", font=source_in,
        bd=2, width=5, height=1)
    texiz.configure(bg="#122c4b", fg="white")
    texiz.grid(row=0, column=0)

    texde = tk.Label(frame_gray, text="", font=source_in, 
        bd=2, width=5, height=1)
    texde.configure(bg="#122c4b", fg="white")
    texde.grid(row=0, column=2)

    textB = tk.Label(frame_gray, text="""Inicio Sesión""", 
        font=("font_bold", 16))
    textB.configure(bg="#122c4b", fg="#ffffff")
    textB.grid(row=0, column=1)

    textE = tk.Label(frame_gray, text="Email", font=("font_bold", 12))
    textE.configure(bg="#122c4b", fg="#ffffff")
    textE.grid(row=1, column=1)

    aentry = tk.Entry(frame_gray)
    aentry.grid(row=2, column=1)

    textC = tk.Label(frame_gray, text="Contraseña", font=("font_bold", 12))
    textC.configure(bg="#122c4b", fg="#ffffff")
    textC.grid(row=3, column=1)

    bentry = tk.Entry(frame_gray)
    bentry.grid(row=4, column=1)

    button_logC = tk.Button(frame_gray, text="Iniciar sesión",
        bg="#1aaadd", width=10, height=1,command=menu
        )
    button_logC.configure(fg="white")
    button_logC.grid(row=5, column=1, pady=20)

    # ====================================VENTANA #4====================================
def menu():
    # Enlazar pestañas a la pestañas base
    eyelashes_menu = ttk.Frame(eyelashes_registerA)
    # Asignarle un nombre a cada pestaña
    eyelashes_registerA.add(eyelashes_menu,text="Menu")
    
    # Contenedor principal
    main_container_menu = tk.Frame(eyelashes_menu)
    main_container_menu.grid(row=0, column=0,padx=125,pady=50)

    # Titulo y logo
    tittle_dishes = tk.Label(
        main_container_menu, text="Mi Restaurante"
    )
    tittle_dishes.configure(
        font=("font_bold",20)  # Estilos del texto
        ) 
    # Imprime el elemento con determinada posición
    tittle_dishes.grid(row=0, column=0)
    # Logo
    lbl_image_home = tk.Label(
        main_container_menu, image=image_home
    ).grid(
        row=2, column=0,pady=5
    )

    # Sub contenedor dentro del contenedor principal
    sub_container_menu = tk.Frame(main_container_menu)

    sub_container_menu.grid(row=3, column=0, pady=15)
    sub_container_menu.configure(bg="#122c4b",padx=74)

    # titulo de botones
    text_menu = tk.Label(
        sub_container_menu, text="Bienvenido",font=(
            "font_bold",14
            ),bg="#122c4b",fg="#ffffff"
        )
    text_menu.grid(row=3, column=0)

    # Botones gestión
    button_menuA = tk.Button(
        sub_container_menu, 
        text="Gestión de platos",bg="#1aaadd",fg="#ffffff",
        command=management_dishes
    )
    button_menuA.grid(row=4, column=0,pady=10)
    button_menuB = tk.Button(
        sub_container_menu, 
        text="Gestión de mesas",bg="#1aaadd",fg="#ffffff",
        command=management_tables
    )
    button_menuB.grid(row=5, column=0)
    button_menuC = tk.Button(
        sub_container_menu, text="Gestión de pedidos",
        bg="#1aaadd",fg="#ffffff",command=management_orders
    )
    button_menuC.grid(row=6, column=0,pady=10)
    button_menuD = tk.Button(
        sub_container_menu, text="Cerrar sesión",
        bg="#1aaadd",fg="#ffffff" 
    )
    button_menuD.grid(row=7, column=0,pady=10)

    # ====================================SUB-VENTANA Gestión de platos #3====================================
    # ====================================SUB-VENTANA Gestión de platos #3====================================
    # ====================================SUB-VENTANA Gestión de platos #3====================================
def management_dishes():
    # Enlazar pestañas a la pestañas base
    eyelashes_dish_management = ttk.Frame(eyelashes_registerA)
    # Asignarle un nombre a cada pestaña
    eyelashes_registerA.add(
        eyelashes_dish_management,text="Gestión de platos"
        )
    def update():
        button_dishesA.destroy()
        button_dishesB.destroy()
        button_dishesC.destroy() 
        
        # Contenedor principal
        main_container_dishes_update = tk.Frame(eyelashes_dish_management)
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
        
        # Se crea la tabla y se le asigna el nombre de la pestaña
        # Tambien le da como especie de identificador a cada columna
        table_dishes_update = ttk.Treeview(sub_container_dishesB_update,
            columns=(
            'Nombre', 'Precio', 'Descripción', 'Disponibilidad'
            ), show='headings'
            )
        # Define el alto de la tabla
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

        # Se crea el boton de eliminar actualizae
        delete_button_update = tk.Button(sub_container_dishesB_update, 
            text='Eliminar',bg="#cc21cc", fg="white"
            )
        update_button_update = tk.Button(sub_container_dishesB_update, 
            text='Actualizar',bg="#1aaadd", fg="white"
            )

        # Se imprimen los botones
        delete_button_update.grid(row=5, column=0,pady=15,padx=10)
        update_button_update.grid(row=5, column=0,columnspan=2,padx=10)


    # ====================================SUB-VENTANA Gestión de platos #2====================================
    # ====================================SUB-VENTANA Gestión de platos #2====================================
    # ====================================SUB-VENTANA Gestión de platos #2====================================

    def add():
        button_dishesA.destroy()
        button_dishesB.destroy()
        button_dishesC.destroy()
        
        main_container_dishes_add = tk.Frame(eyelashes_dish_management)
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

        # Entrada disponibilidad
        availability_dishes_add = tk.Label(
            sub_container_dishesB_add, text="Disponibilidad",
            bg="#122c4b",fg="#ffffff"
            )
        availability_dishes_add.grid(row=6, column=1,pady=4)
        availability_entry_dishes_add = tk.Entry(sub_container_dishesB_add)
        availability_entry_dishes_add.grid(row=7, column=1,padx=10)

        # Ttitulo botón
        button_entry_dishes_add = tk.Button(
            sub_container_dishesB_add, text="Agregar",bg="#1aaadd",fg="#ffffff" 
        )
        # Botón
        button_entry_dishes_add.grid(row=8, columnspan=2, pady=20)

        
    # ====================================VENTANA #5 Gestión de platos #1====================================

    # Contenedor principal
    main_container_dishes = tk.Frame(eyelashes_dish_management)
    main_container_dishes.grid(row=0, column=0,padx=125,pady=50)

    # Titulo y logo
    tittle_dishes = tk.Label(
        main_container_dishes, text="Mi Restaurante"
    )
    tittle_dishes.configure(
        font=("font_bold",20)  # Estilos del texto
        ) 
    # Imprime el elemento con determinada posición
    tittle_dishes.grid(row=0, column=0)
    
    # Logo
    lbl_image_home = tk.Label(
        main_container_dishes, image=image_home
    ).grid(
        row=2, column=0,pady=5
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

    # ====================================SUB-VENTANA Gestión de mesas #3====================================
    # ====================================SUB-VENTANA Gestión de mesas #3====================================
    # ====================================SUB-VENTANA Gestión de mesas #3====================================
def management_tables():
    # Enlazar pestañas a la pestañas base
    eyelashes_table = ttk.Frame(eyelashes_registerA)
    # Asignarle un nombre a cada pestaña
    eyelashes_registerA.add(eyelashes_table,text="Gestión de mesas")
    
    def tables_update():
        button_tablesA.destroy()
        button_tablesB.destroy()
        button_tablesC.destroy() 
        

        # Contenedor principal
        main_container_tables_update = tk.Frame(eyelashes_table)
        main_container_tables_update.grid(row=0, column=0,padx=5,pady=20)

        # Titulo y logo
        tittle_tables_update = tk.Label(
            main_container_tables_update, text="Mi Restaurante"
        )
        tittle_tables_update.configure(
            font=("font_bold",20)  # Estilos del texto
            )
        # Imprime el elemento con determinada posición
        tittle_tables_update.grid(row=0, column=0)

        # Sub contenedor dentro del contenedor principal
        sub_container_tablesB_update = tk.Frame(
            main_container_tables_update
            )
        sub_container_tablesB_update.grid(row=3, column=0, pady=15)
        sub_container_tablesB_update.configure(bg="#122c4b")

        # titulo de entradas
        text_tablesB_update = tk.Label(
            sub_container_tablesB_update, text="Platos",font=(
                "fuente_negrita",14
                ),bg="#122c4b",fg="#ffffff"
            )
        text_tablesB_update.grid(row=3, columnspan=2, pady=7)

        # Se actualiza el la poscición del Logo
        # Asi no desaparece
        lbl_image_home = tk.Label(
        main_container_tables_update, image=image_home
        ).grid(
            row=2, column=0,pady=5
        )
        
        # Se crea la tabla y se le asigna el nombre de la pestaña
        # Tambien le da como especie de identificador a cada columna
        table_tables_update = ttk.Treeview(sub_container_tablesB_update,
            columns=(
            'Mesa', 'Fecha', 'Hora', 'N.personas'), show='headings'
            )
        # Define el alto de la tabla
        table_tables_update.config(height=3)

        # Se define el ancho de las columnas y el centrado del contenido
        table_tables_update.column('Mesa', width=100,anchor='center')
        table_tables_update.column('Fecha', width=100,anchor='center')
        table_tables_update.column('Hora', width=170,anchor='center')
        table_tables_update.column('N.personas', width=100,anchor='center')

        # Declara que va a aser el head de la tabla y lo imprime
        table_tables_update.heading('Mesa', text='Mesa')
        table_tables_update.heading('Fecha', text='Fecha')
        table_tables_update.heading('Hora', text='Hora')
        table_tables_update.heading('N.personas', text='N.personas')

        # Se insertan los datos en la tabla en el orden del teeeview
        table_tables_update.insert('', 'end', 
            values=('1', '20/102023', '10:300', '8')
            )
        table_tables_update.insert('', 'end', 
            values=('2', '20/102023', '11:30', '5')
            )
        table_tables_update.insert('', 'end', 
            values=('3', '20/102023', '14:20', '3')
            )
        table_tables_update.insert('', 'end', 
            values=('4', '20/102023', '09:00', '9')
            )
        table_tables_update.insert('', 'end', 
            values=('5', '20/102023', '17:05', '2')
            )
        table_tables_update.insert('', 'end', 
            values=('6', '20/102023', '21:56', '7')
            )

        style_tables_update = ttk.Style()
        style_tables_update.configure("Treeview", rowheight=50)  

        # Se imprime la tabla
        table_tables_update.grid(row=4, column=0, columnspan=2,padx=10)

        # Se crea el boton de eliminar actualizae
        delete_button_update = tk.Button(
            sub_container_tablesB_update, text='Eliminar',
            bg="#cc21cc", fg="white"
            )
        update_button_update = tk.Button(
            sub_container_tablesB_update, text='Actualizar',
            bg="#1aaadd", fg="white"
            )

        # Se imprimen los botones
        delete_button_update.grid(row=5, column=0,pady=15,padx=10)
        update_button_update.grid(row=5, column=0,columnspan=2,padx=10)

    # ====================================SUB-VENTANA Gestión de mesas #2====================================
    # ====================================SUB-VENTANA Gestión de mesas #2====================================
    # ====================================SUB-VENTANA Gestión de mesas #2====================================

    def tables_add():
        button_tablesA.destroy()
        button_tablesB.destroy()
        button_tablesC.destroy()
        
        main_container_tables_add = tk.Frame(eyelashes_table)
        main_container_tables_add.grid(row=0, column=0,padx=105,pady=50)

            
        # Titulo y logo
        tittle_dishes_add = tk.Label(
            main_container_tables_add, text="Mi Restaurante"
        )
        tittle_dishes_add.configure(
            font=("font_bold",20)  # Estilos del texto
            ) 
        # Imprime el elemento con determinada posición
        tittle_dishes_add.grid(row=0, column=0)
        
        # Se actualiza el la poscición del Logo
        # Asi no desaparece
        lbl_image_home = tk.Label(
            main_container_tables_add, image=image_home
        ).grid(
            row=2, column=0,pady=5
        )
            
        # Sub contenedor dentro del contenedor principal
        sub_container_tablesB_add = tk.Frame(main_container_tables_add)

        sub_container_tablesB_add.grid(row=3, column=0, pady=15)
        sub_container_tablesB_add.configure(bg="#122c4b")

        # titulo de entradas
        text_tablesB_add = tk.Label(
            sub_container_tablesB_add, text="Agregar platos",font=(
                "fuente_negrita",14
                ),bg="#122c4b",fg="#ffffff"
            )
        text_tablesB_add.grid(row=3, columnspan=2, pady=7)

        # Entradas
        # Entrada nombres
        name_tables_add = tk.Label(
            sub_container_tablesB_add, text="Fecha",
            bg="#122c4b",fg="#ffffff"
            )
        name_tables_add.grid(row=4, column=0)
        name_entry_tables_add = tk.Entry(sub_container_tablesB_add)
        name_entry_tables_add.grid(row=5, column=0, pady=5,padx=15)

        # Entrada Fechas
        price_tables_add = tk.Label(
            sub_container_tablesB_add, text="Fecha",bg="#122c4b",
            fg="#ffffff"
            )
        price_tables_add.grid(row=4, column=1)
        price_entry_tables_add = tk.Entry(sub_container_tablesB_add)
        price_entry_tables_add.grid(row=5, column=1,padx=10)

        # Entrada Cantidad de personas
        description_tables_add = tk.Label(
            sub_container_tablesB_add, text="Número de personas",
            bg="#122c4b",fg="#ffffff"
            )
        description_tables_add.grid(row=6, column=0,pady=4)
        description_entry_tables_add = tk.Entry(sub_container_tablesB_add)
        description_entry_tables_add.grid(row=7, column=0)
        
        # Ttitulo botón
        button_entry_tables_add = tk.Button(
            sub_container_tablesB_add, text="Agregar",
            bg="#1aaadd",fg="#ffffff"
        )
        # Botón
        button_entry_tables_add.grid(row=8, columnspan=2, pady=20)

        


    # ====================================VENTANA #6 Gestión de mesas #1====================================

    # Contenedor principal
    main_container_tables = tk.Frame(eyelashes_table)
    main_container_tables.grid(row=0, column=0,padx=125,pady=50)

    # Titulo y logo
    tittle_tables = tk.Label(
        main_container_tables, text="Mi Restaurante"
    )
    tittle_tables.configure(
        font=("font_bold",20)  # Estilos del texto
        ) 
    # Imprime el elemento con determinada posición
    tittle_tables.grid(row=0, column=0)
    # Logo
    lbl_image_home = tk.Label(
        main_container_tables, image=image_home
    ).grid(
        row=2, column=0,pady=5
    )

    # Sub contenedor dentro del contenedor principal
    sub_container_tables = tk.Frame(main_container_tables)

    sub_container_tables.grid(row=3, column=0, pady=15)
    sub_container_tables.configure(bg="#122c4b",padx=50)

    # titulo de botones
    text_tables = tk.Label(
        sub_container_tables, text="Gestión de mesas",font=(
            "font_bold",14
            ),bg="#122c4b",fg="#ffffff"
        )
    text_tables.grid(row=3, column=0)

    # Botones gestión de platos
    button_tablesA = tk.Button(
        sub_container_tables, text="Agregar",bg="#1aaadd",
        fg="#ffffff",command=tables_add 
    )
    button_tablesA.grid(row=4, column=0,pady=10)
    button_tablesB = tk.Button(
        sub_container_tables, text="Eliminar",bg="#1aaadd",fg="#ffffff" 
    )
    button_tablesB.grid(row=5, column=0)
    button_tablesC = tk.Button(
        sub_container_tables, text="Actualizar",
        bg="#1aaadd",fg="#ffffff",command=tables_update
    )
    button_tablesC.grid(row=6, column=0,pady=10)

    # ====================================VENTANA #7 Gestión de pedidos #2====================================
    # ====================================VENTANA #7 Gestión de pedidos #2====================================
    # ====================================VENTANA #7 Gestión de pedidos #2====================================
def management_orders():
    # Enlazar pestañas a la pestañas base
    eyelashes_orders = ttk.Frame(eyelashes_registerA)
    # Asignarle un nombre a cada pestaña
    eyelashes_registerA.add(eyelashes_orders,text="Gestión de pedidos")
    
    def do():
        button_ordersA.destroy()
        button_ordersB.destroy()
        button_ordersC.destroy()
        # Contenedor principal
        main_container_orders_do = tk.Frame(eyelashes_orders)
        main_container_orders_do.grid(row=0, column=0,padx=80,pady=50)

        # Titulo y logo
        tittle_orders_do = tk.Label(
            main_container_orders_do, text="Mi Restaurante"
        )
        tittle_orders_do.configure(
            font=("font_bold",20)  # Estilos del texto
            ) 
        # Imprime el elemento con determinada posición
        tittle_orders_do.grid(row=0, column=0)
        
        lbl_image_home = tk.Label(
            main_container_orders_do, image=image_home
        ).grid(
            row=1, column=0,pady=5
        )

        # Sub contenedor dentro del contenedor principal
        sub_container_orders_do = tk.Frame(main_container_orders_do)
        sub_container_orders_do.grid(row=3, column=0, pady=5)
        sub_container_orders_do.configure(bg="#122c4b",padx=0)
        
        # titulo de botones
        text_orders_do = tk.Label(
        sub_container_orders_do, text="Realizar pedidos",font=(
            "font_bold",14
            ),bg="#122c4b",fg="#ffffff"
        )
        text_orders_do.grid(row=1,columnspan=3, pady=7,padx=100)

        # Se crea la tabla y se le asigna el nombre de la pestaña 
        # Se crea la tabla y se le asigna el nombre de la pestaña 
        # Se crea la tabla y se le asigna el nombre de la pestaña 
        table_orders_dishes_do = ttk.Treeview(sub_container_orders_do, columns=(
            'N.platos'), show='headings'
            )
        # Define el alto de la tabla en filas
        table_orders_dishes_do.config(height=3)

        # Se define el ancho de las columnas y el centrado del contenido
        table_orders_dishes_do.column('N.platos', width=100,anchor='center')


        # Declara que va a aser el head de la tabla y lo imprime
        table_orders_dishes_do.heading('N.platos', text='N.platos')

        # Se insertan los datos en la tabla en el orden del teeeview

        table_orders_dishes_do.insert('', 'end', values=('Plato2'))
        table_orders_dishes_do.insert('', 'end', values=('Plato3'))
        table_orders_dishes_do.insert('', 'end', values=('Plato4'))
        table_orders_dishes_do.insert('', 'end', values=('Plato5'))
        table_orders_dishes_do.insert('', 'end', values=('Plato6'))

        style = ttk.Style()
        style.configure("Treeview", rowheight=30)  

        # Se imprime la tabla
        table_orders_dishes_do.grid(row=2, column=0)

        # Se crea la segunda tabla
        # Se crea la segunda tabla
        # Se crea la segunda tabla
        table_orders_do = ttk.Treeview(sub_container_orders_do, columns=(
            'N.mesa'), show='headings'
            )
        # Define el alto de la tabla en filas
        table_orders_do.config(height=3)

        # Se define el ancho de las columnas y el centrado del contenido
        table_orders_do.column('N.mesa', width=100,anchor='center')


        # Declara que va a aser el head de la tabla y lo imprime
        table_orders_do.heading('N.mesa', text='N.mesa')

        # Se insertan los datos en la tabla en el orden del teeeview

        table_orders_do.insert('', 'end', values=('1'))
        table_orders_do.insert('', 'end', values=('2'))
        table_orders_do.insert('', 'end', values=('3'))
        table_orders_do.insert('', 'end', values=('4'))
        table_orders_do.insert('', 'end', values=('5'))

        style = ttk.Style()
        style.configure("Treeview", rowheight=30)  # Cambia '50' al tamaño que desees


        # Se imprime la tabla
        table_orders_do.grid(row=2, column=2,padx=5)

        # Se crea el boton de Realizar
        update_button_do = tk.Button(
            sub_container_orders_do, text='Realizar',bg="#1aaadd", fg="white"
            )

        # Se imprimen el botón
        update_button_do.grid(row=3, column=1,pady=10)


    # ====================================VENTANA #7 Gestión de pedidos #1====================================

    # Contenedor principal
    main_container_orders = tk.Frame(eyelashes_orders)
    main_container_orders.grid(row=0, column=0,padx=125,pady=50)

    # Titulo y logo
    tittle_orders = tk.Label(
        main_container_orders, text="Mi Restaurante"
    )
    tittle_orders.configure(
        font=("font_bold",20)  # Estilos del texto
        ) 
    # Imprime el elemento con determinada posición
    tittle_orders.grid(row=0, column=0)
    
    # Logo
    lbl_image_home = tk.Label(
        main_container_orders, image=image_home
    ).grid(
        row=2, column=0,pady=5
    )

    # Sub contenedor dentro del contenedor principal
    sub_container_orders = tk.Frame(main_container_orders)

    sub_container_orders.grid(row=3, column=0, pady=15)
    sub_container_orders.configure(bg="#122c4b",padx=44)

    # titulo de botones
    text_orders = tk.Label(
        sub_container_orders, text="Gestión de pedidos",font=(
            "font_bold",14
            ),bg="#122c4b",fg="#ffffff"
        )
    text_orders.grid(row=3, column=0)

    # Botones gestión de platos
    button_ordersA = tk.Button(
        sub_container_orders, text="Realizar",bg="#1aaadd",
        fg="#ffffff",command=do
    )
    button_ordersA.grid(row=4, column=0,pady=10)
    button_ordersB = tk.Button(
        sub_container_orders, text="Eliminar",bg="#1aaadd",
        fg="#ffffff" 
    )
    button_ordersB.grid(row=5, column=0)
    button_ordersC = tk.Button(
        sub_container_orders, text="Actualizar",bg="#1aaadd",
        fg="#ffffff" 
    )
    button_ordersC.grid(row=6, column=0,pady=10)

if __name__ == "__main__":
    
    # ====================================VENTANA #1====================================

    # def menu_r():
    # Creacion de la Ventana

    window_restaurant = tk.Tk()
    window_restaurant.geometry("515x450")
    window_restaurant.resizable(False,False)
    window_restaurant.title("Mi Restaurante")

    # Obtener la info de la altura de la ventana
    height = window_restaurant.winfo_reqheight()
    
    # Pestañas
    eyelashes_registerA = ttk.Notebook(window_restaurant)
    eyelashes_registerA.grid(row=0,column=0)

    # Enlazar pestañas a la pestañas base
    eyelashes_restaurant = ttk.Frame(eyelashes_registerA)
    
    # Asignarle un nombre a cada pestaña
    eyelashes_registerA.add(eyelashes_restaurant,text="Inicio")


    # Definición de la fuente
    font_bold = ("Arial", 13, "bold")

    # Contenedor principal
    container_main_home = tk.Frame(eyelashes_restaurant)
    container_main_home.grid(row=0, column=0,padx=86,pady=50)

    # Titulo
    text_home = tk.Label(container_main_home, text="Mi Restaurante")
    text_home.configure(font=("font_bold",20))  # Estilos del texto
    text_home.grid(
        row=1, column=1, # Imprime el elemento con determinada posición
    )

    # Imagen/Logo
    image_home = tk.PhotoImage(file="restaurante.png")
    image_home = image_home.subsample(10)  # Tamaño de la imagen
    lbl_image_home = tk.Label(container_main_home,image=image_home).grid(
        row=2, column=1,pady=5 # Posicionamiento
    )

    # Descripción del restaurante
    text_home = tk.Label(container_main_home, text="""
    Nuestro restaurante es un lugar donde ofrecemos una variedad
    de platos deliciosos y recursos culinarios para el público para
    satisfacer tus necesidades culinarias y hacerte 
    disfrutar de una experiencia gastronómica exepcional.
    """)

    # Estilos de la descripción
    text_home.configure(bg="#122c4b", fg="#ffffff")
    text_home.grid(row=3, column=1)

    # Botones registrarse
    button_home = tk.Button(
        container_main_home, text="Registrarse",bg="#1aaadd",
        fg="#ffffff",command=register
        )
    button_home.grid(row=4, column=1,pady=8)

    # Botones iniciar sesión
    button_home = tk.Button(
        container_main_home, text="Inicar sesión",
        bg="#1aaadd",fg="#ffffff",command=log_in
        )
    button_home.grid(row=5, column=1,)



    window_restaurant.mainloop()  # Permite mantener en siclo el programa