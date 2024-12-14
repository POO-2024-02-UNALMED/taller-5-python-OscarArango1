from .animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)
    
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, nuevoColorPlumas):
        self._colorPlumas = nuevoColorPlumas
    
    def movimiento(self):
        return "volar"
    
    @staticmethod
    def crearAguila(nombreAguila, edadAguila, generoAguila):
        aguila = Ave(nombreAguila, edadAguila, "montañas", generoAguila, "blanco y amarillo")
        Ave.aguilas += 1
        return aguila
    
    @staticmethod
    def crearHalcon(nombreHalcon, edadHalcon, generoHalcon):
        halcon = Ave(nombreHalcon, edadHalcon, "montañas", generoHalcon, "café glorioso")
        Ave.halcones += 1
        return halcon
    
    def toString(self):
        if self._zona != None:
            mensaje = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getnombre()} en el {self._zona.getZoo().getNombre()}"
        else:
            mensaje = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        return mensaje