import numpy as np

class Inference:
    def __init__(self,upper_sequence,lower_sequence):
        self.upper_sequence = upper_sequence
        self.lower_sequence = lower_sequence


    def print_inference(self):
        symolic_length = max(len(self.upper_sequence.text_sequence()),len(self.lower_sequence.text_sequence()))
        print(self.upper_sequence.text_sequence())
        print(int(0.61*symolic_length)*'—')
        print(self.lower_sequence.text_sequence())

    def check_weakening_left(self):
        is_left = np.array_equal(self.lower_sequence.antecedent[1:], self.upper_sequence.antecedent)
        is_right = np.array_equal(self.upper_sequence.succedent, self.lower_sequence.succedent)

        if is_left and is_right:
            return True
        else:
            return False

    def check_contraction_left(self):
        if self.upper_sequence.antecedent[0]!=self.upper_sequence.antecedent[1]:
            return False
        else:
            if np.array_equal(self.upper_sequence.antecedent[1:],self.lower_sequence.antecedent):
                23
            else:
                return False

        if np.array_equal(self.upper_sequence.succedent,self.lower_sequence.succedent):
            return True
        else:
            return False
    def check_exchange_left(self):
        if len(self.upper_sequence.antecedent)!=len(self.lower_sequence.antecedent):
            return False
        if np.array_equal(self.upper_sequence.succedent,self.lower_sequence.succedent):
            23
        else:
            return False

        is_exchange = False
        for i in range(len(self.upper_sequence.antecedent)-2):
            if self.upper_sequence.antecedent[i] == self.lower_sequence.antecedent[i+1] and  self.upper_sequence.antecedent[i+1] == self.lower_sequence.antecedent[i]:
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