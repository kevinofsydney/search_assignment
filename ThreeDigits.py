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
# -  Make node/leaf objects 
#       - note that a node in a linked list has only one child
#           while a node in a tree could have many children
# -  Construct a tree
# -  Implement the following algorithms
#       - BFS
#       - DFS
#       - IDS
#       - Greedy
#       - Hill-Climbing
#       - A*

#======================

####    NOTES   ####
# if __name__ == "__main__"-> what the hell is this
start = 345
goal = 555

#though I will need to read in the forbidden numbers from the command line

class Node(object):
    def __init__(self, number, changed):
        self.number = number
        self.children = []
        self.changed = changed #digit that was changed, range is [1-3]

    def add_child(self, obj):
        self.children.append(obj)

    def get_number(self):
        return self.number

    def get_changed(self):
        return self.changed

#This function creates all the children for a given node
def child_creator(parent):
    pnum = parent.get_number()
    pchange = parent.get_changed()

    up = pnum + 100
    down = pnum - 100
    
    if (pnum > 200 and pchange is not 1):
        print(pnum, "->", up)
        childA = Node(up, 1)
        parent.add_child(childA)

    if (pnum < 900 and pchange is not 1):
        print(pnum, "<-", down)
        childB = Node(down, 1)
        parent.add_child(childB)

    ptens = pnum % 100
    ptens_up = pnum + 10
    ptens_down = pnum - 10

    if (ptens < 90 and pchange is not 2):
        print(pnum, "->", ptens_up)
        childC = Node(ptens_up, 2)

    if (ptens > 19 and pchange is not 2):
        print(pnum, "<-", ptens_down)
        childD = Node(ptens_up, 2)
        parent.add_child(childD)

    pones = ptens % 10
    pones_up = pnum + 1
    pones_down = pnum - 1

    if (pones < 9 and pchange is not 3):
        print(pnum, "->", pones_up)
        childE = Node(pones_up, 3)
        parent.add_child(childE)

    if (pones > 1 and pchange is not 3):
        print(pnum, "<-", pones_down)
        childF = Node(pones_down, 3)
        parent.add_child(childF)

    return 


def main():
    print("ThreeDigits started.")
    print("Start is 345.\nGoal is 555.")

    root = Node(start, 4)
   
    child_creator(root)
    return;

main();
