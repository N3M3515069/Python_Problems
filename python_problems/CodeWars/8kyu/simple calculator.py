'''if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.

Example:
calculator(1, 2, '+') => 3
calculator(1, 2, '$') # result will be "unknown value"
Good luck!'''


def calculator(x, y, op):
    operators = '+', '-', '/', '*'
    if op in operators and type(x) == int and type(y) == int:
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '/':
            return x/y
        else:
            return x * y
    else:
        return "unknown value"
