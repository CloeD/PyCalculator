"""

Faire la logique de l'application

"""


class PyCalculatorModel:
    def __init__(self):
        self.nombres = '0123456789'

    def effectuerOperation(self, a, operation, b):
        resultat = 0
        try:
            if operation == '+':
                resultat = float(a) + float(b)

            elif operation == '-':
                resultat = float(a) - float(b)

            elif operation == '*':
                resultat = float(a) * float(b)

            elif operation == '/':
                resultat = float(a) / float(b)

        except ZeroDivisionError:
            return "Cannot divide by zero"

        return resultat
            


    def calculerSousEquation(self, index, liste_equation):
        a = liste_equation[index - 1]
        b = liste_equation[index + 1]
        operation = liste_equation[index]
        resultat = self.effectuerOperation(self=self,a=a,operation=operation,b=b)
        liste_equation[index] = resultat
        liste_equation.pop(index - 1)
        liste_equation.pop(index)

    def calculerEquation(self, texte):
        # Séparer la String en plusieurs morceaux
        liste_equation = []
        chaine = ''
        for i in range(len(texte)):
            if texte[i] == '-' or texte[i] == '+' or texte[i] == '*' or texte[i] == '/':
                liste_equation.append(chaine)
                liste_equation.append(texte[i])
                chaine = ''
            else:
                chaine += texte[i]
        liste_equation.append(chaine)
        print(liste_equation)

        liste_operations = ['+', '-', '/', '*']
        while [op for op in liste_operations if (op in liste_equation)]:
            if '*' in texte and '/' in liste_equation:
                index_mul = liste_equation.index('*')
                index_div = liste_equation.index('/')

                if index_mul < index_div:
                    self.calculerSousEquation(self=self, index=index_mul, liste_equation=liste_equation)

                else:
                    self.calculerSousEquation(self=self, index=index_div, liste_equation=liste_equation)

            elif '*' in liste_equation:
                index_mul = liste_equation.index('*')
                self.calculerSousEquation(self=self,index=index_mul, liste_equation=liste_equation)


            elif '/' in liste_equation:
                index_div = liste_equation.index('/')
                self.calculerSousEquation(self=self, index=index_div, liste_equation=liste_equation)

            # Addition + Soustraction
            elif '+' in texte and '-' in liste_equation:
                index_add = liste_equation.index('+')
                index_sous = liste_equation.index('-')

                if index_add < index_sous:
                    self.calculerSousEquation(self=self, index=index_add, liste_equation=liste_equation)

                else:
                    self.calculerSousEquation(self=self, index=index_sous, liste_equation=liste_equation)

            elif '+' in liste_equation:
                index_add = liste_equation.index('+')
                self.calculerSousEquation(self=self,index=index_add, liste_equation=liste_equation)

            elif '-' in liste_equation:
                index_sous = liste_equation.index('-')
                self.calculerSousEquation(self=self,index=index_sous, liste_equation=liste_equation)

        return liste_equation[0]


