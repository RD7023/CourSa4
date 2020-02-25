import numpy as np


class Sequence:
    def __init__(self, id, value, antecedent, succedent):
        self.id = id
        self.value = value
        self.antecedent = np.array(antecedent)  # left part
        self.succedent = np.array(succedent)  # right part

    def print_sequence(self):
        string = '('
        for i in range(len(self.antecedent)-1):
            string += self.antecedent[i].text+','

        string += self.antecedent[len(self.antecedent)-1].text
        string += ') ⊢ ('
        for i in range(len(self.succedent)-1):
            string += self.succedent[i].text + ','
        string += self.succedent[len(self.succedent)-1].text + ')'
        print(string)

    def text_sequence(self):
        string = '('
        for i in range(len(self.antecedent)-1):
            string += self.antecedent[i].text_formula()+','

        string += self.antecedent[len(self.antecedent)-1].text_formula()
        string += ') ⊢ ('
        for i in range(len(self.succedent)-1):
            string +=self.succedent[i].text_formula()+','
        string += self.succedent[len(self.succedent)-1].text_formula() + ')'
        return string
