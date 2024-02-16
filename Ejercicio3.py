class Animal():
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def hacer_sonido(self, sonido):
        print(sonido)

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza=raza
    
    def hacer_sonido(self):
        print("Wau, Wau!")

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.raza=color

    def hacer_sonido(self):
        print("Miau, Miau!")
    
perro1=Perro("Bobby", 10, "Labrador")
gato1=Gato("Michi", 5, "Naranja")

print(f"El perro {perro1.nombre} hace: ")
perro1.hacer_sonido()
print(f"El gato {gato1.nombre} hace: ")
gato1.hacer_sonido()




    