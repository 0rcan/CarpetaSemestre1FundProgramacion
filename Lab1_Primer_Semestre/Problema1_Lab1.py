# Integrante 1 : Josue Loaiza- 2380741
# integrante 2: Jesús Dagua - 2379924
# integrante 3 : Felipe Calan - 2380642 

# Docente: Luis German Toro Pareja
# Grupo : 52
# Laboratorio 1

# Recording film data

#Request and receive value of variables
#start
title= input("Enter the movie title: ") 
country = input("Enter the country of the movie: ") 
genre = input("Enter the genre of the movie: ")
duration = int(input("Enter the duration of the movie in minutes: ")) 
year = int(input("Enter the year of the movie: "))

#Printing variables in an orderly manner 
#process

print(f'''
        MOVIE DATA
        TITLE: {title} 
        COUNTRY: {country} 
        GENRE: {genre} 
        DURATION: {duration} minutes 
        YEAR: {year}''')

#end
