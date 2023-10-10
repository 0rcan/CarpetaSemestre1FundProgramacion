# Integrante 1 : Josue Loaiza- 2380741
# integrante 2: Jesús Dagua - 2379924
# integrante 3 : Felipe Calan - 2380642 

# Docente: Luis German Toro Pareja
# Grupo : 52
# Laboratorio 1

#program that calculates your weight on different planets

#start

weight_earth = float(input("Type your earth weight: "))             #input of variable        


Weight_Mars = float((weight_earth / 9.8) * 3.711)                    #process on mars
Weight_jupiter = float((weight_earth / 9.8) * 24.79)                 #process on jupiter
weight_moon = float((weight_earth / 9.8) * 1.622)                    #process on the moon


#result
print(f'''                             
    Your weight on Moon is:     {round(weight_moon,2)} 
    Your weight on Mars is:     {round(Weight_Mars,2)} 
    Your weight on Jupiter is:  {round(Weight_jupiter,2)} 
    ''')
#exit
