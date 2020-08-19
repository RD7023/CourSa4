from FOL.Alphabet import q_existential, q_universal
from FOL.Variable import Variable
from FOL.AtomicFormulae import AtomicFormulae
from FOL.Formulae import Formulae
from FOL.Sequence import Sequence
from FOL.Node import Node
from FOL.Proof import Proof
x = Variable('x')
y = Variable('y')
p = AtomicFormulae('P', [x, y])
p = Formulae([], [p])
univ_x_p = Formulae([q_universal, x], [p])
exist_y_p = Formulae([q_existential, y], [p])
exist_y_univ_x_p = Formulae([q_existential, y], [univ_x_p])
univ_x_exist_y_p = Formulae([q_universal, x], [exist_y_p])

Sequence1 = Sequence([exist_y_univ_x_p], [univ_x_exist_y_p])
Sequence2 = Sequence([exist_y_univ_x_p], [exist_y_p])
Sequence3 = Sequence([univ_x_p], [exist_y_p])
Sequence4 = Sequence([univ_x_p], [p])
Sequence5 = Sequence([p], [p])

Node1 = Node(Sequence1, None, [Sequence2], 'univ right')
Node2 = Node(Sequence2, Sequence1, [Sequence3], 'exist left')
Node3 = Node(Sequence3, Sequence2, [Sequence4], 'exist right')
Node4 = Node(Sequence4, Sequence3, [Sequence5], 'univ left')
Node5 = Node(Sequence5, Sequence4, [], '')

Proof1 = Proof()

Proof1.add_node(Node1, 0)
Proof1.add_node(Node2, 1)
Proof1.add_node(Node3, 2)
Proof1.add_node(Node4, 3)
Proof1.add_node(Node5, 4)
Proof1.print()
print(Proof1.check_proof())
