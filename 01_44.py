def happy_number(n):
    n= str(n)
    l= len(n)
    s= 0
    for i in range(l):
        s+= int(n[i])**2
    return s
n= 81 # sample number
i= 0 # iteration count
while True:
    i+=1
    print(f'iteration: {i}\nvalue: {n}\n')
    if n == 1:
        print('happy number')
        exit()
    if i == 1000:
        print(f'iteration limit 1000 reached.\nnot a happy number.')
        exit()
    f= happy_number(n)
    n= f