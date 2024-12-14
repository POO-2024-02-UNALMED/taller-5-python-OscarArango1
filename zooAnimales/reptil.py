from .animal import animal

class reptil(animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorEscamas = None, largoCola = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        reptil.listado.append(self)
    
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
        iguana = reptil(nombreIguana, edadIguana, "humedal", generoIguana, "verde", 3)
        reptil.iguanas += 1
        return iguana
    
    @staticmethod
    def crearSerpiente(nombreSerpiente, edadSerpiente, generoSerpiente):
        serpiente = reptil(nombreSerpiente, edadSerpiente, "jungla", generoSerpiente, "blanco", 1)
        reptil.serpientes += 1
        return serpiente