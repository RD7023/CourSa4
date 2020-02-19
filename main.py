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

print('Preposition 1:')
print(atom1.text)


formula1 = Formula(0, True, [[atom1, atom1], [0, 2]], [[l_and], [1]])
formula2 = Formula(1, True, [[atom1, formula1], [0, 2]], [[l_or], [1]])

print('Formula 1:')
formula1.print_formula()
print('Formula 2:')
formula2.print_formula()


sequence1 = Sequence(0, True, [formula2, formula1, formula2], [formula2])
sequence2 = Sequence(1, True, [formula1, formula2, formula2], [formula2])

print('Inference 1:')
inference1 = Inference(sequence1,sequence2)
print(inference1.check_exchange_left())
