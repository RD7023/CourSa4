from FOL.Alphabet import constant_symbols
from FOL.Alphabet import index_symbols


class Constant:
    def __init__(self, symbol):
        # Checking that our symbols type match
        assert len(symbol) > 0
        if len(symbol) > 1:
            assert symbol[0] in constant_symbols
            for i in range(1, len(symbol)):
                assert symbol[i] in index_symbols
        elif len(symbol) == 1:
            assert symbol in constant_symbols

        self.symbol = symbol

    def print(self):
        print(self.text())

    def text(self):
        return self.symbol
