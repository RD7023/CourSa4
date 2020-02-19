class Atom:

    def __init__(self, id, text, value):
        self.id = id
        self.text = text
        self.value = value


    def print_formula(self):
        print(self.text)