## clases ##


# Definición
class MyEmptyPerson:
    pass ## se coloca para que una clase pueda quedar vacia 

print(MyEmptyPerson)
print(MyEmptyPerson())




# Clase con constructor, funciones y propiedades privadas y públicas

class Person: 
    def __init__(self, name, surname, alias = "sin alias"):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname} {alias}"

    def walk(self):
        print(f"{self.full_name} esta caminando")


#Persona 1
my_person = Person("Andres", "Marroquin")
print(my_person.name)
print(my_person.full_name)
my_person.walk()


#Persona 2
my_other_person = Person("Yeison", "Maroquin", "Shadow")
my_other_person.walk()

##Recordemos que esto no es inmutable pues es mutable por ejemplo:
my_other_person.full_name = "Hello, yo he mutado ahora full_name soy yooooo jajajajajaj"
print(my_other_person.full_name)



#Forma para privar un parametro del constructor asi sera inmutable

class Car:
    def __init__(self, name, color):
        self.__name = name #Privada e inmutable
        self.color = color

    def get_name(self):
        return self.__name


car_one = Car("Toyota", "Red")
print(car_one.get_name())
print(car_one.color)