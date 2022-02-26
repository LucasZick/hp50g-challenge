
def isInc(value):
    try:
        float(value)
        return False
    except ValueError:
        return True


opposite_ops = {
    "+": "-",
    "-": "+",
    "*": "/",
    "/": "*"
}


def calculate(calc):
    # Find the '='
    parts = calc.split("=")

    # Find the operator on the second part
    ex = parts[1]
    valid_op = ['+', '-', '*', '/']
    for op in valid_op:
        values = ex.split(op)
        if len(values) > 1:
            operator = op
            break
    values = [v.strip() for v in values]

    leftSide = parts[0].strip()

    # Choose the operation that will execute
    if isInc(leftSide):
        A = float(values[0])
        B = float(values[1])

    elif isInc(values[0]):
        A = float(leftSide)
        B = float(values[1])
        op = opposite_ops[op]

    elif isInc(values[1]):
        if op == '/' or op == '-':
            A = float(values[0])
            B = float(leftSide)
        elif op == '*' or op == '+':
            op = opposite_ops[op]
            A = float(leftSide)
            B = float(values[0])

    # Return the unknown number's value
    if op == '+':
        return A+B
    elif op == '-':
        return A-B
    elif op == '*':
        return A*B
    elif op == '/':
        return A/B


if __name__ == '__main__':
    stop = 1
    while stop != 0:
        print('--------------------------------------------------------------------------------------------------------------')
        str = input(
            '\nWrite the expression in the "A = B op C" containing an unknown number at some position\n\n                 ')
        print('--------------------------------------------------------------------------------------------------------------')
        print('\nThe unknown number is ', calculate(str), '\n')
        print('--------------------------------------------------------------------------------------------------------------')
        stop = int(input(
            '\nDo you want to try another expression?\n\n                 0 - No\n    Something else - Yes\n\n                 '))
        print('--------------------------------------------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------------------------------------------\n\n                 FINISHED THE EXECUTION')
