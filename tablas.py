import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.geometry("600x400")
window.title("Mi Restaurante")

# Se crea el contenedor de la tabla
container = ttk.Frame(window)
container.grid(row=0, column=0)

# Se crea la tabla y se le agina el nombre de la pestaña junto con lo que yo 
table = ttk.Treeview(container, columns=(
    'Nombre', 'Precio', 'Descripción', 'Disponibilidad'), show='headings'
    )
# Define el alto de la tabla
table.config(height=6)

# Se define el ancho de las columnas y el centrado del contenido
table.column('Nombre', width=100,anchor='center')
table.column('Precio', width=100,anchor='center')
table.column('Descripción', width=170,anchor='center')
table.column('Disponibilidad', width=100,anchor='center')

# Declara que va a aser el head de la tabla y lo imprime
table.heading('Nombre', text='Nombre')
table.heading('Precio', text='Precio')
table.heading('Descripción', text='Descripción')
table.heading('Disponibilidad', text='Disponibilidad')

# Se insertan los datos en la tabla en el orden del teeeview
table.insert('', 'end', values=(
    'Pollo a la parrilla', 
    '$15.00', 
    """Pollo a la parrilla con una salsa 
    de limón y hierbas frescas. """,
    'Si'))
table.insert('', 'end', values=('Plato2', '$0.00', '13:30', 'No'))
table.insert('', 'end', values=('Plato3', '$0.00', '14:20', 'Si'))
table.insert('', 'end', values=('Plato4', '$0.00', '09:00', 'No'))
table.insert('', 'end', values=('Plato5', '$0.00', '17:05', 'Si'))
table.insert('', 'end', values=('Plato6', '$0.00', '21:56', 'Si'))

style = ttk.Style()
style.configure("Treeview", rowheight=50)  # Cambia '50' al tamaño que desees

# Se imprime la tabla
table.grid(row=0, column=0, columnspan=2)

# Se crea el boton de eliminar actualizae
delete_button = tk.Button(container, text='Eliminar',bg="#1cccdd", fg="white")
update_button = tk.Button(container, text='Actualizar',bg="#362d69", fg="white")

# Se imprimen los botones
delete_button.grid(row=1, column=0,pady=15)
update_button.grid(row=1, column=0,columnspan=2)





# container = ttk.Frame(window)
# container.grid(row=0, column=0)

# # Se crea la tabla y se le agina el nombre de la pestaña junto con lo que yo 
# table = ttk.Treeview(container, columns=(
#     'Nombre', 'Precio', 'Descripción', 'Disponibilidad'), show='headings'
#     )

# # Se define el ancho de las columnas y el centrado del contenido
# table.column('Nombre', width=50,anchor='center')
# table.column('Precio', width=100,anchor='center')
# table.column('Descripción', width=100,anchor='center')
# table.column('Disponibilidad', width=100,anchor='center')

# # Declara que va a aser el head de la tabla y lo imprime
# table.heading('Nombre', text='Nombre')
# table.heading('Precio', text='Precio')
# table.heading('Descripción', text='Descripción')
# table.heading('Disponibilidad', text='Disponibilidad')

# # Se insertan los datos en la tabla en el orden del teeeview
# table.insert('', 'end', values=('1', '20/10/2023', '10:00', '8'))
# table.insert('', 'end', values=('2', '20/10/2023', '13:30', '5'))
# table.insert('', 'end', values=('3', '20/10/2023', '14:20', '3'))
# table.insert('', 'end', values=('4', '20/10/2023', '09:00', '9'))
# table.insert('', 'end', values=('5', '20/10/2023', '17:05', '2'))
# table.insert('', 'end', values=('6', '20/10/2023', '21:56', '7'))

# # Se imprime la tabla
# table.grid(row=0, column=0, columnspan=2)



# # Create tabs
# tab_control = ttk.Notebook(window)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)
# tab3 = ttk.Frame(tab_control)

# tab_control.add(tab1, text='Inicio')
# tab_control.add(tab2, text='Menu')
# tab_control.add(tab3, text='Gestión Nombres')

# # Create table
# table = ttk.Treeview(tab3, columns=('Nombre', 'Precio', 'Descripción', 'Disponibilidad'), show='headings')
# table.column('Nombre', width=50, anchor='center')
# table.column('Precio', width=100, anchor='center')
# table.column('Descripción', width=100, anchor='center')
# table.column('Disponibilidad', width=100, anchor='center')
# table.heading('Nombre', text='Nombre')
# table.heading('Precio', text='Precio')
# table.heading('Descripción', text='Descripción')
# table.heading('Disponibilidad', text='Disponibilidad')

# # Insert data into table
# table.insert('', 'end', values=('1', '20/10/2023', '10:00', '8'))
# table.insert('', 'end', values=('2', '20/10/2023', '13:30', '5'))
# table.insert('', 'end', values=('3', '20/10/2023', '14:20', '3'))
# table.insert('', 'end', values=('4', '20/10/2023', '09:00', '9'))
# table.insert('', 'end', values=('5', '20/10/2023', '17:05', '2'))
# table.insert('', 'end', values=('6', '20/10/2023', '21:56', '7'))

# # Add buttons
# delete_button = tk.Button(tab3, text='Eliminar')
# update_button = tk.Button(tab3, text='Actualizar')
# delete_button.grid(row=1, column=0)

# # Pack everything
# table.pack(side='left', fill='both', expand=True)
# delete_button.pack(side='bottom', padx=10, pady=10)
# update_button.pack(side='bottom', padx=10, pady=10)
# tab_control.pack(expand=1, fill='both')

# Inserta una fila y guarda el ID

# id = table.insert('', 'end', values=('Pollo a la parrilla', '$15.00', 'Descripción', 'Si'))

# # Más tarde, actualiza la fila
# table.item(id, values=('Pollo a la parrilla', '$20.00', 'Descripción actualizada', 'No'))
# En este ejemplo, la fila con el ID guardado se actualiza para tener nuevos valores. Si quieres actualizar
# una fila específica, necesitarás guardar el ID de esa fila cuando la crees. Si no guardaste el ID de la 
# fila que quieres actualizar, tendrás que buscarlo. Puedes hacerlo recorriendo todas las filas de la tabla con 
# el método get_children y buscando la fila que quieres actualizar. Sin embargo, esto puede ser ineficiente si tienes muchas 
# filas. Es mejor guardar el ID de la fila cuando la creas si sabes que vas a querer actualizarla más tarde.

window.mainloop()
