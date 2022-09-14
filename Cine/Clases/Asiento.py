import Espectador


class Asiento:
    def __init__(self, letra, fila):
        self.letra = letra
        self.fila = fila
        self.objEspectador = Espectador()
        self.objEspectador = None

    def ocupado(self):
        return self.objEspectador is not None

    def getLetra(self):
        return self.letra

    def setLetra(self, letra):
        self.letra = letra

    def getFila(self):
        return self.fila

    def setFila(self, fila):
        self.fila = fila
