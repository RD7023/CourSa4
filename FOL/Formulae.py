from FOL.Variable import Variable
from FOL.Alphabet import quantifier_symbols
from FOL.Alphabet import logical_symbols_binary
from FOL.Alphabet import logical_symbols
from FOL.Alphabet import l_not
from FOL.AtomicFormulae import AtomicFormulae


class Formulae:
    def __init__(self, quantifier, formulae_arr):
        # Checking that quantifier has appropriate length (2 or 0)
        assert len(quantifier) == 2 or len(quantifier) == 0

        # Checking that our logical part is appropriate without quantifier
        if len(quantifier) == 0:
            assert len(formulae_arr) == 2 or len(formulae_arr) == 3 or len(formulae_arr) == 1
            if len(formulae_arr) == 2:
                assert formulae_arr[0] == l_not
                assert isinstance(formulae_arr[1], AtomicFormulae) or isinstance(formulae_arr[1], Formulae)
            if len(formulae_arr) == 3:
                assert isinstance(formulae_arr[0], AtomicFormulae) or isinstance(formulae_arr[0], Formulae)
                assert formulae_arr[1] in logical_symbols_binary
                assert isinstance(formulae_arr[2], AtomicFormulae) or isinstance(formulae_arr[2], Formulae)
            if len(formulae_arr) == 1:
                assert isinstance(formulae_arr[0], AtomicFormulae)
        # Checking that our logical part is appropriate with quantifier
        else:
            assert len(formulae_arr) == 1
            assert isinstance(formulae_arr[0], Formulae) or isinstance(formulae_arr[0], AtomicFormulae)
            assert quantifier[0] in quantifier_symbols
            assert isinstance(quantifier[1], Variable)

        self.formulae_arr = formulae_arr  # formulas and connectives (a and b)
        self.quantifier = quantifier  # first element = quantifier, second = variable

    def text(self):
        txt = ''
        if len(self.quantifier) == 0:
            for i in range(len(self.formulae_arr)):
                if self.formulae_arr[i] in logical_symbols:
                    txt += ' ' + self.formulae_arr[i] + ' '
                else:
                    txt += self.formulae_arr[i].text()
        else:
            txt = '(' + self.quantifier[0] + self.quantifier[1].text() + ')('
            txt += self.formulae_arr[0].text() + ')'
        return txt

    def print(self):
        print(self.text())

    def get_P_t_f_var(self, arr):
        for i in range(len(self.formulae_arr)):
            if isinstance(self.formulae_arr[i], Formulae):
                self.formulae_arr[i].get_P_t_f_var(arr)
            if isinstance(self.formulae_arr[i], AtomicFormulae):
                arr.append(self.formulae_arr[i])
                self.formulae_arr[i].get_P_t_f_var(arr)
        return arr
