start = 999
target = 115

#Also need a priority queue implementation
def manhattan(number):
    t_hun = int(target / 100)
    t_ten = int((target % 100) / 10)
    t_one = (target % 100) % 10

    s_hun = int(number / 100)
    s_ten = int((number % 100) / 10)
    s_one = (number % 100) % 10

    dist = (abs(t_hun - s_hun) + abs(t_ten - s_ten) + abs(t_one - s_one))

    print(t_hun, t_ten, t_one, s_hun, s_ten, s_one)
    print(dist)

manhattan(start)
