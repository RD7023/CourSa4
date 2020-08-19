from FOL.Alphabet import variable_symbols
from FOL.Alphabet import index_symbols


class Variable:
    def __init__(self, symbol):
        # Checking that our symbols type match
        assert len(symbol) > 0
        if len(symbol) > 1:
            assert symbol[0] in variable_symbols
            for i in range(1, len(symbol)):
                assert symbol[i] in index_symbols
        elif len(symbol) == 1:
            assert symbol in variable_symbols

        self.symbol = symbol

    def print(self):
        print(self.text())

    def text(self):
        return self.symbol
