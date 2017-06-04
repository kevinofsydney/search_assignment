###################
#                 #
#     C O M P     #
#     3 3 0 8     #
#                 #
#      Three      #
#      Digits     #           @kevinofsydney
#                 #
###################

#   === TODO LIST ===
# -  Implement the following algorithms
#       - IDS
#       - Hill-Climbing
# -  Print the expanded nodes even when no solution is found
# -  Print single digits correctly (e.g. start 000, goal 001)
# -  Split printing expanded and goal path
# ======================

#    === NOTES ===
# if __name__ == "__main__"-> what the hell is this
from queue import Queue, PriorityQueue
import sys
import time

start = 000
target = 000
forbidden = []
method = ""


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

    def get_depth(self):
        return self.depth


class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# This function creates all the children for a given node
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


def str_format(number):
    num_str = str(number)
    if number < 100 and int(number / 10) == 0:
        num_str = "0" + num_str

    if int(number / 100) == 0:
        num_str = "0" + num_str
    return num_str


def print_answer(expanded, goal):
    # This is the string of the path from the start to the goal
    path_string = "" + str_format(expanded[0].get_number())
    # This is the string of expanded nodes
    exp_string = "" + str_format(expanded[0].get_number())

    if goal is None:
        path_string = "No solution found."
    else:
        exp_nodes = [goal.get_number()]

        temp = goal
        while temp.get_parent() is not None:
            exp_nodes.append(temp.get_parent().get_number())
            temp = temp.get_parent()

        exp_nodes.reverse()
        for i in range(1, len(exp_nodes)):
            num_str = str_format(exp_nodes[i])
            path_string = path_string + "," + num_str

    print(path_string)

    for i in range(1, len(expanded)):
        exp_string = exp_string + "," + str_format(expanded[i].get_number())

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
        print_answer(expanded, None)
        raise SystemExit

    return 0


def bfs(root):
    expanded = []
    fringe = Queue()

    fringe.put(root)

    while not fringe.empty():
        node = fringe.get()
        child_creator(node)

        if multicheck(node, expanded) == 1:
            continue

        current = node.get_number()
        expanded.append(node)

        if current == target:
            break
        else:
            for child in node.get_children():
                fringe.put(child)

    return expanded, node


def dfs(root):
    fringe = Stack()
    expanded = []

    fringe.push(root)

    while not fringe.empty():
        node = fringe.pop()
        child_creator(node)

        if multicheck(node, expanded) == 1:
            continue

        current = node.get_number()
        expanded.append(node)

        if current == target:
            break
        else:
            while len(node.get_children()) > 0:
                fringe.push(node.get_children().pop())

        child_creator(node)
        # This crude hack is necessary to get the ordering of the
        #  children correct in the expanded list

    return expanded, node


def read_input():
    if len(sys.argv) == 1:
        raise SystemExit("No filename selected.")

    global method
    method = sys.argv[1]
    method = method.lower()
    method = method.strip()

    with open(sys.argv[2], 'r') as infile:
        global start
        global target
        global forbidden

        start = int(infile.readline())
        target = int(infile.readline())
        last = infile.readline()

        forbidden = []

        if last == '':
            return
        else:
            for i in (last.split(",")):
                forbidden.append(int(i))


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


# A star also needs to use the path cost (which is just the depth here)
def astar(root):
    fringe = PriorityQueue()
    expanded = []

    fringe.put((0, 0, root))

    # PriorityQueue: an entry is a tuple of the form (priority_number, data)

    while not fringe.empty():
        node = fringe.get()[2]
        child_creator(node)

        if multicheck(node, expanded) == 1:
            continue

        current = node.get_number()
        expanded.append(node)

        if current == target:
            break
        else:
            for child in node.get_children():
                priority = manhattan(child)
                fringe.put((priority + child.depth, time.time() * -1, child))

    return expanded, node


def greedy(root):
    fringe = PriorityQueue()
    expanded = []
    fringe.put((0, 0, root))

    while not fringe.empty():
        node = fringe.get()[2]
        child_creator(node)

        if multicheck(node, expanded) == 1:
            continue

        current = node.get_number()
        expanded.append(node)

        if current == target:
            break
        else:
            for child in node.get_children():
                priority = manhattan(child)
                fringe.put((priority, time.time() * -1, child))

    return expanded, node


def hill(root):
    # 1. Set the current node to the initial state S
    # 2. Generate the successors of n
    # 3. Select the best successor n_best
    # 4. If child is worse than parent, return parent
    # 5. If child is better than parent, set n to n_best and go to step 2

    fringe = PriorityQueue()
    expanded = []
    goal_found = False # This is 0 when the goal is found, and 1 otherwise

    node = root

    while not goal_found:
        heur_parent = manhattan(node)
        child_creator(node)
        expanded.append(node)

        if node.get_number() == target:
            goal_found = True
        else:
            for child in node.get_children():
                priority = manhattan(child)
                fringe.put((priority, time.time() * -1, child))

            forbidden_flag = True
            while forbidden_flag:
                heur_child, temp_time, best_child = fringe.get()
                if best_child.get_number() in forbidden:
                    continue
                else:
                    forbidden_flag = False

            if heur_child >= heur_parent:
                return expanded, None
            else:
                node = best_child

    return expanded, node


def ids(root):
    l = 0
    goal_found = False
    expanded = []

    while not goal_found:
        fringe = Stack()
        temp_expand = []
        fringe.push(root)

        while not fringe.empty():
            node = fringe.pop()
            root.children = []
            child_creator(node)

            if multicheck(node, temp_expand) == 1:
                continue
            elif len(expanded) >= 1000:
                print_answer(expanded, None)
                raise SystemExit

            current = node.get_number()
            expanded.append(node)
            temp_expand.append(node)
            if current == target:
                goal_found = True
                break
            elif l > node.get_depth():
                while len(node.get_children()) > 0:
                    child = node.get_children().pop()
                    fringe.push(child)

            child_creator(node)
            # This crude hack is necessary to get the ordering of the
            #  children correct in the expanded list

        l += 1

    return expanded, node



def main():
    read_input()
    # This initialises the root node. Needed for every algorithm
    root = Node(start, 4, None, 0)
    end = Node(target, 4, None, 0)

    if method == 'debug':
        print("### BFS ###")
        expanded, goal = bfs(root)
        print_answer(expanded, goal)

        print("### DFS ###")
        ex2, goal2 = dfs(root)
        print_answer(ex2, goal2)

        print("### Greedy ###")
        root = Node(start, 4, None, 0)
        ex3, goal3 = greedy(root)
        print_answer(ex3, goal3)

        print("### A* ###")
        root = Node(start, 4, None, 0)
        ex4, goal4 = astar(root)
        print_answer(ex4, goal4)

        print("### Hill Climbing ###")
        root = Node(start, 4, None, 0)
        ex5, goal5 = astar(root)
        print_answer(ex5, goal5)

        print("### IDS ###")
        root = Node(start, 4, None, 0)
        ex6, goal6 = ids(root)
        print_answer(ex6, goal6)
    elif method == 'b':
        # BFS
        expanded, goal = bfs(root)
        print_answer(expanded, goal)
    elif method == 'd':
        # DFS
        ex2, goal2 = dfs(root)
        print_answer(ex2, goal2)
    elif method == 'g':
        # greedy
        ex3, goal3 = greedy(root)
        print_answer(ex3, goal3)
    elif method == 'a':
        # A*
        ex4, goal4 = astar(root)
        print_answer(ex4, goal4)
    elif method == 'h':
        # Hill Climbing
        ex5, goal5 = hill(root)
        print_answer(ex5, goal5)
    elif method == 'i':
        # IDS
        ex6, goal6 = ids(root)
        print_answer(ex6, goal6)

    return 0


main()
