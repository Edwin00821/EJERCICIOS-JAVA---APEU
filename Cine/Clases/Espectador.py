
class Espectador:
    def __init__(self, nombre, edad, dinero):
        self.nombre = nombre
        self.edad = edad
        self.dinero = dinero

    def pagarBoleto(self, precio):
        self.dinero -= precio

    def tieneEdad(self, edadMinima):
        return self.edad >= edadMinima

    def suficienteDinero(self, precioBoleto):
        return self.dinero >= precioBoleto
