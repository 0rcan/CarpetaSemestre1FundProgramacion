# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# JESUS ALERTO TUNUBALA DAGUA 2379924-3743
# Integrante2: PrimerNombre SegundoApellido – código3
#
# Docente: Luis Germán Toro Pareja
# Número de grupo: 52
# Proyecto Final restaurante

import tkinter as tk  # Importamos la libreria

# ====================================VENTANA #1====================================

# def menu_r():
# Creacion de la Ventana
window_home = tk.Tk()
window_home.geometry("500x500")
window_home.title("Mi Restaurante")

container_main_home = tk.Frame(window_home)
container_main_home.grid(row=0, column=0,padx=80)

# Titulo
text_home = tk.Label(container_main_home, text="Mi Restaurante")
text_home.configure(font=("arial", 17))  # Estilos del texto
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

window_home.mainloop()  # Permite mantener en siclo el programa


# ====================================VENTANA #2====================================

# Creación de ventana
window_register = tk.Tk()
window_register.geometry("500x500")
window_register.title("Mi Restaurante")

# Botones menu
container_button_register = tk.Frame(window_register)
container_button_register.grid(row=0, column=0)

button_registerA = tk.Button(
    container_button_register, text="Inicio", width=8, height=1)
button_registerA.grid(row=0, column=1)
button_registerB = tk.Button(
    container_button_register, text="Inicio sesión", width=9, height=1)
button_registerB.grid(row=0, column=2)

# Contenedor principal
main_container_register = tk.Frame(window_register)
main_container_register.grid(row=1, column=1)

# Sub contenedor dentro del contenedor principal
sub_container_register = tk.Frame(main_container_register)

sub_container_register.grid(row=0, column=1, pady=30)
fuente_negrita = ("Arial", 13, "bold")
fuente_in = ("Arial", 13, "bold")
sub_container_register.configure(bg="#5E5C6C",padx=50)

# Titulo y logo

tittle_register = tk.Label(
    sub_container_register, text="Mi Restaurante"
)

tittle_register.configure(
    bg="#5E5C6C",font=fuente_negrita,fg="#ffffff"  # Estilos del texto
    ) 
# Imprime el elemento con determinada posición
tittle_register.grid(row=0, column=0)

image_home = tk.PhotoImage(file="restaurante.png")
image_home = image_home.subsample(10)  # Tamaño de la imagen
lbl_image_home = tk.Label(
    sub_container_register, image=image_home
).grid(
    row=1, column=0,pady=5
)

# Entradas de inicio de sesión
# Registrarse
email_register = tk.Label(sub_container_register, text="Email")
email_register.configure(bg="#5E5C6C", fg="#ffffff")
email_register.grid(row=2, column=0, pady=3)

email_entry_register = tk.Entry(sub_container_register)
email_entry_register.grid(row=3, column=0)

password_register = tk.Label(
    sub_container_register, text="Contraseña"
    )
password_register.configure(bg="#5E5C6C", fg="#ffffff")
password_register.grid(row=4, column=0)

password_entry_register = tk.Entry(sub_container_register, show="*")
password_entry_register.grid(row=5, column=0)

confirm_register = tk.Label(sub_container_register, text="Contraseña")
confirm_register.configure(bg="#5E5C6C", fg="#ffffff")
confirm_register.grid(row=6, column=0)

confirm_entry_register = tk.Entry(sub_container_register, show="*")
confirm_entry_register.grid(row=7, column=0)

# Boton registrar
button_registerC = tk.Button(
    sub_container_register, text="Registrar",bg="gray",fg="#ffffff" # Boton registro
)
button_registerC.grid(row=8, column=0,pady=10)

window_register.mainloop()  # Permite mantener en siclo el programa

# ====================================VENTANA #3====================================

window_log_in = tk.Tk()
window_log_in.geometry("500x500")
window_log_in.title("Mi Restaurante")

# Botones menu
framebutto = tk.Frame(window_log_in)
# framebutto.config(bd=1)
framebutto.grid(row=0, column=0)

butto_log = tk.Button(framebutto, text="Inicio", width=8, height=1)
butto_log.grid(row=0, column=1)
button_logB = tk.Button(
    framebutto, text="Inicio sesión", width=9, height=1
    )
button_logB.grid(row=0, column=2)
# boton invisiblle
# label_muerto = tk.Label(
#     window_log_in, text="", width=23, height=1, bd=2, relief="solid"
# )

# label_muerto.grid(row=0, column=2)

frame1 = tk.Frame(window_log_in)
frame1.grid(row=1, column=1)


framegris = tk.Frame(frame1)

framegris.grid(row=2, column=0, pady=30)
fuente_negrita = ("Arial", 13, "bold")
fuente_in = ("Arial", 13, "bold")
bg = "#5E5C6C"
framegris.configure(bg=bg)
textA = tk.Label(frame1, text="Mi Restaurante")
textA.configure(font=fuente_negrita)  # Estilos del texto
textA.grid(row=0, column=0)  # Imprime el elemento con determinada posición

image_home = tk.PhotoImage(file="restaurante.png")
image_home = image_home.subsample(10)  # Tamaño de la imagen
lbl_image_home = tk.Label(frame1, image=image_home).grid(
    row=1, column=0
)  # Posicionamiento

# Entradas de inicio de sesión

texiz = tk.Label(
    framegris, text="", font=fuente_in, bd=2, width=5, height=1
)
texiz.configure(bg=bg, fg="white")
texiz.grid(row=0, column=0)

texde = tk.Label(
    framegris, text="", font=fuente_in, bd=2, width=5, height=1
)
texde.configure(bg=bg, fg="white")
texde.grid(row=0, column=2)

textB = tk.Label(
    framegris, text="""Inicio Sesión""", font=fuente_negrita
)
textB.configure(bg=bg, fg="#ffffff")
textB.grid(row=0, column=1)


textE = tk.Label(framegris, text="Email", font=fuente_negrita)
textE.configure(bg=bg, fg="#ffffff")
textE.grid(row=1, column=1)

aentry = tk.Entry(framegris)
aentry.grid(row=2, column=1)

textC = tk.Label(framegris, text="Contraseña", font=fuente_negrita)
textC.configure(bg=bg, fg="#ffffff")
textC.grid(row=3, column=1)

bentry = tk.Entry(framegris)
bentry.grid(row=4, column=1)

button_logC = tk.Button(
    framegris, text="Iniciar sesión",
    font=fuente_negrita, bg="gray", width=10, height=1
)
button_logC.configure(fg="white")
button_logC.grid(row=5, column=1, pady=30)

window_log_in.mainloop()  # Permite mantener en siclo

# ====================================VENTANA #4====================================

# ====================================VENTANA #5====================================

