#JOSUE JACINTO ZAMBRANO LOAIZA - 238074-3743

# Docente: Luis Germán Toro Pareja
# Número de grupo: 50
# Laboratorio 2 y 3

def data(weight, height): #[1] funtion defined with 2 variables
    imc = weight / (height**2) #[2]operation of the vars of the funtion data]
    
    if imc< 18.5: #[3] a conditional it's created to assing a category
        category = str("Infrapeso") #[4] the var category is create
    elif 18.5<=imc<25.0:
        category = str("Normal")
    elif imc >= 25.0:
        category = str("SobrePeso")
        
    return print(F"""
    Pacient: {name}
    IMC: {imc} 
    Category: {category}
""")


if __name__ == '__main__': #[5] entrypoint create for ask the vars of the funtion
    name = input("\n Enter your name: ")
    weight = float(input(" Enter your weight in KG: "))#[6] get de data of the variables asking
    height = float(input(" Enter your height in MTS: "))
    data(weight, height) #[7] call the funtion together the variables for send the data to the funtion