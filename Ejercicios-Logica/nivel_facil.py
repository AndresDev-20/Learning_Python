"""
En esta sesión podras ver muchos ejerciciós de practica de un nivel
basico, de tal forma podremos empezar a dominar la logica de programación
con el lenguaje de python.
"""

#1. Concatena la cadena 'Treinta', 'Días', 'De', 'Python' en una sola
#cadena, 'Treinta días de Python'.
# Tu magia aqui:
world_one, world_two, world_three, world_four = "Treinta", "Dias", "De", "Python"
res = "{} {} {} {}".format(world_one, world_two, world_three, world_four)
print("- Respuesta del ejercicio 1: {}".format(res))



#2. Concatenar la cadena 'Codificación', 'Para', 'Todos'
# en una sola cadena, 'Codificación para todos'.
# Tu magia aqui:
one, two, three = 'Codificación', 'Para', 'Todos'
result = "{} {} {}".format(one, two, three)
print("- Respuesta del ejercicio 2: {}".format(result))



#3. Declare una variable llamada empresa y asígnele un valor 
#inicial "Codificación para todos".
# Tu magia aqui:
empresa = "Codificación para todos"



#4. imprima la variable empresa utilizando print() .
print("- Respuesta del ejercicio 3 y 4: "+empresa)



#5. Imprima la longitud de la cadena de la empresa utilizando el método len() y print().
res_len_empresa = len(empresa)
print("- Respuesta del ejercicio 5: Longitud de la variable empresa es {}".format(res_len_empresa))


#6. Cambie todos los caracteres a letras mayúsculas utilizando el método upper() .
res_upper_empresa = empresa.upper()
print("- Resapuesta del ejercicio 6: " + res_upper_empresa)


#7. Cambie todos los caracteres a letras minúsculas utilizando el método lower().
res_lower_empresa = res_upper_empresa.lower()
print("- Respuesta del ejercicio 7: " + res_lower_empresa)


#8. Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All.
