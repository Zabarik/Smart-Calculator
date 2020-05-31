from collections import deque

fifo = deque()
nbr = int(input())
actions = [input().split() for _ in range(nbr)]
for a in actions:
    if a[0] == "READY":
        fifo.append(a[1])
    elif a[0] == "EXTRA":
        fifo.append(fifo[0])
        fifo.popleft()
    else:
        print(fifo.popleft())
