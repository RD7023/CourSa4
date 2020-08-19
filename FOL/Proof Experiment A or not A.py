from FOL.Alphabet import q_existential, q_universal, l_implication
from FOL.Variable import Variable
from FOL.AtomicFormulae import AtomicFormulae
from FOL.Formulae import Formulae
from FOL.Function import Function
from FOL.Term import Term
from FOL.Sequence import Sequence
from FOL.Node import Node
from FOL.Proof import Proof

x = Variable('x')
y = Variable('y')
f = Function('f', [x])
f = Term('t', [f])
q = AtomicFormulae('Q', [y])
q = Formulae([], [q])
p_f = AtomicFormulae('P', [f])
p = AtomicFormulae('P', [x])
p_f = Formulae([], [p_f])
p = Formulae([], [p])
univ_p = Formulae([q_universal, x], [p])
univ_p_f = Formulae([q_universal, x], [p_f])
imp_univ_p_f_Q = Formulae([], [univ_p_f, l_implication, q])
imp_imp_univ_p_f_Q_Q = Formulae([], [imp_univ_p_f_Q, l_implication, q])
imp_imp_univ_p_univ_p_f_Q_Q = Formulae([], [univ_p, l_implication, imp_imp_univ_p_f_Q_Q])

Sequence1 = Sequence([], [imp_imp_univ_p_univ_p_f_Q_Q])
Sequence2 = Sequence([univ_p], [imp_imp_univ_p_f_Q_Q])
Sequence3 = Sequence([imp_univ_p_f_Q, univ_p], [q])
Sequence4_1 = Sequence([q], [q])
Sequence4_2 = Sequence([univ_p], [univ_p_f])
Sequence5 = Sequence([univ_p], [p_f])
Sequence6 = Sequence([p], [p_f])

Node1 = Node(Sequence1, None, [Sequence2], 'imp right')
Node2 = Node(Sequence2, Sequence1, [Sequence3], 'imp right')
Node3 = Node(Sequence3, Sequence2, [Sequence4_1, Sequence4_2], 'imp left')
Node4_1 = Node(Sequence4_1, Sequence3, [], '')
Node4_2 = Node(Sequence4_2, Sequence3, [Sequence5], 'univ right')
Node5 = Node(Sequence5, Sequence4_2, [Sequence6], 'univ left')
Node6 = Node(Sequence6, Sequence5, [], '')

Proof1 = Proof()

Proof1.add_node(Node1, 0)
Proof1.add_node(Node2, 1)
Proof1.add_node(Node3, 2)
Proof1.add_node(Node4_1, 3)
Proof1.add_node(Node4_2, 3)
Proof1.add_node(Node5, 4)
Proof1.add_node(Node6, 5)

Proof1.print()
Proof1.check_proof()
