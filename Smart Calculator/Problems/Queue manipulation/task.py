from collections import deque

fifo = deque()
nbr = int(input())
actions = [input().split() for _ in range(nbr)]
for a in actions:
    fifo.append(a[1]) if a[0] == "ENQUEUE" else fifo.popleft()
print(*fifo, sep="\n")
