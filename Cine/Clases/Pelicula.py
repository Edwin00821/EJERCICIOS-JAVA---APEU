class Pelicula:
    def __init__(self, titulo, duracion, edadMinima, director):

        self.titulo = titulo
        self.duracion = duracion
        self.edadMinima = edadMinima
        self.director = director

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getDuracion(self):
        return self.duracion

    def setDuracion(self, duracion):
        self.duracion = duracion

    def getEdadMinima(self):
        return self.edadMinima

    def setEdadMinima(self, edadMin):
        self.edadMinima = edadMin

    def getDirector(self):
        return self.director

    def setDirector(self, director):
        self.director = director
