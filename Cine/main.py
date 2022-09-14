import sys
from interfaz import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize
from Clases import *


class Traductor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.inicioBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homePage))
        self.ui.titanicBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.titanicPage))
        self.ui.intelestelarBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.intelestelarPage))
        self.ui.viernes13Btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.viernes13Page))
        self.ui.opcionesBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.optionsPage))
        self.ui.ayudaBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ayudaPage))
        self.ui.desarrolladorBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.desarrolladorPage))

        # self.setMidowTnimumSize(QSize(300, 200))
        # self.setWinitle("PyQt messagebox example - pythonprogramminglanguage.com")

        # pybutton = QPushButton('Show messagebox', self)
        # pybutton.clicked.connect(self.clickMethod)
        # pybutton.resize(200, 64)
        # pybutton.move(50, 50)
        # QMessageBox.about(self, "Title", "Message")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Traductor()
    window.show()
    sys.exit(app.exec_())

