def addition(x, y):
    return x+y
def subtraction(x, y):
    return x-y
def multiplication(x, y):
    return x*y
def division(x, y):
    return x/y
while True:
    o= input('enter operation:')
    if o == 'quit':
        exit()
    elif o == '+':
        x= float(input('X:'))
        y= float(input('Y:'))
        print(addition(x, y))
    elif o == '-':
        x= float(input('X:'))
        y= float(input('Y:'))
        print(subtraction(x, y))
    elif o == '*':
        x= float(input('X:'))
        y= float(input('Y:'))
        print(multiplication(x, y))
    elif o == '/':
        x= float(input('X:'))
        y= float(input('Y:'))
        print(division(x, y))