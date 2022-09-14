import sys, pickle
from interfaz import *
from PyQt5 import QtWidgets


class Traductor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # acceder a las páginas
        self.ui.inicioBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homePage))
        self.ui.es_inglesBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.es_inglesPage))
        self.ui.es_francesBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.es_francesPage))
        self.ui.es_alemanBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.es_alemanPage))
        self.ui.opcionesBtn.clicked.connect( lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.optionsPage))
        self.ui.ayudaBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ayudaPage))
        self.ui.desarrolladorBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.desarrolladorPage))

        self.ui.es_inglesTabla.setColumnWidth(0, 230)
        self.ui.es_inglesTabla.setColumnWidth(1, 230)

        self.ui.es_francesTabla.setColumnWidth(0, 230)
        self.ui.es_francesTabla.setColumnWidth(1, 230)

        self.ui.es_alemanTabla.setColumnWidth(0, 230)
        self.ui.es_alemanTabla.setColumnWidth(1, 230)

        dicIng = self.getDicEs_Ing()
        dicFra = self.getDicEs_Fra()
        dicAle = self.getDicEs_Al()

        self.ui.pushButton_2.clicked.connect(lambda: self.buscarPalabraEs(dicIng, dicFra, dicAle))

        self.ui.es_inglesTabla.setRowCount(len(dicIng))
        self.ui.es_francesTabla.setRowCount(len(dicFra))
        self.ui.es_alemanTabla.setRowCount(len(dicAle))

        row_index = 0

        for es, ing in dicIng.items():
            self.ui.es_inglesTabla.setItem(row_index, 0, QtWidgets.QTableWidgetItem(es))
            self.ui.es_inglesTabla.setItem(row_index, 1, QtWidgets.QTableWidgetItem(ing))
            row_index += 1

        row_index = 0

        for es, fra in dicFra.items():
            self.ui.es_francesTabla.setItem(row_index, 0, QtWidgets.QTableWidgetItem(es))
            self.ui.es_francesTabla.setItem(row_index, 1, QtWidgets.QTableWidgetItem(fra))
            row_index += 1

        row_index = 0

        for es, al in dicAle.items():
            self.ui.es_alemanTabla.setItem(row_index, 0, QtWidgets.QTableWidgetItem(es))
            self.ui.es_alemanTabla.setItem(row_index, 1, QtWidgets.QTableWidgetItem(al))
            row_index += 1

        self.ui.es_inglesTabla.sortItems(0)
        self.ui.es_francesTabla.sortItems(0)
        self.ui.es_alemanTabla.sortItems(0)

    def getDicEs_Ing(self):
        file = open('diccionarios/es_ingDic', 'rb')
        diccionario = pickle.load(file)
        return diccionario

    def getDicEs_Fra(self):
        file = open('diccionarios/es_fraDic', 'rb')
        diccionario = pickle.load(file)
        return diccionario

    def getDicEs_Al(self):
        file = open('diccionarios/es_alDic', 'rb')
        diccionario = pickle.load(file)
        return diccionario

    def buscarPalabraEs(self, dicIng, dicFra, dicAle):
        palabra = self.ui.buscarPalabraInput.text()
        palabra = palabra.lower()

        for es, ing in dicIng.items():
            self.ui.buscadorTabla.setRowCount(1)
            if es == palabra:
                self.ui.buscadorTabla.setItem(0, 0, QtWidgets.QTableWidgetItem(es))
                self.ui.buscadorTabla.setItem(0, 1, QtWidgets.QTableWidgetItem(ing))

        for es, fra in dicFra.items():
            if es == palabra:
                self.ui.buscadorTabla.setItem(0, 2, QtWidgets.QTableWidgetItem(fra))

        for es, al in dicAle.items():
            if es == palabra:
                self.ui.buscadorTabla.setItem(0, 3, QtWidgets.QTableWidgetItem(al))

    def buscarPalabraOtroIdioma(self, palabra, diccionario):
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Traductor()
    window.show()
    sys.exit(app.exec_())


