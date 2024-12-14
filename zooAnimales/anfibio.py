from .animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorPiel = None, venenoso = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.listado.append(self)
    
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self, nuevoVenenoso):
        self._venenoso = nuevoVenenoso
    
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self, nuevoColorPiel):
        self._colorPiel = nuevoColorPiel

    def movimiento(self):
        return "saltar"
    
    @staticmethod
    def crearRana(nombreRana, edadRana, generoRana):
        rana = Anfibio(nombreRana, edadRana, "selva", generoRana, "rojo", True)
        Anfibio.ranas += 1
        return rana
    
    @staticmethod
    def crearSalamandra(nombreSalamandra, edadSalamandra, generoSalamandra):
        salamandra = Anfibio(nombreSalamandra, edadSalamandra, "selva", generoSalamandra, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return salamandra