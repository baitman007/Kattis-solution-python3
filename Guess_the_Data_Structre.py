import heapq
from collections import deque, Counter

S_index = 0
Q_index = 1
H_index = 2


def get_data_structure_type(n):
    stack = deque()  # append, pop
    queue = deque()  # append, popleft
    heap = []  # heapq.heappush, heapq.heappop

    data_structure_type = [True, True, True]

    for _ in range(n):
        opcode, value = list(map(int, input().split()))
        if opcode == 1:
            stack.append(value)
            queue.append(value)
            heapq.heappush(heap, -value)
        else:
            if len(stack) == 0:
                data_structure_type = [False, False, False]
                continue

            s_result = stack.pop()
            q_result = queue.popleft()
            h_result = -heapq.heappop(heap)

            if s_result != value:
                data_structure_type[S_index] = False
            if q_result != value:
                data_structure_type[Q_index] = False
            if h_result != value:
                data_structure_type[H_index] = False

    return data_structure_type


try:
    while True:
        n = int(input())
        data_structure_type = get_data_structure_type(n)

        counter = Counter(data_structure_type)
        if counter[False] == 3:
            print("impossible")
        elif counter[True] > 1:
            print("not sure")
        elif data_structure_type[S_index]:
            print("stack")
        elif data_structure_type[Q_index]:
            print("queue")
        else:
            print("priority queue")
except EOFError:
    pass