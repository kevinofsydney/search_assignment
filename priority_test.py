from queue import PriorityQueue

q = PriorityQueue()

q.put((1, 2*-1, "F"))
q.put((1, 3*-1, "F"))

while not q.empty():
    print(q.get())
