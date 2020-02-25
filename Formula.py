import numpy as np


class Formula:  # Wrapping our atoms with formulas and putting their relations into practice

    def __init__(self, id, value, formula_pos, connectives_pos):
        self.id = id
        self.value = value
        self.formula_pos = formula_pos,  # formula(-s)'s position in a wrapping formula
        self.connectives_pos = connectives_pos  # logical symbol(-s)'s position in a wrapping formula

        atoms = np.array(self.formula_pos[0][0])  # formulas_pos has both the formulas(atoms) themselves
        atoms_indices = np.array(self.formula_pos[0][1])  # and their indices, implemented as 2-dim numpy array
        connectives = np.array(
            self.connectives_pos[0])  # connectives_pos is the same as formulas_pos
        connectives_indices = np.array(self.connectives_pos[1])
        if len(connectives) == 0:
            formula_length = 1
        else:
            formula_length = max(max(connectives_indices), max(atoms_indices)) + 1
        formula_text = ''
        for i in range(formula_length):
            if i in atoms_indices:
                atom_index = np.where(atoms_indices == i)
                formula_text += atoms[atom_index][0].text
            else:
                connectives_index = np.where(connectives_indices == i)
                formula_text += connectives[connectives_index][0]
        self.text = formula_text

    def print_formula(self):  # method for printing the whole formula
        formulas = np.array(self.formula_pos[0][0])
        formulas_indices = np.array(self.formula_pos[0][1])
        connectives = np.array(self.connectives_pos[0])
        connectives_indices = np.array(self.connectives_pos[1])
        if len(connectives) == 0:
            formula_length = 1
        else:
            formula_length = max(max(connectives_indices), max(formulas_indices)) + 1

        formula_text = ''
        for i in range(formula_length):
            if i in formulas_indices:
                formula_index = np.where(formulas_indices == i)
                formula_text += formulas[formula_index][0].text
            else:
                connectives_index = np.where(connectives_indices == i)
                formula_text += connectives[connectives_index][0]
        print(formula_text)

    def text_formula(self):
        atoms = np.array(self.formula_pos[0][0])
        atoms_indices = np.array(self.formula_pos[0][1])
        connectives = np.array(self.connectives_pos[0])
        connectives_indices = np.array(self.connectives_pos[1])
        if len(connectives) == 0:
            formula_length = 1
        else:
            formula_length = max(max(connectives_indices), max(atoms_indices)) + 1
        formula_text = ''
        for i in range(formula_length):
            if i in atoms_indices:
                atom_index = np.where(atoms_indices == i)
                formula_text += atoms[atom_index][0].text
            else:
                connectives_index = np.where(connectives_indices == i)
                formula_text += connectives[connectives_index][0]
        return formula_text
