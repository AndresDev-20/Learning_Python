## Functions ##

 
### Functions ###

# Definición

def my_function() :
    print("This is mi function")

my_function()

# Función con parámetros de entrada/argumentos

def sum_numbers(n1, n2):
    print(n1 + n2)

sum_numbers(19, 20)
sum_numbers(1.9, 20)
sum_numbers("19", "20") # Concatena 1920 ya que son string lo que estamos mandando


# Función con parámetros de entrada/argumentos y retorno

def sum_two(a, b):
    res = a + b
    return res

print(sum_two(22, 22))
result = sum_two(23, 12)
print(result)


# Función con parámetros de entrada/argumentos por clave

def presentation(name, surname, age = 0):
    print(f"Hello mi name is {name} {surname} and I have {age} years old")

presentation("Andres", "Marroquin")
presentation("Andres", "Marroquin", 20)


# Función con parámetros de entrada/argumentos por defecto

def presentationDefect(name = "Yeison", surname = "Bernal", age = 20):
    print(f"Hello mi name is {name} {surname} and I have {age} years old")

presentationDefect("Andres", "Marroquin")
presentationDefect("Andres", "Marroquin", 20)
presentationDefect()

# Función con parámetros de entrada/argumentos arbitrarios -> en realidad con esto lo interpreta como una tupla

def print_text(*texts):
    for text in texts:
        print(text.upper())

print_text("hello", "name", "sos")