# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# JESUS ALERTO TUNUBALA DAGUA 2379924-3743
# Integrante3: NO EXISTE :( 
#
# Docente: Luis Germán Toro Pareja
# Número de grupo: 52
# Proyecto Final restaurante

import tkinter as tk  # Importamos la libreria
from tkinter import ttk
# ====================================VENTANA #1====================================

# def menu_r():
# Creacion de la Ventana
window_restaurant = tk.Tk()
window_restaurant.geometry("500x500")
window_restaurant.title("Mi Restaurante")

# Pestañas
eyelashes_registerA = ttk.Notebook(window_restaurant)
eyelashes_registerA.grid(row=0,column=0)

# Enlazar pestañas a la pestañas base
eyelashes_restaurant = ttk.Frame(eyelashes_registerA)
eyelashes_registerB = ttk.Frame(eyelashes_registerA,padding=125)
eyelashes_log_in = ttk.Frame(eyelashes_registerA,padding=125)
eyelashes_menu = ttk.Frame(eyelashes_registerA,padding=125)
eyelashes_dish_managrment = ttk.Frame(eyelashes_registerA,padding=125)
eyelashes_table = ttk.Frame(eyelashes_registerA,padding=125)
eyelashes_orders = ttk.Frame(eyelashes_registerA,padding=125)

# Asignarle un nombre a cada pestaña
eyelashes_registerA.add(eyelashes_restaurant,text="Inicio")
eyelashes_registerA.add(eyelashes_registerB,text="Registro")
eyelashes_registerA.add(eyelashes_log_in,text="Inicio sesión")
eyelashes_registerA.add(eyelashes_menu,text="Menu")
eyelashes_registerA.add(
    eyelashes_dish_managrment,text="Gestión de platos"
    )
eyelashes_registerA.add(eyelashes_table,text="Gestión de mesas")
eyelashes_registerA.add(eyelashes_orders,text="Gestión de pedidos")

# Definición de la fuente
font_bold = ("Arial", 13, "bold")

# Contenedor principal
container_main_home = tk.Frame(eyelashes_restaurant)
container_main_home.grid(row=0, column=0,padx=86,pady=125)

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
text_home.configure(bg="#5E5C6C", fg="#ffffff")
text_home.grid(row=3, column=1)

# Botones registrarse
button_home = tk.Button(
    container_main_home, text="Registrarse",bg="gray",fg="#ffffff"
    )
button_home.grid(row=4, column=1,pady=8)

# Botones iniciar sesión
button_home = tk.Button(
    container_main_home, text="Inicar sesión",bg="gray",fg="#ffffff"
    )
button_home.grid(row=5, column=1,)

# ====================================VENTANA #2====================================

# Contenedor principal
main_container_register = tk.Frame(eyelashes_registerB)
main_container_register.grid(row=1, column=1)

# Titulo y logo

tittle_register = tk.Label(
    main_container_register, text="Mi Restaurante"
)

tittle_register.configure(
    font=("font_bold",20) # Estilos del texto
    ) 
# Imprime el elemento con determinada posición
tittle_register.grid(row=0, column=0)

image_homeA = tk.PhotoImage(file="restaurante.png")
image_homeA = image_homeA.subsample(10)  # Tamaño de la imagen
lbl_image_homeA = tk.Label(
    main_container_register, image=image_homeA
).grid(
    row=1, column=0,pady=5
)

# Sub contenedor dentro del contenedor principal
sub_container_register = tk.Frame(main_container_register)

sub_container_register.grid(row=2, column=0, pady=15)
sub_container_register.configure(bg="#5E5C6C",padx=50)

# Titulo registrarse
text_register = tk.Label(
    sub_container_register, text="Registrarse", font=(
        "font_bold",16
    ),bg="#5E5C6C",fg="#ffffff"
)
text_register.grid(row=1,column=0)

# Entradas de inicio de sesión
# Registrarse
email_register = tk.Label(sub_container_register, text="Email")
email_register.configure(
    bg="#5E5C6C",fg="#ffffff",font=("font_bold",12)
    )
email_register.grid(row=2, column=0, pady=3)

email_entry_register = tk.Entry(sub_container_register)
email_entry_register.grid(row=3, column=0)

password_register = tk.Label(
    sub_container_register, text="Contraseña"
    )
password_register.configure(
    bg="#5E5C6C", fg="#ffffff",font=("font_bold",12)
    )
password_register.grid(row=4, column=0)

password_entry_register = tk.Entry(sub_container_register, show="*")
password_entry_register.grid(row=5, column=0)

confirm_register = tk.Label(
    sub_container_register, text="Confirmar Contraseña"
    )
confirm_register.configure(
    bg="#5E5C6C", fg="#ffffff", font=("font_bold",12)
    )
confirm_register.grid(row=6, column=0)

confirm_entry_register = tk.Entry(sub_container_register, show="*")
confirm_entry_register.grid(row=7, column=0)

# Boton registrar
button_register = tk.Button(
    sub_container_register, text="Registrar",bg="gray",fg="#ffffff" # Boton registro
)
button_register.grid(row=8, column=0,pady=10)


# ====================================VENTANA #3====================================


# Se enlaza el reguistro a la pestaña

frame1 = tk.Frame(eyelashes_log_in)
frame1.grid(row=1, column=1)

frame_gray = tk.Frame(frame1)

frame_gray.grid(row=2, column=0, pady=15)
source_in = ("Arial", 13, "bold")
bg = "#5E5C6C"
frame_gray.configure(bg=bg, padx=11)
textA = tk.Label(frame1, text="Mi Restaurante")
textA.configure(font=("font_bold", 20))  # Estilos del texto
textA.grid(row=0, column=0)  # Imprime el elemento con determinada posición

image_homeB = tk.PhotoImage(file="restaurante.png")
image_homeB = image_homeB.subsample(10)  # Tamaño de la imagen
lbl_image_homeB = tk.Label(frame1, image=image_homeB).grid(
    row=1, column=0, pady=5
)  # Posicionamiento

# Entradas de inicio de sesión

texiz = tk.Label(frame_gray, text="", font=source_in, bd=2, width=5, height=1)
texiz.configure(bg=bg, fg="white")
texiz.grid(row=0, column=0)

texde = tk.Label(frame_gray, text="", font=source_in, bd=2, width=5, height=1)
texde.configure(bg=bg, fg="white")
texde.grid(row=0, column=2)

textB = tk.Label(frame_gray, text="""Inicio Sesión""", font=("font_bold", 16))
textB.configure(bg=bg, fg="#ffffff")
textB.grid(row=0, column=1)

textE = tk.Label(frame_gray, text="Email", font=("font_bold", 12))
textE.configure(bg=bg, fg="#ffffff")
textE.grid(row=1, column=1)

aentry = tk.Entry(frame_gray)
aentry.grid(row=2, column=1)

textC = tk.Label(frame_gray, text="Contraseña", font=("font_bold", 12))
textC.configure(bg=bg, fg="#ffffff")
textC.grid(row=3, column=1)

bentry = tk.Entry(frame_gray)
bentry.grid(row=4, column=1)

button_logC = tk.Button(frame_gray, text="Iniciar sesión", bg="gray", width=10, height=1)
button_logC.configure(fg="white")
button_logC.grid(row=5, column=1, pady=20)

# ====================================VENTANA #4====================================

# Contenedor principal
main_container_menu = tk.Frame(eyelashes_menu)
main_container_menu.grid(row=0, column=0)

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
image_homeE = tk.PhotoImage(file="restaurante.png")
image_homeE = image_homeE.subsample(10)  # Tamaño de la imagen
lbl_image_homeD = tk.Label(
    main_container_menu, image=image_homeE
).grid(
    row=2, column=0,pady=5
)

# Sub contenedor dentro del contenedor principal
sub_container_menu = tk.Frame(main_container_menu)

sub_container_menu.grid(row=3, column=0, pady=15)
sub_container_menu.configure(bg="#5E5C6C",padx=74)

# titulo de botones
text_menu = tk.Label(
    sub_container_menu, text="Bienvenido",font=(
        "font_bold",14
        ),bg="#5E5C6C",fg="#ffffff"
    )
text_menu.grid(row=3, column=0)

# Botones gestión de platos
button_menuA = tk.Button(
    sub_container_menu, text="Gestión de platos",bg="gray",fg="#ffffff" # Boton registro
)
button_menuA.grid(row=4, column=0,pady=10)
button_menuB = tk.Button(
    sub_container_menu, text="Gestión de mesas",bg="gray",fg="#ffffff" # Boton registro
)
button_menuB.grid(row=5, column=0)
button_menuC = tk.Button(
    sub_container_menu, text="Gestión de pedidos",
    bg="gray",fg="#ffffff" # Boton registro
)
button_menuC.grid(row=6, column=0,pady=10)
button_menuD = tk.Button(
    sub_container_menu, text="Cerrar sesión",bg="gray",fg="#ffffff" # Boton registro
)
button_menuD.grid(row=7, column=0,pady=10)

# ====================================VENTANA #5 Gestión de platos #1====================================

# Contenedor principal
main_container_dishes = tk.Frame(eyelashes_dish_managrment)
main_container_dishes.grid(row=0, column=0)

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
sub_container_dishes.configure(bg="#5E5C6C",padx=53)

# titulo de botones
text_dishes = tk.Label(
    sub_container_dishes, text="Gestión de platos",font=(
        "font_bold",14
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
# ====================================SUB-VENTANA Gestión de platos #2====================================

# ====================================SUB-VENTANA Gestión de platos #3====================================

# ====================================VENTANA #6 Gestión de mesas #1====================================

# Contenedor principal
main_container_table = tk.Frame(eyelashes_table)
main_container_table.grid(row=0, column=0)

# Titulo y logo
tittle_table = tk.Label(
    main_container_table, text="Mi Restaurante"
)
tittle_table.configure(
    font=("font_bold",20)  # Estilos del texto
    ) 
# Imprime el elemento con determinada posición
tittle_table.grid(row=0, column=0)
# Logo
image_homeD = tk.PhotoImage(file="restaurante.png")
image_homeD = image_homeD.subsample(10)  # Tamaño de la imagen
lbl_image_homeD = tk.Label(
    main_container_table, image=image_homeD
).grid(
    row=2, column=0,pady=5
)

# Sub contenedor dentro del contenedor principal
sub_container_table = tk.Frame(main_container_table)

sub_container_table.grid(row=3, column=0, pady=15)
sub_container_table.configure(bg="#5E5C6C",padx=50)

# titulo de botones
text_table = tk.Label(
    sub_container_table, text="Gestión de mesas",font=(
        "font_bold",14
        ),bg="#5E5C6C",fg="#ffffff"
    )
text_table.grid(row=3, column=0)

# Botones gestión de platos
button_tableA = tk.Button(
    sub_container_table, text="Agregar",bg="gray",fg="#ffffff" # Boton registro
)
button_tableA.grid(row=4, column=0,pady=10)
button_tableB = tk.Button(
    sub_container_table, text="Eliminar",bg="gray",fg="#ffffff" # Boton registro
)
button_tableB.grid(row=5, column=0)
button_tableC = tk.Button(
    sub_container_table, text="Actualizar",bg="gray",fg="#ffffff" # Boton registro
)
button_tableC.grid(row=6, column=0,pady=10)

# ====================================VENTANA #7 Gestión de pedidos #1====================================

# Contenedor principal
main_container_orders = tk.Frame(eyelashes_orders)
main_container_orders.grid(row=0, column=0)

# Titulo y logo
tittle_orders = tk.Label(
    main_container_orders, text="Mi Restaurante"
)
tittle_orders.configure(
    font=("font_bold",20)  # Estilos del texto
    ) 
# Imprime el elemento con determinada posición
tittle_table.grid(row=0, column=0)
# Logo
image_homeD = tk.PhotoImage(file="restaurante.png")
image_homeD = image_homeD.subsample(10)  # Tamaño de la imagen
lbl_image_homeD = tk.Label(
    main_container_orders, image=image_homeD
).grid(
    row=2, column=0,pady=5
)

# Sub contenedor dentro del contenedor principal
sub_container_orders = tk.Frame(main_container_orders)

sub_container_orders.grid(row=3, column=0, pady=15)
sub_container_orders.configure(bg="#5E5C6C",padx=50)

# titulo de botones
text_table = tk.Label(
    sub_container_orders, text="Gestión de pedidos",font=(
        "font_bold",14
        ),bg="#5E5C6C",fg="#ffffff"
    )
text_table.grid(row=3, column=0)

# Botones gestión de platos
button_tableA = tk.Button(
    sub_container_orders, text="Realizar",bg="gray",fg="#ffffff" # Boton registro
)
button_tableA.grid(row=4, column=0,pady=10)
button_tableB = tk.Button(
    sub_container_orders, text="Eliminar",bg="gray",fg="#ffffff" # Boton registro
)
button_tableB.grid(row=5, column=0)
button_tableC = tk.Button(
    sub_container_orders, text="Actualizar",bg="gray",fg="#ffffff" # Boton registro
)
button_tableC.grid(row=6, column=0,pady=10)

window_restaurant.mainloop()  # Permite mantener en siclo el programa