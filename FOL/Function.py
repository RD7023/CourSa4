from FOL.Constant import Constant
from FOL.Variable import Variable
from FOL.Alphabet import function_symbols
from FOL.Alphabet import index_symbols


class Function:
    def __init__(self, symbol, param_arr):
        # Checking that our symbols type match
        assert len(symbol) > 0
        if len(symbol) > 1:
            assert symbol[0] in function_symbols
            for i in range(1, len(symbol)):
                assert symbol[i] in index_symbols
        elif len(symbol) == 1:
            assert symbol in function_symbols

        # Checking that our parameters type match
        for param in param_arr:
            assert isinstance(param, Constant) or isinstance(param, Variable)

        self.symbol = symbol
        self.param_arr = param_arr  # variables or constants

    def print(self):
        print(self.text())

    def text(self):
        return self.symbol + '(' + ','.join([param.text() for param in self.param_arr]) + ')'

    def get_P_t_f_var(self, arr):
        for i in range(len(self.param_arr)):
            if isinstance(self.param_arr[i], Variable):
                arr.append(self.param_arr[i])
