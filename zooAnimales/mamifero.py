from .animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, pelaje = None, patas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)
    
    def isPelaje(self):
        return self._pelaje
    def setPelaje(self, nuevoPelaje):
        self._pelaje = nuevoPelaje

    def getPatas(self):
        return self._patas
    def setPatas(self, nuevasPatas):
        self._patas = nuevasPatas
    
    @staticmethod
    def crearCaballo(nombreCaballo, edadCaballo, generoCaballo):
        caballo = Mamifero(nombreCaballo, edadCaballo, "pradera", generoCaballo)
        Mamifero.caballos += 1
        return caballo
    
    @staticmethod
    def crearLeon(nombreLeon, edadLeon, generoLeon):
        leon = Mamifero(nombreLeon, edadLeon, "selva", generoLeon)
        Mamifero.leones += 1
        return leon
    
    def cantidadMamiferos(self):
        return len(Mamifero.listado)