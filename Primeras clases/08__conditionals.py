### Conditionals ###

#Primer ejemplo
my_condition = True
if my_condition :
    print("Se ejecuto el if")



#Segundo ejemplo con numeros
numbers = 4 * 3
if numbers == 12 :
    print("verdadero")



#Tercer ejemplo con else
car = "Red"
if car == "Red" :
    print("El carro es rojo")
else:
    print("el carro no es de color rojo")



#Cuarto ejemplo con elif
edad = 18
if edad >= 18 and edad < 50 :
    print("Pase a la fiesta 🎉")
elif edad < 18 :
    print("Eres menor de edad, ve a dormir mejor 💤")
else:
    print("Eres demaciado viejo para entrar, ve a dormir 🤶💤")
    

print("El sistema continua 😼")

#NOTA: En el momento en que el print bajo el if esta con tabulacion 
# forma parte el if si no esta tabulado esta fuera del if