# File with all logic. Later it will be refactored or deleted.
import re
import math

OPERATORS = {'<': (1, lambda x, y: x < y), '<=': (1, lambda x, y: x <= y),
             '>': (1, lambda x, y: x > y), '>=': (1, lambda x, y: x >= y),
             '==': (1, lambda x, y: x == y), '!=': (1, lambda x, y: x != y),
             '+': (2, lambda x, y: x+y), '-': (2, lambda x, y: x-y),
             '*': (3, lambda x, y: x*y), '/': (3, lambda x, y: x/y),
             '//': (3, lambda x, y: x//y), '%': (3, lambda x, y: x%y),
             '^': (4, lambda x,y: x**y),
             'abs': (5, lambda x: abs(x)), 'round': (5, lambda x: round(x)),
             }
CONSTANTS = ('e', 'inf', 'nan', 'pi', 'tau')
def split_string(string_with_eq):
    """Splits input string with mathematical operations.
    Functions like sin will stay separately from "("
    """
    return re.findall(r">=|<=|==|!=|\/\/|\/|\d+\.?\d+|\w+|[\+\-\*\^\(\)]", string_with_eq.replace(' ',''))

def shunting_yard(list_of_eq):
    def is_float(input_str):
        try:
            float(input_str)
            return True
        except ValueError:
            return False


    stack = []

    for token in list_of_eq:
        # digits
        if is_float(token):
            yield float(token)
        # operator in OPERATORS
        elif token in OPERATORS:
            while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                yield stack.pop()
            stack.append(token)
        elif token == ')':
            # for right parenthesis we will return all elements from stack
            # after left parenthesis and then remove left parenthesis too
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                yield x
        elif token == '(':
            # just puts left patenthesis in stack
            stack.append(token)
        elif token in dir(math):
            #tries to find constant
            if token in CONSTANTS:
                yield getattr(math, token)
                continue
            # tries to find function
            method_to_call = getattr(math,token)
            OPERATORS[token] = (5, method_to_call)
            while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                yield stack.pop()
            stack.append(token)                
        else:
            raise AttributeError(f"Unknown function {token}")
    while stack:
        yield stack.pop()

def calc(polish):
    stack = []
    for token in polish:
        if token in OPERATORS:
            y, x = stack.pop(), stack.pop()
            stack.append(OPERATORS[token][1](x, y))
        else:
            stack.append(token)
    # this return condition is made to return integers as integers, float/boolean as float/boolean
    return int(stack[0]) if int(stack[0]) == stack[0] and type(stack[0])== float else stack[0]

if __name__ =="__main__":

    def compose(input_string):
        x = split_string(input_string)
        y = shunting_yard(x)
        # print(calc(y))
        # print(eval(input_string.replace('^', '**')))
        # return list(y)
        return calc(y)
    


    # print(compose("2+2+2+(12+3+55555-26262+sin(26263))"))
    print(compose("5^3"))
    print(compose("5//3"))
    print(compose("5.0//3"))
    print(compose("2!=3.0"))
    print(compose("pi*2"))
    # print(compose("11*sin(2 * 3+6)"))
