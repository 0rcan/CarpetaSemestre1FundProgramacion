# Creación de ventana
import tkinter as tk 
from tkinter import ttk

window_dishes = tk.Tk()
window_dishes.geometry("500x500")
window_dishes.title("Gestión de platos")

# Botones menu
container_button_dishes = tk.Frame(window_dishes)
container_button_dishes.grid(row=0, column=0)

pestañas = ttk.Notebook(window_dishes)
pestañas.grid(row=0,column=0)
pestaña1 = ttk.Frame(pestañas,width=500,height=500)
pestaña3 = ttk.Frame(pestañas)
pestañas.add(pestaña1,text="Titulo")
pestañas.add(pestaña3,text="Titulo2")
# Contenedor principal
main_container_dishes = tk.Frame(pestaña1)
main_container_dishes.grid(row=1, column=1)

# Titulo y logo
tittle_dishes = tk.Label(
    main_container_dishes, text="Mi Restaurante"
)
tittle_dishes.configure(
    font=("fuente_negrita",20)  # Estilos del texto
    ) 
# Imprime el elemento con determinada posición
tittle_dishes.grid(row=1, column=0)
# Logo
image_home = tk.PhotoImage(file="restaurante.png")
image_home = image_home.subsample(10)  # Tamaño de la imagen
lbl_image_home = tk.Label(
    main_container_dishes, image=image_home
).grid(
    row=2, column=0,pady=5
)

# Sub contenedor dentro del contenedor principal
sub_container_dishes = tk.Frame(main_container_dishes)

sub_container_dishes.grid(row=3, column=0, pady=15)
fuente_negrita = ("Arial", 13, "bold")
sub_container_dishes.configure(bg="#5E5C6C",padx=50)

# titulo de botones
text_dishes = tk.Label(
    sub_container_dishes, text="Gestión de platos",font=(
        "fuente_negrita",14
        ),bg="#5E5C6C",fg="#ffffff"
    )
text_dishes.grid(row=3, column=0)

# Botones gestión de platos
button_dishesD = tk.Button(
    sub_container_dishes, text="Agregar",bg="gray",fg="#ffffff" # Boton registro
)
button_dishesD.grid(row=4, column=0,pady=10)
button_dishesE = tk.Button(
    sub_container_dishes, text="Eliminar",bg="gray",fg="#ffffff" # Boton registro
)
button_dishesE.grid(row=5, column=0)
button_dishesF = tk.Button(
    sub_container_dishes, text="Actualizar",bg="gray",fg="#ffffff" # Boton registro
)
button_dishesF.grid(row=6, column=0,pady=10)

window_dishes.mainloop()  # Permite mantener en siclo el programa