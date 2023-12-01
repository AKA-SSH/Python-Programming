s= 'apples'
set_s= set(s)
d= {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
duplicates= []
for j in set_s:
    if d[j]>1:
        duplicates.append(j)
    else:
        continue
print(duplicates)