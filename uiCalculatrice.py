"""

Afficher la vue de l'application

"""

from modeleCalculatrice import PyCalculatorModel
from controleurCalculatrice import PyCalculatorControl

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLineEdit


class PyCalculator:

    def __init__(self):
        self.window = QWidget()
        self.buttonW = QWidget()

        # Créer le layout de la calculatrice
        self.buttonsLayout = QGridLayout()
        self.windowLayout = QVBoxLayout()

        # Créer un dictionnaire des boutons
        self.buttons = {'7': (0, 0),
                        '8': (0, 1),
                        '9': (0, 2),
                        '+': (0, 3),
                        '4': (1, 0),
                        '5': (1, 1),
                        '6': (1, 2),
                        '-': (1, 3),
                        '1': (2, 0),
                        '2': (2, 1),
                        '3': (2, 2),
                        '/': (2, 3),
                        'DEL': (3, 0),
                        '0': (3, 1),
                        '.': (3, 2),
                        '*': (3, 3),
                        'CLEAR': (4, 0),
                        '(': (4, 1),
                        ')': (4, 2),
                        '=': (4, 3)
                        }

        self.textBox = QLineEdit()

    # Initialiser les boutons
    def initBoutons(self):
        for button, position in self.buttons.items():
            self.buttons[button] = QPushButton(button)
            self.buttons[button].setStyleSheet('font: 20px;')
            self.buttons[button].setMinimumHeight(50)
            self.buttons[button].setContentsMargins(0, 0, 0, 0)
            self.buttonsLayout.addWidget(self.buttons[button], position[0], position[1])

        self.buttonsLayout.setSpacing(0)
        # self.buttonsLayout.setVerticalSpacing(0)
        # self.buttonsLayout.setHorizontalSpacing(0)
        self.buttonW.setLayout(self.buttonsLayout)

    def initBoite(self):
        self.textBox.setReadOnly(True)
        self.textBox.setMinimumHeight(50)
        self.textBox.setAlignment(Qt.AlignRight)
        self.textBox.setStyleSheet('font: 20px;')

    def start(self):
        self.initBoutons()
        self.initBoite()
        self.windowLayout.addWidget(self.textBox)
        self.windowLayout.addWidget(self.buttonW)
        self.window.setLayout(self.windowLayout)
        self.window.setMinimumHeight(500)
        self.window.setMinimumWidth(350)
        self.window.show()

    def updateBoite(self, equation):
        self.textBox.setText(str(equation))

    def getTexteBoite(self):
        return self.textBox.text()

    def clearBoite(self):
        self.textBox.setText('')


def main():
    app = QApplication([])
    appli = PyCalculator()
    appli.start()
    PyCalculatorControl(appli, PyCalculatorModel)
    app.exec()



main()

