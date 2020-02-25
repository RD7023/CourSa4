class Atom:
    def __init__(self, id, text, value):  # the core of the project
        self.id = id
        self.text = text
        self.value = value

    def print_formula(self):
        print(self.text)
