#1.Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
#  - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  - NO hace falta comprobar que ambas palabras existan.
#  - Dos palabras exactamente iguales no son anagrama.

def anagram(w1, w2):
    t1 = w1.upper().replace(" ", "")
    t2 = w2.upper().replace(" ", "")
    if t1 == t2 : return False
    if sorted(t1) == sorted(t2):
        return True
    return False
    

print(anagram("Oso", "Soo"));