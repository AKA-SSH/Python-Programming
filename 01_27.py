def Fibonacci(x):
    if x <= 0:
        return 'enter valid input'
    elif x==1:
        return 0
    elif x==2:
        return 1
    else:
        return Fibonacci(x-1) + Fibonacci(x-2)
for i in range(1, 11):
    print(Fibonacci(i))