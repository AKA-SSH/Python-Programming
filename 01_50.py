l= [1, 2, 3, 4, 5]
s= sum(l)
for i in l:
    if i < s:
        s = i
print(s)