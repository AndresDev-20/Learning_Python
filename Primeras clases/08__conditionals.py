### Conditionals ###

# Primer ejemplo
my_condition = True
if my_condition:
    print("Se ejecutó el if")


# Segundo ejemplo con números
numbers = 4 * 3
if numbers == 12:
    print("Verdadero")


# Tercer ejemplo con else
car = "Red"
if car == "Red":
    print("El carro es rojo")
else:
    print("El carro no es de color rojo")


# Cuarto ejemplo con elif
edad = 18
if edad >= 18 and edad < 50:
    print("Pasaste a la fiesta 🎉")
elif edad < 18:
    print("Eres menor de edad, ve a dormir mejor 💤")
else:
    print("Eres demasiado viejo para entrar, ve a dormir 🤶💤")


# Condicional en una sola línea (ternario)
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print("Condicional en una línea:", mensaje)


# Condicional anidado
x = 10
if x > 5:
    if x < 15:
        print("x está entre 5 y 15")


# Ejemplo con operadores lógicos
a = 7
b = 12
if a > 5 and b < 15:
    print("Ambas condiciones se cumplen (a > 5 y b < 15)")

if a < 5 or b < 15:
    print("Al menos una condición se cumple (a < 5 o b < 15)")

if not a == 10:
    print("a no es igual a 10")


print("El sistema continúa 😼")

# NOTA:
# En Python la indentación (tabulación) es muy importante.
# Si no está indentado correctamente, el código puede dar error
# o salirse del bloque de la condición.
