#Variables
#la mejor practica es colocar las variables asi de esa forma en minuscula y si hay varias palabras usamos guion bajo para separar
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 19
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)


#Funciones del sistema
#str:
my_age = 19
print(my_age, type(my_age))
my_age_string = str(my_age)
print( my_age_string, type(my_age_string))


#Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Yeison", "Marroquin", "Andres.dev", 19
print("Me llamo", name, surname,". Mi edad es:", age,". Y mi alias es:", alias)

#Inputs
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)