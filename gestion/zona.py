class Zona:
    def __init__(self, nombre = None, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def getNombre(self):
        return self._nombre
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre
    
    def getZoo(self):
        return self._zoo
    def setZoo(self, nuevoZoologico):
        self._zoo = nuevoZoologico

    def cantidadAnimales(self):
        return len(self._animales)
    
    def agregarAnimales(self, nuevoAnimal):
        self._animales.append(nuevoAnimal)