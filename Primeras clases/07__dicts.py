### Dictionaries ###

# Definición
my_dict = dict()
my_other_dict = {}

print(type(my_dict))  # Verifica que my_dict es de tipo 'dict'
print(type(my_other_dict))  # Verifica que my_other_dict es de tipo 'dict'

my_other_dict = {"Nombre": "Yeison",
                 "Apellido": "Marroquin", "Edad": 19, 1: "Python"}

my_dict = {
    "Nombre": "Yeison",
    "Apellido": "Marroquin",
    "Edad": 19,
    "Lenguajes": {"Python", "Java", "JavaScript"},
    1: 1.80
}

print(my_other_dict)  # Imprime el diccionario my_other_dict
print(my_dict)  # Imprime el diccionario my_dict

# Búsqueda
print(my_dict[1])  # Obtiene el valor de la clave 1
print(my_dict["Nombre"])  # Obtiene el valor de la clave "Nombre"

print("Moure" in my_dict)  # Verifica si la clave "Moure" está en my_dict
print("Apellido" in my_dict)  # Verifica si la clave "Apellido" está en my_dict

# Inserción
my_dict["Calle"] = "Calle AndresDev"  # Inserta una nueva clave:valor
print(my_dict)

# Actualización
my_dict["Nombre"] = "Andres"  # Actualiza el valor de la clave "Nombre"
print(my_dict["Nombre"])
print(my_dict)

# Eliminación
del my_dict["Calle"]  # Elimina la clave "Calle"
print(my_dict)

value = my_dict.pop("Edad", "Clave no encontrada")  # Elimina la clave "Edad" y devuelve su valor
print(value)
print(my_dict)



# Otras operaciones

"""
Explicación de las operaciones nuevas:
1. my_dict.items(): Devuelve una lista de pares (clave, valor) como objetos dict_items.
2. my_dict.keys(): Devuelve una lista con solo las claves.
3. my_dict.values(): Devuelve una lista con solo los valores.
4. dict.fromkeys(): Crea un nuevo diccionario con claves de una lista, tupla u otro iterable, asignándoles un valor por defecto (o None si no se especifica).
5. dict.fromkeys(list(my_new_dict.values())).keys(): Remueve duplicados de los valores (convirtiéndolos en claves) y devuelve las nuevas claves.
6. tuple(my_new_dict): Convierte las claves del diccionario en una tupla.
7. set(my_new_dict): Convierte las claves del diccionario en un conjunto (set).
"""

# Muestra todos los elementos (clave, valor) como pares
print(my_dict.items())  # dict_items([...])

# Muestra solo las claves
print(my_dict.keys())  # dict_keys([...])

# Muestra solo los valores
print(my_dict.values())  # dict_values([...])

# Crear un diccionario con claves provenientes de una lista
my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)  # Crea un diccionario con las claves de my_list y valores None
print(my_new_dict)

# Crear un diccionario con claves y valores None usando tuplas
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

# Crear un diccionario con claves de otro diccionario (valores por defecto: None)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

# Crear un diccionario con claves de otro diccionario y un valor por defecto
my_new_dict = dict.fromkeys(my_dict, "AndresDev")
print(my_new_dict)

# Verificar el tipo de los valores en un diccionario
my_values = my_new_dict.values()
print(type(my_values))  # <class 'dict_values'>

# Convertir los valores del diccionario en una lista
print(list(my_new_dict.values()))

# Remover valores repetidos y convertirlos en claves de un nuevo diccionario
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))

# Convertir el diccionario en una tupla de claves
print(tuple(my_new_dict))

# Convertir el diccionario en un conjunto de claves
print(set(my_new_dict))
