d= {1: 5,
    2: 7,
    'k': 6,
    'g': 8,
    0: 'er'}
key_list= list(d.keys())
s= 0
for i in key_list:
    if type(d[i]) == int:
        s+=d[i]
    else:
        continue
print(s)