from collections import deque


class Calculator:
    def __init__(self):
        self.variables_dict = {}

    @staticmethod
    def addition(first, second):
        return first + second

    @staticmethod
    def subtraction(first, second):
        return first - second

    @staticmethod
    def multiplication(first, second):
        return first * second

    @staticmethod
    def division(first, second):
        return int(first / second)

    @staticmethod
    def power(first, second):
        return first ** second

    def add_variable(self, string):
        try:
            variable, value = string.split("=")
        except ValueError:
            print("Invalid assignment")
        else:
            variable = variable.strip()
            value = value.strip()
            if not variable.isalpha():
                print("Invalid identifier")
            elif not value.isdigit() and not value.isalpha():
                print("Invalid assignment")
            else:
                if value in self.variables_dict.keys():
                    self.variables_dict[variable] = self.variables_dict[value]
                elif value.isalpha():
                    print("Unknown variable")
                else:
                    self.variables_dict[variable] = value

    @staticmethod
    def parse_command(command):
        if command == "/help":
            print("The program calculates the sum of numbers")
            return 1
        if command == "/exit":
            print("Bye!")
            return 0
        print("Unknown command")
        return 1

    @staticmethod
    def clean_input(line):
        # remove all spaces
        clean_line = line.replace(' ', '')
        # check duplicates of */^ signs (using math rule)
        if any((rule in clean_line) for rule in ["**", "//", "^^", "+*", "-*", "+/", "-/",
                                                 "+^", "-^", "/*", "*/", "*^", "^*", "/^", "^/"]):
            print("Invalid expression")
            return False
        # unite all +- signs (using math rule)
        while any((rule in clean_line) for rule in ["--", "+-", "-+", "++"]):
            clean_line = clean_line.replace('--', '+')
            clean_line = clean_line.replace('++', '+')
            clean_line = clean_line.replace('-+', '-')
            clean_line = clean_line.replace('+-', '-')
        # add space before and after sign
        clean_line = clean_line.replace('+', ' + ').replace('-', ' - ')
        if clean_line.startswith(" - "):  # for "-" at start of line
            clean_line = "-" + clean_line[3:]
        clean_line = clean_line.replace('* + ', "*").replace('* - ', '*-')
        clean_line = clean_line.replace('/ + ', "/").replace('/ - ', '/-')
        clean_line = clean_line.replace('^ + ', "^").replace('^ - ', '^-')
        clean_line = clean_line.replace('*', ' * ').replace('/', ' / ').replace('^', ' ^ ')
        clean_line = clean_line.replace('(', ' ( ').replace(')', ' ) ')
        return clean_line

    @staticmethod
    def calculate_postfix_expression(tokens):
        numbers_stack = deque()
        for el in tokens:
            if el in ["+", "-", "*", "/", "^"]:
                b = numbers_stack.pop()  # second operand is popped first
                a = numbers_stack.pop()
                if el == "+":
                    numbers_stack.append(Calculator.addition(a, b))
                elif el == "-":
                    numbers_stack.append(Calculator.subtraction(a, b))
                elif el == "*":
                    numbers_stack.append(Calculator.multiplication(a, b))
                elif el == "/":
                    numbers_stack.append(Calculator.division(a, b))
                elif el == "^":
                    numbers_stack.append(Calculator.power(a, b))
            else:
                numbers_stack.append(el)
        return numbers_stack[0]

    @staticmethod
    def transform_to_postfix(tokens):
        output_stack = deque()
        operators_stack = deque()
        priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        for el in tokens:
            if isinstance(el, int):
                output_stack.append(el)
            elif el in priority.keys():
                if (not operators_stack or operators_stack[-1] == "(") or (priority[el] > priority[operators_stack[-1]]):
                    operators_stack.append(el)
                else:
                    while operators_stack and operators_stack[-1] != "(" \
                            and priority[el] <= priority[operators_stack[-1]]:
                        output_stack.append(operators_stack.pop())
                    operators_stack.append(el)
            elif el == "(":
                operators_stack.append(el)
            elif el == ")":
                try:
                    while operators_stack[-1] != "(":
                        output_stack.append(operators_stack.pop())
                    operators_stack.pop()  # pop "("
                except IndexError:
                    print("Invalid expression")
                    return False
        while operators_stack:
            if operators_stack[-1] != "(":
                output_stack.append(operators_stack.pop())
            else:
                print("Invalid expression")
                return False
        return output_stack

    def parse_token(self, token):
        try:
            if token.isalpha():
                return int(self.variables_dict[token])
            if token.isdigit() or (token.startswith("-") and len(token) > 1):
                return int(token)
            return token
        except KeyError:
            print("Unknown variable")
            return False
        except ValueError:
            print("Invalid identifier")
            return False

    def parse_string(self, string):
        string = Calculator.clean_input(string)
        if not string:
            return False
        tokens = string.split()
        tokens = [self.parse_token(el) for el in tokens]
        if not all(tokens):
            return False
        tokens = Calculator.transform_to_postfix(tokens)
        if tokens:
            print(Calculator.calculate_postfix_expression(tokens))

    def run(self):
        while True:
            user_input = input()
            if user_input.startswith("/"):
                if not self.parse_command(user_input):
                    break
            elif user_input == "":
                continue
            elif "=" in user_input:
                self.add_variable(user_input)
            else:
                try:
                    self.parse_string(user_input)
                except (ValueError, IndexError):
                    print("Invalid expression")


calculator = Calculator()
calculator.run()
