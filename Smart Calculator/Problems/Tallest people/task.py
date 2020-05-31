def tallest_people(**kwargs):
    max_value = max(kwargs.values())
    pairs = [f"{name} : {height}" for name, height in kwargs.items() if height == max_value]
    pairs.sort()
    print(*pairs, sep="\n")
