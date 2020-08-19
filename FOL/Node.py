import FOL.InferenceCheck as check


class Node:
    def __init__(self, sequence, parent_sequence, descendant_sequence_arr, rule):
        self.value = sequence
        self.parent_sequence = parent_sequence
        self.descendant_sequence_arr = descendant_sequence_arr
        self.rule = rule

    def check_node(self):
        if self.rule == 'exchange left':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.exchange_left(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'exchange right':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.exchange_right(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'contraction left':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.contraction_left(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'contraction right':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.contraction_right(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'weakening left':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.weakening_left(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'weakening right':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.weakening_right(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'cut':
            if len(self.descendant_sequence_arr) != 2:
                return False
            return check.cut(self.descendant_sequence_arr[0], self.descendant_sequence_arr[1], self.value)

        if self.rule == 'not left':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.not_left(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'not right':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.not_right(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'and left':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.and_left(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'and right':
            if len(self.descendant_sequence_arr) != 2:
                return False
            return check.and_right(self.descendant_sequence_arr[0], self.descendant_sequence_arr[1], self.value)

        if self.rule == 'or left':
            if len(self.descendant_sequence_arr) != 2:
                return False
            return check.or_left(self.descendant_sequence_arr[0], self.descendant_sequence_arr[1], self.value)

        if self.rule == 'or right':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.or_right(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'imp left':
            if len(self.descendant_sequence_arr) != 2:
                return False
            return check.imp_left(self.descendant_sequence_arr[0], self.descendant_sequence_arr[1], self.value)

        if self.rule == 'imp right':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.imp_right(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'univ left':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.univ_left(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'exist left':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.exist_left(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'univ right':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.univ_right(self.descendant_sequence_arr[0], self.value)

        if self.rule == 'exist right':
            if len(self.descendant_sequence_arr) != 1:
                return False
            return check.exist_right(self.descendant_sequence_arr[0], self.value)

        if self.rule == '':
            if self.value.antecedent != self.value.succedent:
                return False
            return True
