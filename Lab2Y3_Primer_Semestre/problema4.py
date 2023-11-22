#JOSUE JACINTO ZAMBRANO LOAIZA - 238074-3743

# Docente: Luis Germán Toro Pareja
# Número de grupo: 50
# Laboratorio 2 y 3

def fundamentos ():
    if calculation >= 0.0 and calculation < 2.0:
        category = "Bad"
    elif calculation >= 2.0 and calculation < 3.0:
        category = "Deficient"
    elif calculation >= 3.0 and calculation < 3.8:
        category = "Regular"
    elif calculation >= 3.8 and calculation < 4.5:
        category = "Good"
    elif calculation >= 4.5 and calculation <= 5.0:
        category = "Excelent"
    return print(f"""
        Student name: {estudent_name}
        Subject name= {subject_name} 
        Clasification= {category}
        """)
    
def calculoI ():
    if calculation >= 0.0 and calculation < 2.0:
        category = "Bad"
    elif calculation >= 2.0 and calculation < 3.0:
        category = "Deficient"
    elif calculation >= 3.0 and calculation < 3.5:
        category = "Regular"
    elif calculation >= 3.5 and calculation < 4.5:
        category = "Good"
    elif calculation >= 4.5 and calculation <= 5.0:
        category = "Excelent"
    return print(f"""
        Student name: {estudent_name}
        Subject name= {subject_name} 
        Clasification= {category}
        """)
def inglesI ():
    if calculation >= 0.0 and calculation < 3.0:
        category = "Bad"
    elif calculation >= 3.0 and calculation < 4.0:
        category = "Deficient"
    elif calculation >= 4.0 and calculation < 4.5:
        category = "Regular"
    elif calculation >= 4.5 and calculation <= 5.0:
        category = "Good"
    return print(f"""
        Student name: {estudent_name}
        Subject name= {subject_name} 
        Clasification= {category}
        """)
def deporte ():
    if calculation >= 0.0 and calculation < 3.0:
        category = "Bad"
    elif calculation >= 3.0 and calculation < 4.0:
        category = "Regular"
    elif calculation >= 4.0 and calculation <= 5.0:
        category = "Good"
    return print(f"""
        Student name: {estudent_name}
        Subject name= {subject_name} 
        Clasification= {category}
        """)
    
if __name__ == '__main__':
    estudent_name = input("\n Estudent name: ")
    subject_name = input(" Subject name: ")
    exam_partial1 = float(input(" Exam partial I: ")) #20
    homework1 = float(input(" Homework I: ")) #20
    homework2 = float(input(" Homework II: ")) #20
    final_exam = float(input(" Final exam: ")) #40
    share = float(input(" Share: ")) #20
    
    result1 = float((exam_partial1 * 0.2) + (homework1 * 0.1) + (homework2 * 0.1))
    result2 = float((final_exam * 0.4) + (share * 0.2))
    calculation = float(result1 + result2)
    
    if subject_name == "Fundamentos":
        fundamentos()
    elif subject_name == "CalculoI":
        calculoI()
    elif subject_name == "InglesI":
        inglesI()
    elif subject_name == "Deporte":
        deporte()
    else:
        print("""    
    *****************
    SUBJECT INCORRECT

    *****************
    """)