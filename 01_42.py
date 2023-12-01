n= input('number:')
l= len(n)
s= 0
for i in range(1, l+1):
    s+= int(n[i-1])**i
if int(n) == s:
    print('disarium number')
else:
    print('some vanilla ass number.')