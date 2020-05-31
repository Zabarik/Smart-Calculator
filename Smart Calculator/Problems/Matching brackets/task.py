string = input()
braces = []
for el in string:
    if el == "(":
        braces.append("(")
    if el == ")":
        try:
            braces.pop()
        except IndexError:
            print("ERROR")
            break
else:
    print("OK") if not braces else print("ERROR")
