import LogicalSymbols as LS
from Atom import Atom
from Formula import Formula
from Sequence import Sequence
from Inference import Inference

l_not = LS.l_not
l_or = LS.l_or
l_and = LS.l_and
l_equiv = LS.l_equiv
l_implication = LS.l_implication
l_inference = LS.l_inference


atom1 = Atom(0, " I'm Batman ", True)
atom2 = Atom(1, " I'm Superman ", True)

print('Preposition 1:')
print(atom1.text)


formula1 = Formula(0, True, [[atom1], [0]], [[], []])

formula2 = Formula(1, True, [[formula1, formula1], [0, 2]], [[l_and], [1]])

formula3 = Formula(1, True, [[formula1, formula2], [0, 2]], [[l_implication], [1]])

formula4 = Formula(3, False, [[atom1, atom2], [0, 2]], [[l_and], [1]])

print('Formula 1:')
formula1.print_formula()

print('Formula 2:')
formula2.print_formula()


sequence10 = Sequence(0, True, [formula1, formula2], [formula1, formula1])
sequence11 = Sequence(2, True, [formula2, formula1], [formula1, formula1])

sequence2 = Sequence(1, True, [formula3, formula1, formula1], [formula1])

print('Inference 1:')
inference1 = Inference([sequence10, sequence11], sequence2)
inference1.print_inference()

print('Correct: ', end='')
print(inference1.check_implication_left())

print('Inference 2:')
inference2 = Inference(sequence10, sequence11)
inference2.print_inference()
print(inference2.check_exchange_left())












"""

print('Preposition 2:')
print(atom2.text)
formula3 = Formula(2, True, [[atom2], [1]], [[l_not], [0]])
formula3.print_formula()

formula4.print_formula()
sequence3 = Sequence(2, True, [formula3, formula4], [formula4])
sequence4 = Sequence(3, False, [formula4, formula4], [formula4, formula3])
inference2 = Inference(sequence3, sequence4)
inference2.print_inference()
print(inference2.check_weakening_right())
"""