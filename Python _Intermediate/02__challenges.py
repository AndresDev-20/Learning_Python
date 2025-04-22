### Challenges ###

# 1)
""" 
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

 Tu magia Aqui 😼
"""
def fizzbuzz():
    for index in range(1, 101):
        if index % 5 == 0 and index % 3 == 0:
            print("fizzbuzz")
        elif index % 5 == 0:
            print("buzz")
        elif index % 3 == 0:
            print("fizz")
        else:
            print(index)
        
fizzbuzz()


# 2)
"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
 
 Tu magia Aqui 😼
"""

def is_anagram(word_one, word_two):
   order_one, order_two = word_one.upper(), word_two.upper()
   if order_one == order_two:
       return False
   
   return sorted(order_one) == sorted(order_two)
    
print(is_anagram("Hola", "Halo"))


# 3)
"""
 Escribe un programa que imprima los 50 primeros números de la sucesión
 de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesión de números en
   la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    prev = 0
    next = 1
    for index in range(0, 51):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()