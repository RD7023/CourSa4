import FOL.Alphabet as symb
from FOL.Term import Term, Variable


def exchange_left(s_upper, s_lower):
    if s_upper.succedent != s_lower.succedent:
        return False
    if len(s_upper.antecedent) != len(s_lower.antecedent):
        return False
    antecedent_uniq = []
    for i in range(len(s_upper.antecedent)):
        if not s_upper.antecedent[i] in antecedent_uniq:
            antecedent_uniq.append(s_upper.antecedent[i])
        if not s_lower.antecedent[i] in antecedent_uniq:
            antecedent_uniq.append(s_lower.antecedent[i])
    for uniq in antecedent_uniq:
        counter_up = 0
        counter_low = 0
        for i in range(len(s_upper.antecedent)):
            if uniq == s_upper.antecedent[i]:
                counter_up += 1
            if uniq == s_lower.antecedent[i]:
                counter_low += 1
        if not counter_up == counter_low:
            return False
    return True


def exchange_right(s_upper, s_lower):
    if s_upper.antecedent != s_lower.antecedent:
        return False
    if len(s_upper.succedent) != len(s_lower.succedent):
        return False
    succedent_uniq = []
    for i in range(len(s_upper.succedent)):
        if not s_upper.succedent[i] in succedent_uniq:
            succedent_uniq.append(s_upper.succedent[i])
        if not s_lower.succedent[i] in succedent_uniq:
            succedent_uniq.append(s_lower.succedent[i])
    for uniq in succedent_uniq:
        counter_up = 0
        counter_low = 0
        for i in range(len(s_upper.succedent)):
            if uniq == s_upper.succedent[i]:
                counter_up += 1
            if uniq == s_lower.succedent[i]:
                counter_low += 1
        if not counter_up == counter_low:
            return False
    return True


def contraction_left(s_upper, s_lower):
    if s_upper.succedent != s_lower.succedent:
        return False
    if len(s_upper.antecedent) <= len(s_lower.antecedent):
        return False
    set_upper = set(s_upper.antecedent)
    set_lower = set(s_lower.antecedent)
    if not set_lower == set_upper:
        return False
    for uniq in set_upper:
        counter_up = 0
        counter_low = 0
        for i in range(len(s_upper.antecedent)):
            if uniq == s_upper.antecedent[i]:
                counter_up += 1
            if i < len(s_lower.antecedent):
                if uniq == s_lower.antecedent[i]:
                    counter_low += 1
        if not counter_up >= counter_low:
            return False
    return True


def contraction_right(s_upper, s_lower):
    if s_upper.antecedent != s_lower.antecedent:
        return False
    if len(s_upper.succedent) <= len(s_lower.succedent):
        return False
    set_upper = set(s_upper.succedent)
    set_lower = set(s_lower.succedent)
    if not set_lower == set_upper:
        return False
    for uniq in set_upper:
        counter_up = 0
        counter_low = 0
        for i in range(len(s_upper.succedent)):
            if uniq == s_upper.succedent[i]:
                counter_up += 1
            if i < len(s_lower.succedent):
                if uniq == s_lower.succedent[i]:
                    counter_low += 1
        if not counter_up >= counter_low:
            return False
    return True


def weakening_left(s_upper, s_lower):
    if s_upper.succedent != s_lower.succedent:
        return False
    if len(s_upper.antecedent) >= len(s_lower.antecedent):
        return False
    antecedent_uniq = []
    for i in range(len(s_lower.antecedent)):
        if i < len(s_upper.antecedent):
            if not s_upper.antecedent[i] in antecedent_uniq:
                antecedent_uniq.append(s_upper.antecedent[i])
        if not s_lower.antecedent[i] in antecedent_uniq:
            antecedent_uniq.append(s_lower.antecedent[i])
    for uniq in antecedent_uniq:
        counter_up = 0
        counter_low = 0
        for i in range(len(s_lower.antecedent)):
            if i < len(s_upper.antecedent):
                if uniq == s_upper.antecedent[i]:
                    counter_up += 1
            if uniq == s_lower.antecedent[i]:
                counter_low += 1
        if counter_up > counter_low:
            return False
    return True


def weakening_right(s_upper, s_lower):
    if s_upper.antecedent != s_lower.antecedent:
        return False
    if len(s_upper.succedent) >= len(s_lower.succedent):
        return False
    succedent_uniq = []
    for i in range(len(s_lower.succedent)):
        if i < len(s_upper.succedent):
            if not s_upper.succedent[i] in succedent_uniq:
                succedent_uniq.append(s_upper.succedent[i])
        if not s_lower.succedent[i] in succedent_uniq:
            succedent_uniq.append(s_lower.succedent[i])
    for uniq in succedent_uniq:
        counter_up = 0
        counter_low = 0
        for i in range(len(s_lower.succedent)):
            if i < len(s_upper.succedent):
                if uniq == s_upper.succedent[i]:
                    counter_up += 1
            if uniq == s_lower.succedent[i]:
                counter_low += 1
        if counter_up > counter_low:
            return False
    return True


def cut(s_upper1, s_upper2, s_lower):
    if s_upper1.antecedent != s_upper2.antecedent[:-1]:
        return False
    if s_upper1.succedent[:-1] != s_upper2.succedent:
        return False
    if s_lower.succedent != s_upper2.succedent:
        return False
    if s_lower.antecedent != s_upper1.antecedent:
        return False
    if s_upper1.succedent[-1] != s_upper2.antecedent[-1]:
        return False
    return True


def not_left(s_upper, s_lower):
    if s_upper.antecedent != s_lower.antecedent[1:]:
        return False
    if s_upper.succedent[:-1] != s_lower.succedent:
        return False
    A = s_upper.succedent[-1]
    not_A = s_lower.antecedent[0]
    if not_A.quantifier:
        return False
    if not_A.formulae_arr[0] != symb.l_not:
        return False
    if not_A.formulae_arr[1] != A:
        return False
    return True


def not_right(s_lower, s_upper):
    if s_upper.antecedent != s_lower.antecedent[1:]:
        return False
    if s_upper.succedent[:-1] != s_lower.succedent:
        return False
    not_A = s_upper.succedent[-1]
    A = s_lower.antecedent[0]
    if not_A.quantifier:
        return False
    if not_A.formulae_arr[0] != symb.l_not:
        return False
    if not_A.formulae_arr[1] != A:
        return False
    return True


def and_left(s_upper, s_lower):
    if s_upper.antecedent[2:] != s_lower.antecedent[1:]:
        return False
    if s_upper.succedent != s_lower.succedent:
        return False
    A_and_B = s_lower.antecedent[0]
    if not A_and_B.formulae_arr[1] == symb.l_and:
        return False
    if A_and_B.quantifier:
        return False
    A = s_upper.antecedent[0]
    B = s_upper.antecedent[1]
    if A != A_and_B.formulae_arr[0]:
        return False
    if B != A_and_B.formulae_arr[2]:
        return False
    return True


def and_right(s_upper1, s_upper2, s_lower):
    if s_upper1.succedent[:-1] != s_upper2.succedent[:-1]:
        return False
    if s_upper1.succedent[:-1] != s_lower.succedent[:-1]:
        return False
    if s_upper1.antecedent != s_upper2.antecedent:
        return False
    if s_upper1.antecedent != s_lower.antecedent:
        return False
    A = s_upper1.succedent[-1]
    B = s_upper2.succedent[-1]
    A_and_B = s_lower.succedent[-1]
    if A != A_and_B.formulae_arr[0]:
        return False
    if A_and_B.formulae_arr[1] != symb.l_and:
        return False
    if A_and_B.quantifier:
        return False
    if B != A_and_B.formulae_arr[2]:
        return False
    return True


def or_left(s_upper1, s_upper2, s_lower):
    if not s_upper1.succedent == s_upper2.succedent and s_upper2.succedent == s_lower.succedent:
        return False
    if not s_upper1.antecedent[1:] == s_upper2.antecedent[1:]:
        return False
    A_or_B = s_lower.antecedent[0]
    if not A_or_B.formulae_arr[1] == symb.l_or:
        return False
    if A_or_B.quantifier:
        return False
    A = s_upper1.antecedent[0]
    B = s_upper2.antecedent[0]
    if A != A_or_B.formulae_arr[0]:
        return False
    if B != A_or_B.formulae_arr[2]:
        return False
    return True


def or_right(s_upper, s_lower):
    if s_upper.succedent[:-2] != s_lower.succedent[:-1]:
        return False
    if s_upper.antecedent != s_lower.antecedent:
        return False
    A_or_B = s_lower.succedent[-1]
    if not A_or_B.formulae_arr[1] == symb.l_or:
        return False
    if A_or_B.quantifier:
        return False
    A = s_upper.succedent[-2]
    B = s_upper.succedent[-1]
    if A != A_or_B.formulae_arr[0]:
        return False
    if B != A_or_B.formulae_arr[2]:
        return False
    return True


def imp_left(s_upper1, s_upper2, s_lower):
    if s_upper1.antecedent != s_upper2.antecedent[1:]:
        return False
    if s_upper1.antecedent != s_lower.antecedent[1:]:
        return False
    if s_upper1.succedent[:-1] != s_upper2.succedent:
        return False
    if s_upper1.succedent[:-1] != s_lower.succedent:
        return False
    A = s_upper1.succedent[-1]
    B = s_upper2.antecedent[0]
    A_imp_B = s_lower.antecedent[0]
    if A_imp_B.formulae_arr[1] != symb.l_implication:
        return False
    if A_imp_B.quantifier:
        return False
    if A != A_imp_B.formulae_arr[0]:
        return False
    if B != A_imp_B.formulae_arr[2]:
        return False
    return True


def imp_right(s_upper, s_lower):
    if s_upper.succedent[:-1] != s_lower.succedent[:-1]:
        return False
    if s_upper.antecedent[1:] != s_lower.antecedent:
        return False
    A_imp_B = s_lower.succedent[-1]
    if not A_imp_B.formulae_arr[1] == symb.l_implication:
        return False
    if A_imp_B.quantifier:
        return False
    A = s_upper.antecedent[0]
    B = s_upper.succedent[-1]
    if A != A_imp_B.formulae_arr[0]:
        return False
    if B != A_imp_B.formulae_arr[2]:
        return False
    return True


def univ_left(s_upper, s_lower):
    if s_upper.antecedent[1:] != s_lower.antecedent[1:]:
        return False
    if s_upper.succedent != s_lower.succedent:
        return False
    A_upper = s_upper.antecedent[0]
    A_lower = s_lower.antecedent[0]

    if not A_lower.quantifier:
        return False
    if A_lower.quantifier[0] != symb.q_universal:
        return False
    quantified_variable = A_lower.quantifier[1]
    A_lower = s_lower.antecedent[0].formulae_arr[0]
    upper_arr = A_upper.get_P_t_f_var([])
    lower_arr = A_lower.get_P_t_f_var([])
    term = 0
    for i in range(len(upper_arr)):
        if lower_arr[i] == quantified_variable:
            term = upper_arr[i]
            break
    if not (isinstance(term, Term) or isinstance(term, Variable)):
        return False
    A_lower_text = A_lower.text()
    A_lower_text = A_lower_text.replace(quantified_variable.text(), term.text())
    if A_lower_text != A_upper.text():
        return False
    return True


def exist_left(s_upper, s_lower):
    if s_upper.antecedent[1:] != s_lower.antecedent[1:]:
        return False
    if s_upper.succedent != s_lower.succedent:
        return False
    A_upper = s_upper.antecedent[0]
    A_lower = s_lower.antecedent[0]

    if not A_lower.quantifier:
        return False
    if A_lower.quantifier[0] != symb.q_existential:
        return False
    quantified_variable = A_lower.quantifier[1]
    A_lower = s_lower.antecedent[0].formulae_arr[0]
    upper_arr = A_upper.get_P_t_f_var([])
    lower_arr = A_lower.get_P_t_f_var([])
    variable = 0
    for i in range(len(upper_arr)):
        if lower_arr[i] == quantified_variable:
            variable = upper_arr[i]
            break
    if not isinstance(variable, Variable):
        return False
    A_lower_text = A_lower.text()
    A_lower_text = A_lower_text.replace(quantified_variable.text(), variable.text())
    if A_lower_text != A_upper.text():
        return False
    return True


def univ_right(s_upper, s_lower):
    if s_upper.succedent[:-1] != s_lower.succedent[:-1]:
        return False
    if s_upper.antecedent != s_lower.antecedent:
        return False
    A_upper = s_upper.succedent[-1]
    A_lower = s_lower.succedent[-1]

    if not A_lower.quantifier:
        return False
    if A_lower.quantifier[0] != symb.q_universal:
        return False
    quantified_variable = A_lower.quantifier[1]
    A_lower = s_lower.succedent[-1].formulae_arr[0]
    upper_arr = A_upper.get_P_t_f_var([])
    lower_arr = A_lower.get_P_t_f_var([])
    variable = 0
    for i in range(len(upper_arr)):
        if lower_arr[i] == quantified_variable:
            variable = upper_arr[i]
            break
    if not isinstance(variable, Variable):
        return False
    A_lower_text = A_lower.text()
    A_lower_text = A_lower_text.replace(quantified_variable.text(), variable.text())
    if A_lower_text != A_upper.text():
        return False
    return True


def exist_right(s_upper, s_lower):
    if s_upper.succedent[:-1] != s_lower.succedent[:-1]:
        return False
    if s_upper.antecedent != s_lower.antecedent:
        return False
    A_upper = s_upper.succedent[-1]
    A_lower = s_lower.succedent[-1]

    if not A_lower.quantifier:
        return False
    if A_lower.quantifier[0] != symb.q_existential:
        return False
    quantified_variable = A_lower.quantifier[1]
    A_lower = s_lower.succedent[-1].formulae_arr[0]
    upper_arr = A_upper.get_P_t_f_var([])
    lower_arr = A_lower.get_P_t_f_var([])
    term = 0
    for i in range(len(upper_arr)):
        if lower_arr[i] == quantified_variable:
            term = upper_arr[i]
            break
    if not (isinstance(term, Term) or isinstance(term, Variable)):
        return False
    A_lower_text = A_lower.text()
    A_lower_text = A_lower_text.replace(quantified_variable.text(), term.text())
    if A_lower_text != A_upper.text():
        return False
    return True
