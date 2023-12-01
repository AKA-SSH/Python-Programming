n= input('enter:')
l= len(n)
s= 0
for i in range(l):
    s+=int(n[i])**l
print('armstrong' if int(n) == s else 'not armstrong')