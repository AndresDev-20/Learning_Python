# Primera forma de importar modulos
import my_module

my_module.sum(12, 33, 55)
my_module.presentation("Andres", 20, "Software Engineer")


# Segunda forma de importar modulos
from my_module import sum, presentation

sum(99, 100, 20)
presentation("Alan", 30, "Políglota")


# Si usamos el import podemos importar modulos creados o tambien moddulos del sistema por ejemplo el potencias, sacar el Pi varias cosas para hacer con el lenguaje.
import math
print(math.pi)

# Renombracio:
from math import pi as number_Pi
print(number_Pi)