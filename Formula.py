import numpy as np

class Formula:

    def __init__(self, id, value, formula_pos, conectivs_pos):
        self.id = id
        self.value = value
        self.formula_pos = formula_pos,
        self.conectivs_pos = conectivs_pos

        atoms=np.array(self.formula_pos[0][0])
        atoms_indecies = np.array(self.formula_pos[0][1])
        connectivs = np.array(self.conectivs_pos[0])
        connectivs_indecies = np.array(self.conectivs_pos[1])
        formula_length = max(max(connectivs_indecies),max(atoms_indecies))+1
        formula_text = ''
        for i in range(formula_length):
            if i in atoms_indecies:
                atom_index = np.where(atoms_indecies == i)
                formula_text+=atoms[atom_index][0].text
            else:
                connectiv_index = np.where(connectivs_indecies == i)
                formula_text += connectivs[connectiv_index][0]
        self.text = formula_text

    def print_formula(self):
        formulas=np.array(self.formula_pos[0][0])
        formulas_indecies = np.array(self.formula_pos[0][1])
        connectivs = np.array(self.conectivs_pos[0])
        connectivs_indecies = np.array(self.conectivs_pos[1])
        formula_length = max(max(connectivs_indecies),max(formulas_indecies))+1
        formula_text = ''
        for i in range(formula_length):
            if i in formulas_indecies:
                formula_index = np.where(formulas_indecies == i)
                formula_text+=formulas[formula_index][0].text
            else:
                connectiv_index = np.where(connectivs_indecies == i)
                formula_text += connectivs[connectiv_index][0]
        print(formula_text)

    def text_formula(self):
        atoms=np.array(self.formula_pos[0][0])
        atoms_indecies = np.array(self.formula_pos[0][1])
        connectivs = np.array(self.conectivs_pos[0])
        connectivs_indecies = np.array(self.conectivs_pos[1])
        formula_length = max(max(connectivs_indecies),max(atoms_indecies))+1
        formula_text = ''

        for i in range(formula_length):
            if i in atoms_indecies:
                atom_index = np.where(atoms_indecies == i)
                formula_text+=atoms[atom_index][0].text
            else:
                connectiv_index = np.where(connectivs_indecies == i)
                formula_text += connectivs[connectiv_index][0]
        return formula_text