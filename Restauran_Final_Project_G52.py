# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# JESUS ALERTO TUNUBALA DAGUA 2379924-3743
# Integrante2: PrimerNombre SegundoApellido – código3
#
# Docente: Luis Germán Toro Pareja
# Número de grupo: 52
# Proyecto Final restaurante

import tkinter as tk  # Importamos la libreria
from PIL import ImageTk, Image
# ====================================VENTANA #1====================================

# def menu_r():
# Creacion de la Ventana
window_home = tk.Tk()
window_home.geometry("500x500")
window_home.title("Mi Restaurante")

# Imagen/Logo
image_home = tk.PhotoImage(file="restaurante.png")
image_home = image_home.subsample(10)  # Tamaño de la imagen
lbl_image_home = tk.Label(image=image_home).place(
    relx=0.50, rely=0.17, anchor="center"  # Posicionamiento
)

# Titulo
text_home = tk.Label(window_home, text="Mi Restaurante")
text_home.configure(font=("arial", 17))  # Estilos del texto
text_home.place(
    relx=0.35, rely=0.05  # Imprime el elemento con determinada posición
)

# Descripción del restaurante
text_home = tk.Label(window_home, text="""
Nuestro restaurante es un lugar donde ofrecemos una variedad
de platos deliciosos y recursos culinarios para el público para 
satisfacer tus necesidades culinarias y hacerte 
disfrutar de una experiencia gastronómica exepcional.
""")
# Estilos de la descripción
text_home.configure(bg="#5E5C6C", fg="#ffffff")
text_home.place(relx=0.16, rely=0.25, relheight=0.3, relwidth=0.7)

# Botones registrarse
button_home = tk.Button(window_home, text="Registrarse")
button_home.place(relx=0.25, rely=0.6, relwidth=0.5)

# Botones iniciar sesión
button_home = tk.Button(window_home, text="Inicar sesión")
button_home.place(relx=0.25, rely=0.7, relwidth=0.5)

window_home.mainloop()  # Permite mantener en siclo el programa


# ====================================VENTANA #2====================================

# Creación ventana
window_register = tk.Tk()
window_register.geometry("500x500")
window_register.title("Registrarse")

# Contenedor A
container_registerA = tk.Frame(window_register)
container_registerA.grid(row=0,column=0)

# Botones menú
button_registerA = tk.Button( 
    container_registerA, text="Inicio" # Boton inicio
    )
button_registerA.grid(row=0,column=1)
button_registerB = tk.Button(
    container_registerA, text="Registro" # Boton registro
    )
button_registerB.grid(row=0,column=2)

# Contenedor B
container_registerB = tk.Frame(window_register)
container_registerB.grid(row=1,column=2,padx=80)
container_registerB.config(bg="#000000")

# Titulo
text_register = tk.Label(container_registerB, text="Mi Restaurante")
text_register.configure(font=("arial", 17))  # Estilos del texto
text_register.grid(row=0,column=0)

# Logo
# # Cargar imagen
# imagen_home = Image.open("restaurante.png")
# # Tamaño
# imagen_home = image_home.resize((100, 100), Image.ANTIALIAS)

# # Convertir la imagen de PIL a una imagen de Tkinter

# imagen_tk = ImageTk.PhotoImage(imagen_home)

# # Agregar la imagen a un widget de etiqueta
# panel = tk.Label(window_register, image=imagen_home)
# panel.grid(row=1, column=0)

# Registrarse
email_register = tk.Label(container_registerB, text="Email")
email_register.configure(bg="#5E5C6C", fg="#ffffff")
email_register.grid(row=2,column=0)

email_entry_register = tk.Entry(container_registerB)
email_entry_register.grid(row=3,column=0)

password_register = tk.Label(container_registerB, text="Contraseña")
password_register.configure(bg="#5E5C6C", fg="#ffffff")
password_register.grid(row=4,column=0)

password_entry_register = tk.Entry(container_registerB, show="*")
password_entry_register.grid(row=5,column=0)

confirm_register = tk.Label(container_registerB, text="Contraseña")
confirm_register.configure(bg="#5E5C6C", fg="#ffffff")
confirm_register.grid(row=6,column=0) 

confirm_entry_register = tk.Entry(container_registerB, show="*")
confirm_entry_register.grid(row=7,column=0)

# Boton registrar
button_registerC = tk.Button(
    container_registerB, text="Registrar" # Boton registro
    )
button_registerC.grid(row=8,column=0)

window_register.mainloop()  # Permite mantener en siclo el programa


# ====================================VENTANA #3====================================
window_log_in = tk.Tk()
window_log_in.geometry("500x500")
window_log_in.title("Mi Restaurante")

# Botones menú
button_logA = tk.Button(window_log_in, text="Inicio")
button_logA.place(x=0, y=0, relwidth=0.1)
button_logB = tk.Button(window_log_in, text="Inicio sesión")
button_logB.place(x=50, y=0, relwidth=0.2)

textA = tk.Label(window_log_in, text="Mi Restaurante")
textA.configure(font=("arial", 17))  # Estilos del texto
textA.place(
    relx=0.25, rely=0.1, relwidth=0.2
)  # Imprime el elemento con determinada posición

image_home = tk.PhotoImage(file="restaurante.png")
image_home = image_home.subsample(10)  # Tamaño de la imagen
lbl_image_home = tk.Label(image=image_home).place(
    relx=0.50, rely=0.17, anchor="center"
)  # Posicionamiento

# Entradas de inicio de sesión
textB = tk.Label(window_log_in, text="""Inicio Sesión""")
textB.configure(bg="#5E5C6C", fg="#ffffff")
textB.place(relx=0.15, rely=0.2, relheight=0.3, relwidth=0.7)

textE = tk.Label(window_log_in, text="Email")
textE.configure(bg="#5E5C6C", fg="#ffffff")
textE.place(relx=0.15, rely=0.4, relheight=0.1, relwidth=0.50)

aentry = tk.Entry(window_log_in)
aentry.place(relx=0.35, rely=0.5)

textC = tk.Label(window_log_in, text="Contraseña")
textC.configure(bg="#5E5C6C", fg="#ffffff")
textC.place(relx=0.15, rely=0.6, relheight=0.1, relwidth=0.50)

window_log_in.mainloop()  # Permite mantener en siclo
