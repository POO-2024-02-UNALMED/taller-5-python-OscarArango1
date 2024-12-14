
class animal:
    totalAnimales = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        animal.totalAnimales += 1
    
    def getTotalAnimales(self):
        return animal.totalAnimales
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre
    
    def getEdad(self):
        return self._edad
    def setEdad(self, nuevaEdad):
        self._edad = nuevaEdad
    
    def getHabitat(self):
        return self._habitat
    def setHabitat(self,nuevoHabitat):
        self._habitat = nuevoHabitat

    def getGenero(self):
        return self._genero
    def setGenero(self, nuevoGenero):
        self._genero = nuevoGenero

    def getZona(self):
        return self._zona
    def setZona(self, nuevaZona):
        self._zona = nuevaZona

    def movimiento(self):
        return "desplazarse"
    
    @staticmethod
    def totalPorTipo():
        from .anfibio import Anfibio
        from .ave import Ave
        from .mamifero import Mamifero
        from .pez import Pez
        from .reptil import Reptil
        mensaje = f"Mamiferos : {len(Mamifero.listado)}\nAves : {len(Ave.listado)}\nReptiles : {len(Reptil.listado)}\nPeces : {len(Pez.listado)}\nAnfibios : {len(Anfibio.listado)}"
        return mensaje
    
    def __str__(self):
        mensaje = ""
        
        if self._zona != None:
            mensaje = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getnombre()} en el {self._zona.getZoo().getNombre()}"
        else:
            mensaje = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        
        return mensaje