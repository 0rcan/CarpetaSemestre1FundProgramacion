# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# Integrante2: PrimerNombre SegundoApellido – código2
# Integrante2: PrimerNombre SegundoApellido – código3

# Docente: Luis Germán Toro Pareja
# Número de grupo: 52
# Proyecto Final restaurante

import tkinter as tk
# Creacion de la Ventana
window = tk.Tk()
window.geometry("700x700")
window.title("Mi Restaurante")

text = tk.Label(window, text="Mi Restaurante")
text.configure(font=("arial", 17)) # Estilos del texto
text.grid(row=1, column=1) # .grid Imprime el elemento

button = tk.Button(window, text= "to register")
button.grid(row=4, column=7)

button2 = tk.Button(window, text= "log in")
button2.grid(row=5, column=7)

window.mainloop() # Permite mantener en siclo el programa