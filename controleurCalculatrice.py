"""

Contrôler l'interaction de l'application

"""

from functools import partial


class PyCalculatorControl():

    def __init__(self, ui, mod):
        self.ui = ui
        self.mod = mod
        self.connecterBoutons()

    def ajouterTexte(self, texte):
        self.ui.updateBoite(self.ui.getTexteBoite() + texte)

    def supprimerTexte(self):
        self.ui.updateBoite(self.ui.getTexteBoite()[:-1])

    def clearTexte(self):
        self.ui.clearBoite()

    def donnerResultat(self):
        texte = self.ui.getTexteBoite()
        resultat = self.mod.calculerEquation(self=self.mod, texte=texte)
        self.ui.updateBoite(resultat)

    def connecterBoutons(self):
        for text, button in self.ui.buttons.items():

            if text == '=':
                button.clicked.connect(lambda: self.donnerResultat())

            elif text == 'DEL':
                button.clicked.connect(lambda: self.supprimerTexte())

            elif text == 'CLEAR':
                button.clicked.connect(lambda: self.clearTexte())

            else:
                button.clicked.connect(partial(self.ajouterTexte, text))

