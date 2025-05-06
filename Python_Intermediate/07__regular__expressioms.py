### Regular Expressions ###

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span() 
print(start, end) # <re.Match object; span=(0, 20), match='Esta es la lección'>
print(my_string[start:end])


print(re.match("Esta es la lección", my_other_string))
print(re.match("Esta es la lección", my_string))