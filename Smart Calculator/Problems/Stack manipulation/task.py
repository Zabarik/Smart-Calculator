nbr = int(input())
actions = [input().split(" ", 1) for _ in range(nbr)]
stack = []
for a in actions:
    stack.append(a[1]) if a[0] == "PUSH" else stack.pop()
print(*stack[::-1], sep="\n")
