from .animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorEscamas = None, largoCola = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)
    
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, nuevoColorEscamas):
        self._colorEscamascolorEscamas = nuevoColorEscamas

    def getLargoCola(self):
        return self._largoCola
    def setCola(self, nuevoLargoCola):
        self._largoCola = nuevoLargoCola

    def movimiento(self):
        return "reptar"
    
    @staticmethod
    def crearIguana(nombreIguana, edadIguana, generoIguana):
        iguana = Reptil(nombreIguana, edadIguana, "humedal", generoIguana, "verde", 3)
        Reptil.iguanas += 1
        return iguana
    
    @staticmethod
    def crearSerpiente(nombreSerpiente, edadSerpiente, generoSerpiente):
        serpiente = Reptil(nombreSerpiente, edadSerpiente, "jungla", generoSerpiente, "blanco", 1)
        Reptil.serpientes += 1
        return serpiente