def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
for num in range(2, 10000+1):
    if prime(num):
        print(num)