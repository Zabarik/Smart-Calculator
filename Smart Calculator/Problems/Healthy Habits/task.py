# the list "walks" is already defined
# your code here
values = [d["distance"] for d in walks]
print(int(sum(values) / len(values)))
