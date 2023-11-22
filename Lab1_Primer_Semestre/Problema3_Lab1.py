# Integrante 1 : Josue Loaiza- 2380741
# integrante 2: Jesús Dagua - 2379924
# integrante 3 : Felipe Calan - 2380642 

# Docente: Luis German Toro Pareja
# Grupo : 52
# Laboratorio 1

# Calculating sales values 

#Request Notable product data
#Start
Product = input("Enter the name of the Product: ")
Cost = float(input("Enter the Cost of the Product: "))

#Calculate the cost of the Product
#process
Revenue = float(Cost * 0.20)
Iva = float(Cost * (19/100))
Cost = float(Cost * (61/100))

#Print Product value
#Exit
print(f'''
Product: {Product}
IVA: {Iva}
Cost: {Cost}
Revenue: {Revenue}
''')

#End
