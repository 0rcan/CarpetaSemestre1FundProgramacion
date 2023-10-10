#JOSUE JACINTO ZAMBRANO LOAIZA - 238074-3743

# Docente: Luis Germán Toro Pareja
# Número de grupo: 50
# Laboratorio 2 y 3

def data(weight, height): #[1] funtion defined whit 2 variables
    imc = weight / (height**2) #[2]operation of the vars of the funtion data]
    
    category = str #[3] the var category is create
    
    if imc< 18.5: #[4] a conditional it's created to assing a category
        category = str("Infrapeso")
    elif 18.5<=imc<25.0:
        category = str("Normal")
    elif imc >= 25.0:
        category = str("SobrePeso")
        
    return print(F"""
Your name is: {name}
and your imc is: {imc} your are in category: {category}
""")


if __name__ == '__main__': #[5] entrypoint create for ask the vars of the funtion
    name = input("enter your namer: ")
    weight = float(input("enter your weight in KG: "))#[6] get de data of the variables asking
    height = float(input("enter your height in MTS: "))
    data(weight, height) #[7] call the funtion together the variables for send the data to the funtion
    