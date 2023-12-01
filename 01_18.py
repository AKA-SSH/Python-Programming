r= int(input('range:'))
n1= 0
n2= 1
s= None
f= [0, 1]
for i in range(r):
    s= n1+n2
    n1, n2= n2, s
    f.append(s)
print(f)