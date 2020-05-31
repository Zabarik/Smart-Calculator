from collections import deque

fifo = deque()
nbr = int(input())
actions = [input().split() for _ in range(nbr)]
for a in actions:
    fifo.appendleft(a[1]) if a[0] == "ISSUE" else fifo.pop()
fifo.reverse()
print(*fifo, sep="\n")
