import numpy as np
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("400x400")
container = tk.Frame(window)
container.grid(row=0, column=0)
    
    
def mounth():
    average = {}
    for column in range(6):
        for row in range(1):
            mounth_column1 = matriz[row][column]
            mounth_column2 = matriz[row+1][column]
            mounth_column3 = matriz[row+2][column]
            count = 0
            count += mounth_column1+mounth_column2+mounth_column3
            average[column] = count
            print(mounth_column1)
    for i in range(len(average)):
        result_average = f"\n Promedio mes: {(average[i]/6)*2}\n"
        entry_control.insert(i,result_average)
        

def department():
    result_department = {}
    for column in range(6):
        for row in range(3):
            department_column1 = matriz[row][column]
            count = 0
            count += department_column1
            result_department[column] = count
            print(department_column1)
    for i in range(len(result_department)):
        result_department = f"""
        \n Promedio por departamento es: {(result_department[i])}\n
        """
        entry_control.insert(i,result_department)

def precipitation():
    pass


matriz = np.array(([[23.2,88.9,6.9,22.8,11.8,5.5],
                    [12.3,90.4,13.5,44.3,10.8,27.4],
                    [45.6,66.4,57.9,87.2,3.4,15.6]]))
print(matriz)

button_controlA = tk.Button(
    container,text="Promedio mes",command=mounth
    )
button_controlA.grid(row=0,column=1,pady=30,padx=140)

        

button_controlB = tk.Button(
container,text="Promedio departamento",command=department
    )
button_controlB.grid(row=1,column=1)


button_controlC = tk.Button(
container,text="Promedio precipitación",command=precipitation
    )
button_controlC.grid(row=2,column=1,pady=30)


entry_control = tk.Listbox(container)
entry_control.grid(row=3,column=1,ipadx=120,ipady=90)
    

window.mainloop()


    

