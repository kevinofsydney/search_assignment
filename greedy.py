from queue import PriorityQueue, Queue
import time

start = 320
target = 110
forbidden = []

class Node(object):
    def __init__(self, number, changed, parent, depth):
        self.number = number
        self.children = []
        self.changed = changed  # digit that was changed, range is [1-3]
        self.parent = parent
        self.depth = depth

    def __eq__(self, other):
        return self.number == other.number and self.children == other.children

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


def child_creator(parent):
    # Cannot add to 9
    # Cannot subtract from 0
    pnum = parent.get_number()
    pchange = parent.get_changed()

    up = pnum + 100
    down = pnum - 100

    if pnum > 99 and pchange is not 1:
        childA = Node(down, 1, parent, parent.depth + 1)
        parent.add_child(childA)

    if pnum < 900 and pchange is not 1:
        childB = Node(up, 1, parent, parent.depth + 1)
        parent.add_child(childB)

    ptens = pnum % 100
    ptens_up = pnum + 10
    ptens_down = pnum - 10

    if ptens > 9 and pchange is not 2:
        childC = Node(ptens_down, 2, parent, parent.depth + 1)
        parent.add_child(childC)

    if ptens < 90 and pchange is not 2:
        childD = Node(ptens_up, 2, parent, parent.depth + 1)
        parent.add_child(childD)

    pones = ptens % 10
    pones_up = pnum + 1
    pones_down = pnum - 1

    if pones > 0 and pchange is not 3:
        childE = Node(pones_down, 3, parent, parent.depth + 1)
        parent.add_child(childE)

    if pones < 9 and pchange is not 3:
        childF = Node(pones_up, 3, parent, parent.depth + 1)
        parent.add_child(childF)

    return


def print_answer(expanded, goal):
    # This is the string of the path from the start to the goal
    exp_nodes = [goal.get_number()]
    path_string = "" + str(expanded[0].get_number())
    # This is the string of expanded nodes
    exp_string = "" + str(expanded[0].get_number())

    temp = goal
    while temp.get_parent() is not None:
        exp_nodes.append(temp.get_parent().get_number())
        temp = temp.get_parent()

    exp_nodes.reverse()
    for i in range(1, len(exp_nodes)):
        path_string = path_string + "," + str(exp_nodes[i])

    for i in range(1, len(expanded)):
        exp_string = exp_string + "," + str(expanded[i].get_number())

    print(path_string)
    print(exp_string)


# Multicheck() performs the following checks common to each method:
#   - whether the current node is  already in the expanded list
#   - whether the current node is in the forbidden list
#   - whether expanded is above 1000 elements
def multicheck(node, expanded):
    if node in expanded:
        return 1
    elif node.get_number() in forbidden:
        return 1
    elif len(expanded) >= 1000:
        print("No solution found.")
        return 2

    return 0


def manhattan(node):
    number = node.get_number()

    t_hun = int(target / 100)
    t_ten = int((target % 100) / 10)
    t_one = (target % 100) % 10

    s_hun = int(number / 100)
    s_ten = int((number % 100) / 10)
    s_one = (number % 100) % 10

    dist = (abs(t_hun - s_hun) + abs(t_ten - s_ten) + abs(t_one - s_one))
    return dist


def greedy(root):
    fringe = PriorityQueue()
    expanded = []
    full = [(0, 0, root)]
    fringe.put((0, 0, root))

    i = 0
    while not fringe.empty():
        node = fringe.get()[2]
        child_creator(node)

        if multicheck(node, expanded) == 1:
            continue
        elif multicheck(node, expanded) == 2:
            return

        current = node.get_number()
        expanded.append(node)

        if current is target:
            break
        else:
            for child in node.get_children():
                priority = manhattan(child)
                fringe.put((priority, time.time() * -1, child))

    return expanded, node


def main():

    root = Node(start, 4, None, 0)

    expanded, goal = greedy(root)
    print_answer(expanded, goal)

    return 0


main()
