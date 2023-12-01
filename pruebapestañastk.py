# Creación de ventana
import tkinter as tk 
from tkinter import ttk

window_dishes = tk.Tk()
window_dishes.geometry("500x500")
window_dishes.title("Gestión de platos")

# Pestañas
pestañas = ttk.Notebook(window_dishes)
pestañas.grid(row=0,column=0)
pestaña1 = ttk.Frame(pestañas,padding=125)
pestaña2 = ttk.Frame(pestañas)
pestaña3 = ttk.Frame(pestañas)

pestañas.add(pestaña1,text="Titulo")
pestañas.add(pestaña2,text="Titulo2")
pestañas.add(pestaña3,text="Titulo3")
# Contenedor principal
main_container_dishes = tk.Frame(pestaña1)
main_container_dishes.grid(row=1, column=1)


# Contenedor principal
main_container_dishes = tk.Frame(main_container_dishes)
main_container_dishes.grid(row=0, column=0)

# Titulo y logo
tittle_dishes = tk.Label(
    main_container_dishes, text="Mi Restaurante"
)
tittle_dishes.configure(
    font=("fuente_negrita",20)  # Estilos del texto
    ) 
# Imprime el elemento con determinada posición
tittle_dishes.grid(row=0, column=0)
# Logo
image_homeD = tk.PhotoImage(file="restaurante.png")
image_homeD = image_homeD.subsample(10)  # Tamaño de la imagen
lbl_image_homeD = tk.Label(
    main_container_dishes, image=image_homeD
).grid(
    row=2, column=0,pady=5
)

# Sub contenedor dentro del contenedor principal
sub_container_dishes = tk.Frame(main_container_dishes)

sub_container_dishes.grid(row=3, column=0, pady=15)
fuente_negrita = ("Arial", 13, "bold")
sub_container_dishes.configure(bg="#5E5C6C",padx=53)

# titulo de botones
text_dishes = tk.Label(
    sub_container_dishes, text="Gestión de platos",font=(
        "fuente_negrita",14
        ),bg="#5E5C6C",fg="#ffffff"
    )
text_dishes.grid(row=3, column=0)

# Botones gestión de platos
button_dishesA = tk.Button(
    sub_container_dishes, text="Agregar",bg="gray",fg="#ffffff" # Boton registro
)
button_dishesA.grid(row=4, column=0,pady=10)
button_dishesB = tk.Button(
    sub_container_dishes, text="Eliminar",bg="gray",fg="#ffffff" # Boton registro
)
button_dishesB.grid(row=5, column=0)
button_dishesC = tk.Button(
    sub_container_dishes, text="Actualizar",bg="gray",fg="#ffffff" # Boton registro
)
button_dishesC.grid(row=6, column=0,pady=10)



#========================================================================
#========================================================================
#========================================================================

# Contenedor principal
main_container_dishesB = tk.Frame(pestaña2)
main_container_dishesB.grid(row=0, column=0)

# Titulo y logo
tittle_dishesB = tk.Label(
    main_container_dishesB, text="Mi Restaurante"
)
tittle_dishesB.configure(
    font=("fuente_negrita",20)  # Estilos del texto
    ) 
# Imprime el elemento con determinada posición
tittle_dishesB.grid(row=0, column=0)
# Logo
image_homeE = tk.PhotoImage(file="restaurante.png")
image_homeE = image_homeE.subsample(10)  # Tamaño de la imagen
lbl_image_homeE = tk.Label(
    main_container_dishesB, image=image_homeE
).grid(
    row=2, column=0,pady=5
)

# Sub contenedor dentro del contenedor principal
sub_container_dishesB = tk.Frame(main_container_dishesB)

sub_container_dishesB.grid(row=3, column=0, pady=15)
font_boldB = ("Arial", 13, "bold")
sub_container_dishesB.configure(bg="#5E5C6C",padx=10)

# titulo de entradas
text_dishesB = tk.Label(
    sub_container_dishesB, text="Agregar platos",font=(
        "fuente_negrita",14
        ),bg="#5E5C6C",fg="#ffffff"
    )
text_dishesB.grid(row=3, columnspan=2, pady=7)

# Entradas
# Entrada nombres
name_dishes = tk.Label(
    sub_container_dishesB, text="Nombre",bg="#5E5C6C",fg="#ffffff"
    )
name_dishes.grid(row=4, column=0)
name_entry_dishes = tk.Entry(sub_container_dishesB)
name_entry_dishes.grid(row=5, column=0, pady=5,padx=15)

# Entrada precios
price_dishes = tk.Label(
    sub_container_dishesB, text="Precio",bg="#5E5C6C",fg="#ffffff"
    )
price_dishes.grid(row=4, column=1)
price_entry_dishes = tk.Entry(sub_container_dishesB)
price_entry_dishes.grid(row=5, column=1)

# Entrada descripción
description_dishes = tk.Label(
    sub_container_dishesB, text="Descripción",bg="#5E5C6C",fg="#ffffff"
    )
description_dishes.grid(row=6, column=0,pady=4)
description_entry_dishes = tk.Entry(sub_container_dishesB)
description_entry_dishes.grid(row=7, column=0)

# Entrada disponibilidad
availability_dishes = tk.Label(
    sub_container_dishesB, text="Disponibilidad",
    bg="#5E5C6C",fg="#ffffff"
    )
availability_dishes.grid(row=6, column=1,pady=4)
availability_entry_dishes = tk.Entry(sub_container_dishesB)
availability_entry_dishes.grid(row=7, column=1)

# Ttitulo botón
button_entry_dishes = tk.Button(
    sub_container_dishesB, text="Agregar",bg="gray",fg="#ffffff" # Boton registro
)
# Botón
button_entry_dishes.grid(row=8, columnspan=2, pady=20)


#========================================================================
#========================================================================
#========================================================================


# Contenedor principal
main_container_tableB = tk.Frame(pestaña3)
main_container_tableB.grid(row=0, column=0)

# Titulo y logo
tittle_dtableB = tk.Label(
    main_container_tableB, text="Mi Restaurante"
)
tittle_dtableB.configure(
    font=("fuente_negrita",20)  # Estilos del texto
    ) 
# Imprime el elemento con determinada posición
tittle_dtableB.grid(row=0, column=0)
# Logo
image_homeF = tk.PhotoImage(file="restaurante.png")
image_homeF = image_homeF.subsample(10)  # Tamaño de la imagen
lbl_image_homeE = tk.Label(
    main_container_tableB, image=image_homeF
).grid(
    row=2, column=0,pady=5
)

# Sub contenedor dentro del contenedor principal
sub_container_tableB = tk.Frame(main_container_tableB)

sub_container_tableB.grid(row=3, column=0, pady=15)
font_boldB = ("Arial", 13, "bold")
sub_container_tableB.configure(bg="#5E5C6C",padx=10)

# titulo de entradas
text_dtableB = tk.Label(
    sub_container_tableB, text="Agregar platos",font=(
        "fuente_negrita",14
        ),bg="#5E5C6C",fg="#ffffff"
    )
text_dtableB.grid(row=3, columnspan=2, pady=7)

# Entradas
# Entrada nombres
name_table = tk.Label(
    sub_container_tableB, text="Fecha",bg="#5E5C6C",fg="#ffffff"
    )
name_table.grid(row=4, column=0)
name_entry_table = tk.Entry(sub_container_tableB)
name_entry_table.grid(row=5, column=0, pady=5,padx=15)

# Entrada precios
price_dtable = tk.Label(
    sub_container_tableB, text="Hora",bg="#5E5C6C",fg="#ffffff"
    )
price_dtable.grid(row=4, column=1)
price_entry_dtable = tk.Entry(sub_container_tableB)
price_entry_dtable.grid(row=5, column=1)

# Entrada descripción
description_dtable = tk.Label(
    sub_container_tableB, text="Numero de personas",bg="#5E5C6C",fg="#ffffff"
    )
description_dtable.grid(row=6, column=0,pady=4)
description_entry_dtable = tk.Entry(sub_container_tableB)
description_entry_dtable.grid(row=7, column=0)

# Ttitulo botón
button_entry_table = tk.Button(
    sub_container_tableB, text="Agregar",bg="gray",fg="#ffffff" # Boton registro
)
# Botón
button_entry_table.grid(row=8, columnspan=2, pady=20)

window_dishes.mainloop() 

