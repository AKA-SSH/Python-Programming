a= int(input('start:'))
b= int(input('end:'))
response= []
for x in range(a, b):
    n= str(x)
    l= len(n)
    s= 0
    for i in range(l):
        s+=int(n[i])**l
    if int(n) == s:
        response.append(s)
print(response)