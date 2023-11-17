# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# JESUS ALERTO TUNUBALA DAGUA 2379924-3743
# Integrante2: PrimerNombre SegundoApellido – código2
# Integrante2: PrimerNombre SegundoApellido – código3
#
# Docente: Luis Germán Toro Pareja
# Número de grupo: 52
# Proyecto Final restaurante

import tkinter as tk

# def menu_r():

# Creacion de la Ventana
windowA = tk.Tk()
windowA.geometry("500x500")
windowA.title("Mi Restaurante")

imageA = tk.PhotoImage(file="restaurante.png")  # IMAGEN LOGO
lbl_imageA = tk.Label(image=imageA)


textA = tk.Label(windowA, text="Mi Restaurante")

textA.configure(font=("arial", 17))  # Estilos del texto
textA.place(
    relx=0.25, rely=0.1, relwidth=0.5
)  # Imprime el elemento con determinada posición

# Descripción del restaurante

textB = tk.Label(
    windowA,
    text="""Nuestro restaurante es un lugar donde ofrecemos una variedad 
de platos deliciosos y recursos culinarios para el público para 
satisfacer tus necesidades culinarias y hacerte 
disfrutar de una experiencia gastronómica exepcional.""",
)
textB.configure(bg="#5F25B4", fg="#ffffff")
textB.place(relx=0.16, rely=0.2, relheight=0.3, relwidth=0.7)


buttonA = tk.Button(windowA, text="Registrarse")  # boton
buttonA.place(relx=0.25, rely=0.6, relwidth=0.5)
##buttonA.config(round)

buttonB = tk.Button(windowA, text="Inicar sesión")
buttonB.place(relx=0.25, rely=0.7, relwidth=0.5)

windowA.mainloop()  # Permite mantener en siclo el programa
# josue
