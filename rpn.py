#!/usr/bin/env python3

import operator
import readline
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '//': operator.floordiv,
}

def print_colorized_input(args):
    colored_args = []
    for token in args.split():
        color = 'yellow' if token in operators else 'red' if int(token) < 0 else 'blue'
        colored_args.append(colored(token, color))
    print('User input: ' + ' '.join(colored_args))


def calculate(myarg):
    print_colorized_input(myarg)
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            # if token == '//':
            #     print('Found floordiv token')
            #     print('Sadly, this line has no test coverage')
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        color = 'red' if int(result) < 0 else 'blue'
        print("Result: ", colored(result, color))

if __name__ == '__main__':
    main()
