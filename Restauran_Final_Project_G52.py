# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# JESUS ALERTO TUNUBALA DAGUA 2379924-3743
# Integrante2: PrimerNombre SegundoApellido – código3
#
# Docente: Luis Germán Toro Pareja
# Número de grupo: 52
# Proyecto Final restaurante

import tkinter as tk  # Importamos la libreria

# VENTANA #1
# def menu_r():
# Creacion de la Ventana
window_home = tk.Tk()
window_home.geometry("500x500")
window_home.title("Mi Restaurante")

# Imagen/Logo
image_home = tk.PhotoImage(file="restaurante.png")
image_home = image_home.subsample(10)  # Tamaño de la imagen
lbl_image_home = tk.Label(image=image_home).place(
    relx=0.50, rely=0.17, anchor="center" # Posicionamiento
)

text_home = tk.Label(window_home, text="Mi Restaurante")
text_home.configure(font=("arial", 17))  # Estilos del texto
text_home.place(
    relx=0.35, rely=0.05  # Imprime el elemento con determinada posición
)

# Descripción del restaurante
text_home = tk.Label(window_home,text="""
Nuestro restaurante es un lugar donde ofrecemos una variedad
de platos deliciosos y recursos culinarios para el público para 
satisfacer tus necesidades culinarias y hacerte 
disfrutar de una experiencia gastronómica exepcional.
""")
text_home.configure(bg="#5E5C6C", fg="#ffffff")
text_home.place(relx=0.16, rely=0.25, relheight=0.3, relwidth=0.7)


button_home = tk.Button(window_home, text="Registrarse")
button_home.place(relx=0.25, rely=0.6, relwidth=0.5)
# buttonA.config(round)

button_home = tk.Button(window_home, text="Inicar sesión")
button_home.place(relx=0.25, rely=0.7, relwidth=0.5)

window_home.mainloop()  # Permite mantener en siclo el programa

# VENTANA #2
window_register = tk.Tk()
window_register.geometry("500x500")
window_register.title("Registrarse")

#container = CTkFrame(window_register,bg ="#5E5C6C")

# Botones menú
button_register = tk.Button(window_register, text="Inicio")
button_register.place(x=0, y=0, relwidth=0.1)
button_registerbutton_register = tk.Button(window_register, text="Inicio sesión")
button_registerbutton_register.place(x=50, y=0, relwidth=0.2)

window_register.mainloop()  # Permite mantener en siclo el programa

#   VENTANA #3
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
