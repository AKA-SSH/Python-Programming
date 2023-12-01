s1= 'hello mister Parker, are you Spider-Man ?'
s2= 'hello miss Jane, are you Cat Woman ?'
s1_l= s1.split()
s2_l= s2.split()
s1_l= list(set(s1_l))
s2_l= list(set(s2_l))
unique= []
for i in s1_l:
    if i not in s2_l:
        unique.append(i)
for i in s2_l:
    if i not in s1_l:
        unique.append(i)
print(unique)