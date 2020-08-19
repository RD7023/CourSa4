class Proof:
    def __init__(self):
        self.proof = {}

    def add_node(self, node, level):
        if level == 0:
            assert node.parent_sequence == None
        if level > 0:
            assert node.parent_sequence in [node.value for node in self.proof['Level ' + str(level - 1)]]
        if 'Level ' + str(level) in self.proof:
            self.proof['Level ' + str(level)].append(node)
        else:
            self.proof['Level ' + str(level)] = [node]

    def print(self):
        for level in self.proof:
            for node in self.proof[level]:
                print(node.value.text(), end='', sep='')
                print('(' + node.rule + ')', '', '  ')
            print('')

    def check_proof(self):
        for level in self.proof:
            for node in self.proof[level]:
                if not node.check_node():
                    print("Error here :")
                    print(level)
                    print(node.value.text())
                    desc_arr = [seq.text() for seq in node.descendant_sequence_arr]
                    print(node.rule)
                    for i in range(len(desc_arr)):
                        print(desc_arr[i], sep='   ', end='   ')
                    return False
        return True
