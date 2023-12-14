import tkinter as tk

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Ventana Principal")

        self.btn_siguiente = tk.Button(master, text="Siguiente", command=self.abrir_ventana_siguiente)
        self.btn_siguiente.pack(pady=10)

    def abrir_ventana_siguiente(self):
        # Ocultar la ventana principal
        self.master.withdraw()

        # Crear la ventana siguiente
        ventana_siguiente = tk.Toplevel(self.master)
        VentanaSiguiente(ventana_siguiente, self)

class VentanaSiguiente:
    def __init__(self, master, ventana_principal):
        self.master = master
        self.ventana_principal = ventana_principal
        master.title("Ventana Siguiente")

        self.btn_volver = tk.Button(master, text="Volver", command=self.volver_a_ventana_anterior)
        self.btn_volver.pack(pady=10)

    def volver_a_ventana_anterior(self):
        # Mostrar la ventana principal
        self.ventana_principal.master.deiconify()

        # Cerrar la ventana actual
        self.master.destroy()

def main():
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
