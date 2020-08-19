from FOL.Formulae import Formulae
from FOL.Alphabet import l_inference


class Sequence:
    def __init__(self, antecedent, succedent):
        for formula in antecedent:
            assert isinstance(formula, Formulae)
        for formula in succedent:
            assert isinstance(formula, Formulae)
        self.antecedent = antecedent  # left part
        self.succedent = succedent  # right part

    def text(self):
        return ', '.join([formula.text() for formula in self.antecedent]) + '  ' + l_inference + '  ' +\
               ', '.join([formula.text() for formula in self.succedent])

    def print(self):
        print(self.text())
