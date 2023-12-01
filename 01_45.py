# function for iteration
def happy_number_iteration(n):
    s= 0
    n= str(n)
    l= len(n)
    for i in range(l):
        s+= int(n[i])**2
    return s
# function for checking if a number is a happy number or not
def check_happy_number(n):
    for i in range(1000):
        f= n
        s= happy_number_iteration(f)
        n= s
        if n == 1:
            return n
# list comprehension
happy_numbers= [i for i in range(1, 101) if check_happy_number(i) == 1]
print(happy_numbers)