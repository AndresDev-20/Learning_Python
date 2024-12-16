## Tuples ##
# Las tuplas son muy similares a las listas, sin embargo las tuplas son inmutables ya que son constantes,
# pero tambien podemos pasar una tupla a una lista, a continuacion conoceremos todo sobre ellas.


# Definición

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (19, 1.77, "Andres", "Marroquin", "Bernal")
my_other_tuple = (19, 60, 30)

print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Bernal"))
print(my_tuple.index("Marroquin"))
print(my_tuple.index("Bernal"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "AndresDev"
my_tuple.insert(1, "Rojo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
