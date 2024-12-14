from .animal import animal

class mamifero(animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, pelaje = None, patas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        mamifero.listado.append(self)
    
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
        caballo = mamifero(nombreCaballo, edadCaballo, "pradera", generoCaballo)
        mamifero.caballos += 1
        return caballo
    
    @staticmethod
    def crearLeon(nombreLeon, edadLeon, generoLeon):
        leon = mamifero(nombreLeon, edadLeon, "selva", generoLeon)
        mamifero.leones += 1
        return leon
    
    def cantidadMamiferos(self):
        return len(mamifero.listado)