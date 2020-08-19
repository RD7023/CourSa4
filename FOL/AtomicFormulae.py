from FOL.Term import Term
from FOL.Alphabet import predicate_symbols
from FOL.Alphabet import index_symbols
from FOL.Function import Function
from FOL.Variable import Variable


class AtomicFormulae:
    def __init__(self, symbol, term_arr):
        # Checking that our symbols type match
        assert len(symbol) > 0
        if len(symbol) > 1:
            assert symbol[0] in predicate_symbols
            for i in range(1, len(symbol)):
                assert symbol[i] in index_symbols
        elif len(symbol) == 1:
            assert symbol in predicate_symbols

        # Checking that our parameters type match
        for param in term_arr:
            assert isinstance(param, Term) or isinstance(param, Variable)

        self.symbol = symbol
        self.term_arr = term_arr  # terms

    def print(self):
        print(self.text())

    def text(self):
        return self.symbol + '(' + ','.join([term.text() for term in self.term_arr]) + ')'

    def get_P_t_f_var(self, arr):
        for i in range(len(self.term_arr)):
            if isinstance(self.term_arr[i], Term):
                arr.append(self.term_arr[i])
                self.term_arr[i].get_P_t_f_var(arr)
            if isinstance(self.term_arr[i], Function):
                arr.append(self.term_arr[i])
                self.term_arr[i].get_P_t_f_var(arr)
            if isinstance(self.term_arr[i], Variable):
                arr.append(self.term_arr[i])
