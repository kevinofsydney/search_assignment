import sys
target = 555

def manhattan(number):

    t_hun = int(target / 100)
    t_ten = int((target % 100) / 10)
    t_one = (target % 100) % 10

    s_hun = int(number / 100)
    s_ten = int((number % 100) / 10)
    s_one = (number % 100) % 10

    dist = (abs(t_hun - s_hun) + abs(t_ten - s_ten) + abs(t_one - s_one))
    return dist

def main():
    global target
    node = int(sys.argv[1])
    # target = int(sys.argv[2])

    print(manhattan(node))

main()
