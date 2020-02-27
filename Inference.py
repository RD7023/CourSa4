import numpy as np
import LogicalSymbols as LS
from Sequence import Sequence

l_not = LS.l_not
l_or = LS.l_or
l_and = LS.l_and
l_equiv = LS.l_equiv
l_implication = LS.l_implication
l_inference = LS.l_inference


class Inference:
    def __init__(self,upper_sequence,lower_sequence):
        self.upper_sequence = upper_sequence
        self.lower_sequence = lower_sequence

    def print_inference(self):
        if isinstance(self.upper_sequence,Sequence):
            symbolic_length = max(len(self.upper_sequence.text_sequence()),len(self.lower_sequence.text_sequence()))
            print(self.upper_sequence.text_sequence())
            print(int(0.61*symbolic_length)*'—')
            print(self.lower_sequence.text_sequence())
        else:
            first_upper = self.upper_sequence[0]
            second_upper = self.upper_sequence[1]
            print(first_upper.text_sequence(), end='\t')
            print(second_upper.text_sequence())
            symbolic_length = len(first_upper.text_sequence()) + len(second_upper.text_sequence())
            print(int(0.61 * symbolic_length) * '—')
            print(self.lower_sequence.text_sequence())

    def check_weakening_left(self):
        is_left = np.array_equal(self.lower_sequence.antecedent[1:], self.upper_sequence.antecedent)
        is_right = np.array_equal(self.upper_sequence.succedent, self.lower_sequence.succedent)

        if is_left and is_right:
            return True
        else:
            return False

    def check_weakening_right(self):
        is_left = np.array_equal(self.lower_sequence.antecedent, self.upper_sequence.antecedent)
        is_right = np.array_equal(self.upper_sequence.succedent, self.lower_sequence.succedent[:-1])

        if is_left and is_right:
            return True
        else:
            return False

    def check_contraction_left(self):
        if self.upper_sequence.antecedent[0] != self.upper_sequence.antecedent[1]:
            return False
        else:
            if np.array_equal(self.upper_sequence.antecedent[1:], self.lower_sequence.antecedent):
                23
            else:
                return False

        if np.array_equal(self.upper_sequence.succedent, self.lower_sequence.succedent):
            return True
        else:
            return False

    def check_contraction_right(self):
        if self.upper_sequence.succedent[-1] != self.upper_sequence.succedent[-2]:
            return False
        else:
            if np.array_equal(self.upper_sequence.succedent[:-1], self.lower_sequence.succedent):
                32
            else:
                return False

        if np.array_equal(self.upper_sequence.antecedent, self.lower_sequence.antecedent):
            return True
        else:
            return False

    def check_exchange_left(self):
        if len(self.upper_sequence.antecedent) != len(self.lower_sequence.antecedent):
            return False
        if np.array_equal(self.upper_sequence.succedent, self.lower_sequence.succedent):
            23
        else:
            return False

        is_exchange = False
        for i in range(len(self.upper_sequence.antecedent)-1):
            if self.upper_sequence.antecedent[i] == self.lower_sequence.antecedent[i+1] and self.upper_sequence.antecedent[i+1] == self.lower_sequence.antecedent[i]:
                is_exchange = True

        upper_left_subarray = self.upper_sequence.antecedent[0:i]
        lower_left_subarray = self.lower_sequence.antecedent[0:i]

        upper_right_subarray = self.upper_sequence.antecedent[i+2:]
        lower_right_subarray = self.lower_sequence.antecedent[i+2:]

        is_left_subarray = np.array_equal(upper_left_subarray, lower_left_subarray)
        is_right_subarray = np.array_equal(upper_right_subarray, lower_right_subarray)

        if is_left_subarray and is_right_subarray and is_exchange:
            return True
        else:
            return False

    def check_exchange_right(self):
        if len(self.upper_sequence.succedent)!=len(self.lower_sequence.succedent):
            return False
        if np.array_equal(self.upper_sequence.antecedent,self.lower_sequence.antecedent):
            32
        else:
            return False

        is_exchange = False
        for i in range(len(self.upper_sequence.succedent)-1):
            if self.upper_sequence.succedent[i] == self.lower_sequence.succedent[i+1] and  self.upper_sequence.succedent[i+1] == self.lower_sequence.succedent[i]:
                is_exchange = True

        upper_left_subarray = self.upper_sequence.succedent[0:i]
        lower_left_subarray = self.lower_sequence.succedent[0:i]

        upper_right_subarray = self.upper_sequence.succedent[i+2:]
        lower_right_subarray = self.lower_sequence.succedent[i+2:]

        is_left_subarray = np.array_equal(upper_left_subarray, lower_left_subarray)
        is_right_subarray = np.array_equal(upper_right_subarray, lower_right_subarray)

        if is_left_subarray and is_right_subarray and is_exchange:
            return True
        else:
            return False

    def check_not_left(self):
        if len(self.upper_sequence.antecedent)+1 != len(self.lower_sequence.antecedent):
            return False
        if len(self.upper_sequence.succedent) != len(self.lower_sequence.succedent)+1:
            return False
        if not np.array_equal(self.upper_sequence.antecedent, self.lower_sequence.antecedent[1:]):
            return False
        if not np.array_equal(self.upper_sequence.succedent[:-1], self.lower_sequence.succedent):
            return False

        A = self.upper_sequence.succedent[-1]
        A_not = self.lower_sequence.antecedent[0]

        if len(A.connectives_pos[0]) > 0 and A.connectives_pos[0][0] == l_not:
            if A.formula_pos[0][0] == A_not.formula_pos[0][0]:
                return True
        else:
            if A_not.connectives_pos[0][0] == l_not:
                if A_not.formula_pos[0][0] == A.formula_pos[0][0]:
                    return True
        return False

    def check_not_right(self):
        if len(self.upper_sequence.antecedent) != len(self.lower_sequence.antecedent)+1:
            return False
        if len(self.upper_sequence.succedent)+1 != len(self.lower_sequence.succedent):
            return False
        if not np.array_equal(self.upper_sequence.succedent, self.lower_sequence.succedent[1:]):
            return False
        if not np.array_equal(self.upper_sequence.succedent[:-1], self.lower_sequence.succedent):
            return False

        A = self.upper_sequence.antecedent[0]
        A_not = self.lower_sequence.succedent[-1]

        if len(A.connectives_pos[0]) > 0 and A.connectives_pos[0][0] == l_not:
            if A.formula_pos[0][0] == A_not.formula_pos[0][0]:
                return True
        else:
            if A_not.connectives_pos[0][0] == l_not:
                if A_not.formula_pos[0][0] == A.formula_pos[0][0]:
                    return True
        return False

    def check_and_left(self):
        if len(self.upper_sequence.antecedent)!=len(self.lower_sequence.antecedent)+1:

            return False
        if len(self.upper_sequence.succedent)!=len(self.lower_sequence.succedent):

            return False
        if not np.array_equal(self.upper_sequence.antecedent[2:],self.lower_sequence.antecedent[1:]):

            return False
        if not np.array_equal(self.upper_sequence.succedent,self.lower_sequence.succedent):
            print(23)
            return False

        A = self.upper_sequence.antecedent[0]
        B = self.upper_sequence.antecedent[1]
        A_and_B = self.lower_sequence.antecedent[0]
        if A!=A_and_B.formula_pos[0][0][0]:
            return False
        if B!=A_and_B.formula_pos[0][0][1]:
            return False
        if A_and_B.connectives_pos[0][0]==l_and and A_and_B.connectives_pos[1][0] == 1:
            return True
        return False

    def check_or_left(self):
        if isinstance(self.upper_sequence,Sequence):

            return False

        first_upper = self.upper_sequence[0]
        second_upper = self.upper_sequence[1]
        lower = self.lower_sequence

        if first_upper.antecedent[1:].all() != second_upper.antecedent[1:].all():
            return False

        if first_upper.succedent.all() != second_upper.succedent.all():
            return False

        if first_upper.antecedent[1:].all() != lower.antecedent[1:].all():
            return False

        if first_upper.succedent.all() != lower.succedent.all():
            return False

        A = first_upper.antecedent[0]
        B = second_upper.antecedent[0]
        A_or_B = lower.antecedent[0]

        if A!= A_or_B.formula_pos[0][0][0]:
            return False

        if B != A_or_B.formula_pos[0][0][1]:
            return False

        if A_or_B.connectives_pos[0][0] != l_or:
            return False

        return True

    def check_implication_left(self):
        if isinstance(self.upper_sequence,Sequence):
            return False

        first_upper = self.upper_sequence[0]
        second_upper = self.upper_sequence[1]
        lower = self.lower_sequence

        if first_upper.antecedent.all() != second_upper.antecedent[1:].all():
            return False

        if first_upper.succedent[:-1].all() != second_upper.succedent.all():
            return False

        if first_upper.antecedent.all() != lower.antecedent[1:].all():
            return False

        if first_upper.succedent[:-1].all() != lower.succedent.all():
            return False

        A = first_upper.succedent[-1]
        B = second_upper.antecedent[0]

        A_imp_B = lower.antecedent[0]

        if A!= A_imp_B.formula_pos[0][0][0]:
            return False

        if B != A_imp_B.formula_pos[0][0][1]:
            return False

        if A_imp_B.connectives_pos[0][0] != l_implication:
            return False

        return True
