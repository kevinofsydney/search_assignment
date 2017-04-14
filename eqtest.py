class Node(object):
    def __init__(self, number, changed, parent):
        self.number = number
        self.children = []
        self.changed = changed #digit that was changed, range is [1-3]
        self.parent = parent

    def add_child(self, obj):
        self.children.append(obj)

    def get_number(self):
        return self.number

    def get_changed(self):
        return self.changed

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def __eq__(self, other):
        return self.number == other.number and self.children == other.children


def child_creator(parent):
    pnum = parent.get_number()
    pchange = parent.get_changed()

    up = pnum + 100
    down = pnum - 100

    if (pnum < 900 and pchange is not 1):
        childA = Node(down, 1, parent)
        parent.add_child(childA)

    if (pnum > 200 and pchange is not 1):
        childB = Node(up, 1, parent)
        parent.add_child(childB)

    ptens = pnum % 100
    ptens_up = pnum + 10
    ptens_down = pnum - 10

    if (ptens < 90 and pchange is not 2):
        childC = Node(ptens_down, 2, parent)
        parent.add_child(childC)

    if (ptens > 19 and pchange is not 2):
        childD = Node(ptens_up, 2, parent)
        parent.add_child(childD)

    pones = ptens % 10
    pones_up = pnum + 1
    pones_down = pnum - 1

    if (pones > 1 and pchange is not 3):
        childE = Node(pones_down, 3, parent)
        parent.add_child(childE)

    if (pones < 9 and pchange is not 3):
        childF = Node(pones_up, 3, parent)
        parent.add_child(childF)

    return


A = Node(320, 0, None)
B = Node(320, 0, None)

child_creator(A)
child_creator(B)

testlist = []
testlist.append(B)

print(A in testlist)
