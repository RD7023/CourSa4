import FOL.Alphabet as Symb
from FOL.Variable import Variable
from FOL.Constant import Constant
from FOL.Function import Function
from FOL.Term import Term
from FOL.AtomicFormulae import AtomicFormulae
from FOL.Formulae import Formulae
from FOL.Sequence import Sequence
import FOL.InferenceCheck as check


x = Variable('x')
y = Variable('y')
z = Variable('z')

a = Constant('a')
b = Constant('b')
c = Constant('c')

f = Function('f', [y])
g = Function('g', [z])
h = Function('h', [x, y, z])

g1 = Term('g1', [f, h, f])
f1 = Term('f1', [f, g1])
f1_x = Term('f1', [f, x])


P = AtomicFormulae('P', [f1])
P_x = AtomicFormulae('P', [f1_x])
Q = AtomicFormulae('Q', [g1, f1])


F = Formulae([], [P])
F_x = Formulae([], [P_x])
A = Formulae([Symb.q_universal, x], [F_x])

Q = Formulae([], [Q, Symb.l_or, P])

S1 = Sequence([F, F, F], [Q, Q])
#  S2 = Sequence([F, Q, F], [Q, Q])
S = Sequence([A, F, F], [Q, Q])


#print(check.univ_left(S1, S))
