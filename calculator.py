print('=======\nThis is my 2 value calculator\n=======')
operators = ['+', '-', '*', '/', '^']

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if secondValue == 0:
        print('0 index on division\n=======')
        return '0_INDEX_ERROR'
    return str(int(x // y)) + ' R: ' + str(int(x % y))

def pow(x, y):
    return x**y

while True:
    output = 0
    firstValue = 0
    secondValue = 0
    operation = 0

    # first value
    firstValue = input('Value 1: ')
    if firstValue == 'exit':
        break
    else:
        firstValue = float(firstValue)

    # operation to perform
    operation = input('Operation: ')
    if operation == 'exit':
        break
    elif not operation in operators:
        print('not a valid operator, please choose from "=", "-", "*", "/", "^"\n=======')
        continue
    else:
        if operation == '+':
            operation = add
        elif operation == '-':
            operation = sub
        elif operation == '*':
            operation = mult
        elif operation == '/':
            operation = div
        elif operation == '^':
            operation = pow

    # second value
    secondValue = input('Value 2: ')
    if secondValue == 'exit':
        break
    else:
        secondValue = float(secondValue)

    # perform operation on values
    output = operation(firstValue, secondValue)
    if output == '0_INDEX_ERROR':
        continue
        
    # display output
    print('OUTPUT: ' + str(output) + '\n=======')
print('=======\nThank you for using my calculator!\n=======')
