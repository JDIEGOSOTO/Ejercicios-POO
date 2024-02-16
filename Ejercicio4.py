class Forma():
    def __init__(self, nombre):
        self.nombre=nombre

    def dibujar(self):
        print(f"Dibujando {self.nombre}")

class Color():
    def __init__(self, color):
        self.color=color

    def pintar(self):
        print(f"Pintando con {self.color}")

class CuadradoColorido(Forma, Color):
    def __init__ (self, nombre, color):
        Forma.__init__(self, nombre)
        Color.__init__(self, color)

cuadradocolorido1=CuadradoColorido("Cuadrado", "Rojo")

cuadradocolorido1.dibujar()
cuadradocolorido1.pintar()


