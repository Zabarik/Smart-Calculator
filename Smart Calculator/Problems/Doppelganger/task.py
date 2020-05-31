from collections.abc import Hashable

# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
hashable_list = [hash(x) for x in object_list if isinstance(x, Hashable)]
hashable_set = set(hashable_list)
duplicates = [hashable_list.count(x) for x in hashable_set if hashable_list.count(x) > 1]
print(sum(duplicates))
