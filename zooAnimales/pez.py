from .animal import animal

class pez(animal):
    listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorEscamas = None, cantidadAletas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        pez.listado.append(self)
    
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, nuevoColorEscamas):
        self._colorEscamas = nuevoColorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self, nuevoCantidadAletas):
        self._cantidadAletas = nuevoCantidadAletas

    def movimiento(self):
        return "nadar"
    
    @staticmethod
    def crearSalmon(nombreSalmon, edadSalmon, generoSalmon):
        salmon = pez(nombreSalmon, edadSalmon, "océano", generoSalmon, "rojo", 6)
        pez.salmones += 1
        return salmon
    
    @staticmethod
    def crearBacalao(nombreBacalao, edadBacalao, generoBacalao):
        bacalao = pez(nombreBacalao, edadBacalao, "océano", generoBacalao, "gris", 6)
        pez.bacalaos += 1
        return bacalao