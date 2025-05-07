### Regular Expressions ###

import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# Coincidencia al inicio (match)
match = re.match("Esta es la lección", my_string, re.I)
print(match)                          # Match si encuentra al inicio
start, end = match.span()             # Índices de inicio/fin del match
print(my_string[start:end])           # Texto encontrado

# Coincidencia al inicio en otro string
match = re.match("Esta no es la lección", my_other_string)
if match is not None:
    start, end = match.span()
    print(my_other_string[start:end])

# No encuentra porque "Expresiones Regulares" no está al inicio
print(re.match("Expresiones Regulares", my_string))

# search encuentra en cualquier parte
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall busca todas las coincidencias
findall = re.findall("lección", my_string, re.I)
print(findall)

# split divide por ":"
print(re.split(":", my_string))

# sub reemplaza "lección" por "LECCIÓN"
print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Algunos patrones importantes
pattern = r"[lL]ección"               # Coincide "lección" o "Lección"
pattern = r"[lL]ección|Expresiones"   # Coincide "lección", "Lección" o "Expresiones"
pattern = r"[0-9]"                    # Un solo dígito
pattern = r"\d"                       # Equivalente a [0-9]
pattern = r"\D"                       # Todo lo que NO es dígito
pattern = r"[l].*"                    # Desde la primera "l" hasta el final

# Validación de correo
email = "andres@mouredev.com.mx"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))



# Para aprender y validar expresiones regulares: https://regex101.com