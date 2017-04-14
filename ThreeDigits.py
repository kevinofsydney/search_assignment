###################
#                 #
#     C O M P     #
#     3 3 0 8     #
#                 #
#      Three      #
#      Digits     #           @kevinofsydney
#                 #
###################

####    TODO LIST   ###
# -  Implement the following algorithms
#       - IDS
#       - Greedy
#       - Hill-Climbing
#       - A*
# - Handle choosing a particular method
# - Expanded list can only contain 1,000 nodes
#======================

####    NOTES   ####
# if __name__ == "__main__"-> what the hell is this
from queue import Queue
import sys

start = 000
target = 000
forbidden = []

class Node(object):
    def __init__(self, number, changed, parent):
        self.number = number
        self.children = []
        self.changed = changed #digit that was changed, range is [1-3]
        self.parent = parent

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
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

        
#This function creates all the children for a given node
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


def print_answer(expanded, goal):
    #This is the string of the path from the start to the goal
    exp_nodes = [goal.get_number()]
    path_string = "" + str(expanded[0].get_number())
    #This is the string of expanded nodes
    exp_string = "" + str(expanded[0].get_number())

    temp = goal
    while (temp.get_parent() is not None):
        exp_nodes.append(temp.get_parent().get_number())
        temp = temp.get_parent()
 
    exp_nodes.reverse() 
    for i in range(1, len(exp_nodes)):
        path_string = path_string + "," + str(exp_nodes[i])
    
    for i in range(1, len(expanded)):
        exp_string = exp_string + "," + str(expanded[i].get_number())

    print(path_string) 
    print(exp_string)


def bfs(root):
    expanded = []
    fringe = Queue()

    fringe.put(root) 

    while not fringe.empty():
        node = fringe.get()

        if (node in expanded):
            continue
        elif (node.get_number() in forbidden):
            continue

        child_creator(node)
        current = node.get_number()
        expanded.append(node)
       
        if (current is target):
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
        
        if (node in expanded):
            continue
        elif (node.get_number() in forbidden):
            continue
        
        child_creator(node)
        current = node.get_number()
        expanded.append(node)
       
        if (current is target):
            break
        else:
            while (len(node.get_children()) > 0):
                fringe.push(node.get_children().pop())

    return expanded, node


def read_input():
    with open(sys.argv[2], 'r') as infile:
        global start
        global target
        global forbidden

        start = int(infile.readline())
        target = int(infile.readline())
        last = infile.readline()

        forbidden = []

        for i in (last.split(",")):
            forbidden.append(int(i))


def main():
    print("ThreeDigits started.")
    read_input()
    print("Start is " + str(start) + ".")
    print("Target is " + str(target) + ".")

    #This initialises the root node. Needed for every algorithm
    root = Node(start, 4, None)
   
    ### BFS ###
    expanded, goal = bfs(root)
    print("###    BFS    ###")
    print_answer(expanded, goal)

    ### DFS ###
    ex2, goal2 = dfs(root)
    print("###   DFS   ###")
    print_answer(ex2, goal2)

    return;

main();
