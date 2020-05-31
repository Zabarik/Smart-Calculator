nbr = int(input())
actions = [input().split(" ", 1) for _ in range(nbr)]
books = []
for i in range(len(actions)):
    if actions[i][0] == "BUY":
        books.append(actions[i][1])
    else:
        print(books.pop())
