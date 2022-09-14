import random
import Espectador


def posicionTable(self, fila, columna):
    return random.randint(0, fila), random.randint(0, columna)


def espectadorRandom(self):
    objViewer = Espectador()
    objViewer.setNombre(random.choice(
        ["Santiago", "Mateo", "Sebastián", "Leonardo", "Diego",
         "Sofía", "Valentina", "Ximena", "Regina", "Camila"]))
    objViewer.setEdad(random.randint(8, 20))
    objViewer.setDinero(random.randint(30, 50))

    return objViewer

